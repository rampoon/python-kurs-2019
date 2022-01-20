#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re, os, inspect
from importlib import import_module

from contextlib import redirect_stdout, redirect_stderr

name = "aritmetik"
mod = import_module(name)


def test_modul():
    os.chdir(os.path.dirname(__file__))
    assert 'addera' in dir(mod), \
        "addera ska finnas i modulen " + name
    assert inspect.isfunction(mod.addera), \
        "addera ska vara en funktion"


def test_anrop():
    assert mod.addera(2, 3) == 5, \
        "addera(2, 3) ska returnera 5"
    assert mod.addera(3.5, 11.5) == 15, \
        "addera(3.5, 11.5) ska returnera 15"
    assert mod.addera(-2, 2) == 0, \
        "addera(-2, 2) ska returnera 0"


if __name__ == '__main__':
    pytest.main(['-vx'])
