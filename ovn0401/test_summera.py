#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re, os
from importlib import import_module

from contextlib import redirect_stdout

name = "summera"


def test_summera():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]

    os.chdir(os.path.dirname(__file__))

    tot = 0
    with open("tal.txt") as fh:
        for line in fh:
            tot += int(line)

    with redirect_stdout(f):
        import_module(name)

    assert re.search(r"\b" + str(tot) + r"\b", f.getvalue()), \
        "Summan ska vara " + str(tot) + ", fick " + f.getvalue()


if __name__ == '__main__':
    pytest.main(['-vx'])
