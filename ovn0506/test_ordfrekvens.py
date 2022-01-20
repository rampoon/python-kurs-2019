#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re, os
from importlib import import_module

from contextlib import redirect_stdout

name = "ordfrekvens"


def test_fil():
    os.chdir(os.path.dirname(__file__))
    f = io.StringIO()
    with redirect_stdout(f):
        if name in sys.modules: del sys.modules[name]
        sys.argv = ["verify.py", "fil.txt"]
        import_module(name)
    rx = r"och.*3.*tre.*2.*fyra.*1"
    assert re.search(rx, f.getvalue(), re.I | re.S), \
        "Fel utskrift, fick " + f.getvalue()


def test_carlsson():
    os.chdir(os.path.dirname(__file__))
    f = io.StringIO()
    with redirect_stdout(f):
        if name in sys.modules: del sys.modules[name]
        sys.argv = ["verify.py", "carlsson.txt"]
        import_module(name)
    rx = r"och.*12.*\bde.*6.*\bett[^\n]*4.*\bhade.*3"
    assert re.search(rx, f.getvalue(), re.I | re.S), \
        "Fel utskrift, fick " + f.getvalue()


if __name__ == '__main__':
    pytest.main(['-vx'])
