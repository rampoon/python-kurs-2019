#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, os, inspect
import re, locale

from importlib import import_module
from contextlib import redirect_stdout, redirect_stderr

name = "hittaord"

mod = import_module(name)


def _allaord(filnamn):
    try:
        s = set()
        with open(filnamn, encoding="utf-8") as infil:
            for rad in infil:
                for ord in re.split(r'[\W\d_]+', rad):
                    s.add(ord)
            s.remove('')
            L = list(s)
            try:
                old = locale.setlocale(locale.LC_COLLATE, None)
                locale.setlocale(locale.LC_COLLATE, "sv_SE.UTF-8")
                L.sort(key=locale.strxfrm)
                locale.setlocale(locale.LC_COLLATE, old)
            except:
                L.sort()
            return " ".join(L)
    except IOError as err:
        pass


def test_ladda():
    assert 'allaord' in dir(mod), \
        "allaord ska finnas i " + name
    assert inspect.isfunction(mod.allaord), \
        "allaord ska vara en funktion"


def check_file(fn):
    os.chdir(os.path.dirname(__file__))
    res = _allaord(fn)
    got = mod.allaord(fn)
    assert got == res, \
        'Fil ' + str(fn) + ' fick "' + str(got) + \
        '", skulle få "' + str(res) + '".'


def test_fil():
    check_file("fil.txt")


def test_carlsson():
    check_file("carlsson.txt")


def test_ingaord():
    check_file("ingaord.txt")


def test_filsaknas():
    check_file("nosuchfile.bin")
