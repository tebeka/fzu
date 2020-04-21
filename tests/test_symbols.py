import unicodedata

import pytest

from fzu.symbols import symbols


@pytest.mark.parametrize('symbol', symbols)
def test_symbol(symbol):
    try:
        unicodedata.lookup(symbol)
    except KeyError:
        raise AssertionError(symbol)
