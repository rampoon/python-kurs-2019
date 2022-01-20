#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re, os
from importlib import import_module

from contextlib import redirect_stdout

name = "palindrom"


def test_summera():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]

    os.chdir(os.path.dirname(__file__))

    tot = 0
    S = set()
    with open("ord.txt") as fh:
        for rad in fh:
            ord = rad.rstrip().lower()
            l = ord[::-1]
            if l == ord:
                S.add(ord.lower())

    with redirect_stdout(f):
        import_module(name)

    T = set(f.getvalue().lower().split())

    assert S == T, \
        str(S) + " förväntat, fick " + str(T)


if __name__ == '__main__':
    pytest.main(['-vx'])
