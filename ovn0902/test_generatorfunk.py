#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re, os, inspect
from importlib import import_module

from contextlib import redirect_stdout, redirect_stderr

name = "generatorfunk"

mod = import_module(name)


def test_modul():
    assert 'Stega' in dir(mod), \
        "Stega ska finnas i modulen " + name
    assert inspect.isgeneratorfunction(mod.Stega), \
        "Stega ska vara en generatorfunktion"


def test_anrop():
    obj = mod.Stega(5)


def test_forsta_noll():
    a = mod.Stega(5)
    assert next(a) == 0, \
        "första iterationen ska returnera 0"


def test_next():
    a = mod.Stega(2)
    assert next(a) == 0, \
        "första iterationen ska returnera 0"
    assert next(a) == 2, \
        "it(2) ska öka med 2 för varje iteration"
    assert next(a) == 4, \
        "it(2) ska öka med 2 för varje iteration"


def test_loop():
    s = 0
    for x in mod.Stega(3):
        if x > 13:
            break
        else:
            s += x
    assert s == 3 + 6 + 9 + 12, \
        "det ska gå att loopa över it(3)"


if __name__ == '__main__':
    pytest.main(['-vx'])
