#!/usr/bin/env python
"""Fuzzy search unicode symbols (requires fzf installed)"""

from argparse import ArgumentParser
from subprocess import run, PIPE
from pathlib import Path
from zipfile import is_zipfile, ZipFile
import sys
from getpass import getuser
from tempfile import gettempdir

__version__ = '0.1.3'

tmp_dir: Path = Path(gettempdir()) / f'fzu-{getuser()}'


def has_fzf():
    try:
        out = run(['fzf', '--help'], capture_output=True)
        return out.returncode == 0
    except OSError:
        return False


def should_extract(exe):
    if not tmp_dir.exists():
        return True

    return Path(exe).stat().st_mtime > tmp_dir.stat().st_mtime


def extract_files(exe):
    if not should_extract(exe):
        return

    tmp_dir.mkdir(parents=True, exist_ok=True)
    with ZipFile(exe) as zf:
        zf.extractall(tmp_dir)


def main():
    parser = ArgumentParser(description=__doc__, prog='fzu')
    parser.add_argument(
        '--version', help='print version & exit', action='store_true',
        default=False)
    args = parser.parse_args()
    if args.version:
        print(__version__)
        raise SystemExit()

    exe = sys.argv[0]
    if is_zipfile(exe):
        extract_files(exe)
        symbols_dir = tmp_dir / 'symbols'
    else:
        symbols_dir = Path(__file__).parent.absolute() / 'symbols'

    if not has_fzf():
        raise SystemExit('error: fzf not found, please install it')

    out = run(['fzf', '--preview', 'cat {}'], cwd=symbols_dir, stdout=PIPE)
    if out.returncode != 0:
        raise SystemExit()

    sym_file = symbols_dir / out.stdout.decode('utf-8').strip()
    with sym_file.open() as fp:
        sym = fp.read()
    print(sym)


if __name__ == '__main__':
    main()
