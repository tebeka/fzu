#!/usr/bin/env python
"""Fuzzy search unicode symbols (requires fzf installed)"""

from argparse import ArgumentParser
from subprocess import run, PIPE
from pathlib import Path

__version__ = '0.1.0'


def main():
    parser = ArgumentParser(description=__doc__, prog='fzu')
    parser.add_argument(
        '--version', help='print version & exit', action='store_true',
        default=False)
    args = parser.parse_args()
    if args.version:
        print(__version__)
        raise SystemExit()

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
