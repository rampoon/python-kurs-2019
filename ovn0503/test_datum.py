#!/usr/bin/python3
# coding=utf-8

import io, sys, re, os
from importlib import import_module

from contextlib import redirect_stdout

name = "datum"


def no_days(a, b):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    d1, m1 = a.split("/")
    d2, m2 = b.split("/")
    n = sum(days[int(m1):int(m2)]) + int(d2) - int(d1) + 1
    return n


def mdiff(a, b):
    if name in sys.modules: del sys.modules[name]
    f = io.StringIO()
    with redirect_stdout(f):
        sys.argv = ["verify.py", a, b]
        import_module(name)
        output = f.getvalue().strip()
    res = str(no_days(a, b))
    assert re.search(r"\b" + res + r"\b", output), \
        "Fick " + output + ", skulle få " + res


def test_28aug_24dec():
    mdiff("28/8", "24/12")


def test_1jan_31dec():
    mdiff("1/1", "31/12")


def test_7okt_7okt():
    mdiff("7/10", "7/10")


if __name__ == '__main__':
    import pytest
    pytest.main(['-vx'])
