#!/usr/bin/env python
"""Fuzzy search unicode symbols (requires fzf installed)"""

from argparse import ArgumentParser
from subprocess import run, PIPE
from pathlib import Path

from fzu import __version__


def has_fzf():
    try:
        out = run(['fzf', '--help'], capture_output=True)
        return out.returncode == 0
    except OSError:
        return False


def main():
    parser = ArgumentParser(description=__doc__, prog='fzu')
    parser.add_argument(
        '--version', help='print version & exit', action='store_true',
        default=False)
    args = parser.parse_args()
    if args.version:
        print(__version__)
        raise SystemExit()

    if not has_fzf():
        raise SystemExit('error: fzf not found, please install it')

    symbols = Path(__file__).parent.absolute() / 'symbols'
    out = run(['fzf', '--preview', 'cat {}'], cwd=symbols, stdout=PIPE)
    if out.returncode != 0:
        raise SystemExit()

    sym_file = symbols / out.stdout.decode('utf-8').strip()
    with sym_file.open() as fp:
        sym = fp.read()
    print(sym)


if __name__ == '__main__':
    main()
