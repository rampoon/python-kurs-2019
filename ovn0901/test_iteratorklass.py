#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re, os, inspect
from importlib import import_module

from contextlib import redirect_stdout, redirect_stderr

name = "iteratorklass"
klass = "it"

mod = import_module(name)


def test_modul():
    assert 'it' in dir(mod), \
        klass + " ska finnas i modulen " + name
    assert inspect.isclass(mod.it), \
        klass + " ska vara en klass"


def test_konstruktor():
    obj = mod.it(5)


def test_iter():
    obj = mod.it(5)
    a = iter(obj)


def test_forsta_noll():
    obj = mod.it(5)
    a = iter(obj)
    assert next(a) == 0, \
        "första iterationen ska returnera 0"


def test_next():
    obj = mod.it(2)
    a = iter(obj)
    assert next(a) == 0, \
        "första iterationen ska returnera 0"
    assert next(a) == 2, \
        "it(2) ska öka med 2 för varje iteration"
    assert next(a) == 4, \
        "it(2) ska öka med 2 för varje iteration"


def test_loop():
    s = 0
    for x in mod.it(3):
        if x > 13:
            break
        else:
            s += x
    assert s == 3 + 6 + 9 + 12, \
        "det ska gå att loopa över it(3)"

if __name__ == '__main__':
    pytest.main(['-vx'])
