#!/usr/bin/env python
"""Fuzzy search unicode symbols"""

from argparse import ArgumentParser
from subprocess import run, PIPE
from pathlib import Path

parser = ArgumentParser(description=__doc__)
args = parser.parse_args()

symbols = Path(__file__).parent.absolute() / 'symbols'
out = run(['fzf', '--preview', 'cat {}'], cwd=symbols, stdout=PIPE)
if out.returncode != 0:
    raise SystemExit('error: cannot find')

sym_file = symbols / out.stdout.decode('utf-8').strip()
with sym_file.open() as fp:
    sym = fp.read()
print(sym)
