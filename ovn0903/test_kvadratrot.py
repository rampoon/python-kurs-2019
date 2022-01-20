#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re, os, inspect
from importlib import import_module

from contextlib import redirect_stdout, redirect_stderr

name = "kvadratrot"

mod = import_module(name)


def test_modul():
    for funk in "f1 f2 f3".split():
        assert funk in dir(mod), \
            funk + " ska finnas i modulen " + name
    assert inspect.isfunction(mod.f1), \
        "f1 ska vara en funktion"
    assert inspect.isfunction(mod.f2), \
        "f2 ska vara en funktion"
    assert inspect.isfunction(mod.f3), \
        "f3 ska vara en funktion"


def test_f1():
    obj = mod.f1(10)
    assert isinstance(obj, map), \
        "f1(10) ska vara av typen map"
    L = list(obj)
    assert len(L) == 9, \
        "f1(10) ska vara en sekvens av längden 9"
    assert L[0] == 1 and L[8] == 3, \
        "f1(10) ska vara en sekvens av kvadratrötter"


def test_f2():
    obj = mod.f2(10)
    assert isinstance(obj, list), \
        "f2(10) ska vara av typen list"
    L = list(obj)
    assert len(L) == 9, \
        "f2(10) ska vara en lista av längden 9"
    assert L[0] == 1 and L[8] == 3, \
        "f2(10) ska vara en lista av kvadratrötter"


def test_f3():
    obj = mod.f3(10)
    assert inspect.isgenerator(obj), \
        "f3(10) ska vara en generator"
    L = list(obj)
    assert len(L) == 9, \
        "f3(10) ska vara en sekvens av längden 9"
    assert L[0] == 1 and L[8] == 3, \
        "f3(10) ska vara en sekvens av kvadratrötter"


if __name__ == '__main__':
    pytest.main(['-vx'])
