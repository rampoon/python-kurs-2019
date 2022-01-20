#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re
from importlib import import_module

from contextlib import redirect_stdout

name = "frukter"


def test_frukter():
    f = io.StringIO()
    with redirect_stdout(f):
        if name in sys.modules: del sys.modules[name]
        sys.stdin = io.StringIO("10\r\n2\r\n-1\r\n")
        import_module(name)
    rx = "banan.*21.*plommon.*18.*ron.*25.*pple.*15.*"
    assert re.search(rx, f.getvalue(), re.I | re.S), \
        "Fel utskrift, fick " + f.getvalue()


if __name__ == '__main__':
    pytest.main(['-vx'])
