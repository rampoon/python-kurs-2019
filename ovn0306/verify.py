#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re
from importlib import import_module

from contextlib import redirect_stdout

name = "frekvent"


def test_avsluta_med_blankrad():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]
    with redirect_stdout(f):
        sys.stdin = io.StringIO("hej och hå\n\n")
        import_module(name)
    assert f.getvalue(), \
        "Utskrift förväntades, fick ingen"


def test_frekvent():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]
    with redirect_stdout(f):
        sys.stdin = io.StringIO("ett och två\nsamt tre och fyra\n\n")
        import_module(name)

    res = f.getvalue()

    assert re.search(r'\boch\b', res), \
        "Resultatet 'och' förväntades, fick <" + res + ">"


def test_radbrytning():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]
    with redirect_stdout(f):
        sys.stdin = io.StringIO("tal ett ett\nett och tal tre\n\n")
        import_module(name)

    res = f.getvalue()

    assert re.search(r'\bett\b', res), \
        "Resultatet 'ett' förväntades: tal ett ett\nett och tal tre"


def test_dubbletter():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]
    with redirect_stdout(f):
        sys.stdin = io.StringIO("tal ett och\nett och annat tal\n\n")
        import_module(name)

    res = f.getvalue()

    assert re.search(r'\bett\b', res), \
        "Resultatet 'ett' förväntades: tal ett och\nett och annat tal"
