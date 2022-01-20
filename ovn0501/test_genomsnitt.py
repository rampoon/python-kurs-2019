#!/usr/bin/python3
# coding=utf-8

import io, sys, re, os
from importlib import import_module

from contextlib import redirect_stdout

name = "genomsnitt"


def myavg(filename):
    try:
        L = [int(line) for line in open(filename)]
        L.sort()
        L = L[3:-3]
        avg = sum(L) / len(L)
        return avg
    except:
        return None


def checkfile(filename):
    if name in sys.modules: del sys.modules[name]
    os.chdir(os.path.dirname(__file__))
    f = io.StringIO()
    with redirect_stdout(f):
        sys.argv = ["verify.py", filename]
        import_module(name)
        output = f.getvalue().strip()
    res = str(myavg(filename))
    assert re.search(r"\b" + res + r"\b", output), \
        "Fick " + output + ", skulle få " + res


def test_tal():
    checkfile("tal.txt")


def test_tal2():
    checkfile("tal2.txt")


if __name__ == '__main__':
    import pytest
    pytest.main(['-vx'])
