#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re
from importlib import import_module

from contextlib import redirect_stdout

name = "tallista"


def test_avsluta_med_0():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]
    with redirect_stdout(f):
        sys.stdin = io.StringIO("1\r\n10\r\n0\r\n")
        import_module(name)


def test_antal():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]
    with redirect_stdout(f):
        sys.stdin = io.StringIO("1\r\n10\r\n0\r\n")
        import_module(name)

    L = [int(x) for x in f.getvalue().splitlines()]

    assert len(L) == 2, \
        "Två tal matades in men " + str(len(L)) + " skrevs ut"


def test_sortering():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]
    with redirect_stdout(f):
        sys.stdin = io.StringIO("3\r\n20\r\n6\r\n0\r\n")
        import_module(name)

    L = [int(x) for x in f.getvalue().splitlines()]
    assert L == [3, 6, 20], \
        "Matade in 3, 20, 6 men fick " + str(L)


def test_dubbletter():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]
    with redirect_stdout(f):
        sys.stdin = io.StringIO("3\r\n20\r\n6\r\n20\r\n20\r\n44\r\n0\r\n")
        import_module(name)

    L = [int(x) for x in f.getvalue().splitlines()]
    assert L == [3, 6, 20, 44], \
        "Matade in 3, 20, 6, 20, 20, 44 men fick " + str(L)


if __name__ == '__main__':
    pytest.main(['-vx'])
