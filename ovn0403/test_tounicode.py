#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re, os
from importlib import import_module

from contextlib import redirect_stdout

name = "tounicode"


def test_konvertera():
    os.chdir(os.path.dirname(__file__))

    with open("fil2.txt", encoding="latin-1") as fh:
        oldtext = fh.read()

    import_module(name)

    assert os.path.isfile("fil3.txt"), \
        "filen fil3.txt skapades inte"

    try:
        with open("fil3.txt", encoding="utf-8") as fh:
            newtext = fh.read()
    except UnicodeDecodeError:
        assert False, \
            "filen fil3.txt är inte kodad i utf-8"

    assert oldtext == newtext, \
        oldtext + " förväntat, fick " + newtext


if __name__ == '__main__':
    pytest.main(['-vx'])
