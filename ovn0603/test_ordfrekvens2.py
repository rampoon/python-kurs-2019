#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re, os
from importlib import import_module

from contextlib import redirect_stdout, redirect_stderr

name = "ordfrekvens2"


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


def test_missing_file():
    os.chdir(os.path.dirname(__file__))
    f = io.StringIO()
    with pytest.raises(SystemExit):
        with redirect_stderr(f):
            if name in sys.modules: del sys.modules[name]
            sys.argv = ["verify.py", "no_such_file"]
            import_module(name)
    assert len(f.getvalue()), \
        "Inget felmeddelande skrevs ut"


def test_bad_encoding():
    os.chdir(os.path.dirname(__file__))
    f = io.StringIO()
    with pytest.raises(SystemExit):
        with redirect_stderr(f):
            if name in sys.modules: del sys.modules[name]
            sys.argv = ["verify.py", "fil-latin1.txt"]
            import_module(name)
    assert len(f.getvalue()), \
        "Inget felmeddelande skrevs ut"


if __name__ == '__main__':
    pytest.main(['-vx'])
