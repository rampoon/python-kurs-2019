#!/usr/bin/python3
# coding=utf-8

import io, sys, re, os
from importlib import import_module

from contextlib import redirect_stdout

name = "manader"


def no_days(a, b):
    days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days[a:b + 1])


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


def test_mar_maj():
    mdiff(3, 5)


def test_jan_dec():
    mdiff(1, 12)


def test_okt_okt():
    mdiff(10, 10)


if __name__ == '__main__':
    import pytest
    pytest.main(['-vx'])
