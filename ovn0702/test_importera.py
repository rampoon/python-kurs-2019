#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re, os, inspect
from importlib import import_module

from contextlib import redirect_stdout, redirect_stderr

name = "importera"
mname = "aritmetik"


def test_importera():
    os.chdir(os.path.dirname(__file__))
    f = io.StringIO()
    with redirect_stdout(f):
        try:
            import_module(name)
        except ModuleNotFoundError:
            pass

        assert name in sys.modules, \
            "kan inte ladda programmet " + name
        assert mname in sys.modules, \
            "programmet " + mname + " ska importera modulen"
        assert re.search(r"\b5\b", f.getvalue()), \
            "Summan 5 ska skrivas ut, fick " + f.getvalue()
        assert inspect.isfunction(sys.modules[mname].addera), \
            "den importerade modulen ska innehålla funktionen addera"


if __name__ == '__main__':
    pytest.main(['-vx'])
