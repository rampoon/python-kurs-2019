#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re
from importlib import import_module

from contextlib import redirect_stdout

name = "sekvens"


def test_prompt():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]
    with redirect_stdout(f):
        sys.stdin = io.StringIO("1\r\n10\r\n0\r\n")
        try:
            import_module(name)
        except:
            pass
    assert re.search(r"start.+stop.+in.rement",
                     f.getvalue(), re.I | re.M), \
        "ska fråga efter start, stop och increment"


def test_sequence():
    f = io.StringIO()
    try:
        with redirect_stdout(f):
            if name in sys.modules: del sys.modules[name]
            sys.stdin = io.StringIO("3\r\n10\r\n2\r\n1\r\n2\r\n0\r\n")
            import_module(name)
    except:
        pass

    assert re.search(r"rement\D+3\s+5\s+7\s+9\s*$",
                     f.getvalue(), re.I | re.M), \
        "range(3, 10, 2) ska vara 3 5 7 9"


def test_sequence2():
    f = io.StringIO()
    try:
        with redirect_stdout(f):
            if name in sys.modules: del sys.modules[name]
            sys.stdin = io.StringIO("19\r\n22\r\n1\r\n-10\r\n21\r\n5\r\n1\r\n2\r\n0\r\n")
            import_module(name)
    except:
        pass

    assert re.search(r"rement\D+19\s+20\s+21\s*$",
                     f.getvalue(), re.I | re.M), \
        "range(19, 22, 1) ska vara 19 20 21"

    assert re.search(r"rement\D+-10\s+-5\s+0\s+5\s+10\s+15\s+20\s*$",
                     f.getvalue(), re.I | re.M), \
        "range(-10, 21, 5) ska vara -10 -5 0 5 10 15 20"


def test_quit():
    f = io.StringIO()
    with redirect_stdout(f):
        if name in sys.modules: del sys.modules[name]
        sys.stdin = io.StringIO("1\r\n2\r\n0\r\n")
        try:
            import_module(name)
        except SystemExit:
            pass


def test_quit2():
    f = io.StringIO()
    with redirect_stdout(f):
        if name in sys.modules: del sys.modules[name]
        sys.stdin = io.StringIO("10\r\n2\r\n-1\r\n")
        try:
            import_module(name)
        except SystemExit:
            pass


if __name__ == '__main__':
    pytest.main(['-vx'])
