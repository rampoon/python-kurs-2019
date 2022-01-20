#!/usr/bin/python3
# coding=utf-8

import io, sys
from importlib import import_module

from contextlib import redirect_stdout

name = "skrivtal"

output = ""


def test_load():
    global output
    f = io.StringIO()
    with redirect_stdout(f):
        try:
            import_module(name)
        except:
            pass
        output = f.getvalue()


def test_first_line():
    L = output.splitlines()
    assert L, "the program should print to stdout"
    if L:
        assert L[0].strip() == "0", \
            "first line of output should be 0"


def test_numbers():
    L = output.splitlines()
    assert len(L) > 20, \
        "there should be at least 21 lines of output"
    if len(L) > 20:
        del L[21:]
        LL = [str(n) for n in range(21)]
        assert L == LL, \
            "the numbers 0, 1, ..., 20 should be printed"


def test_sum():
    L = output.splitlines()
    assert len(L) == 22, \
        "there should be exactly 22 lines of output"
    if L:
        assert L[-1].strip() == "210"


if __name__ == '__main__':
    import pytest
    pytest.main(['-vx'])
