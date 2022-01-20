#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re, os
from importlib import import_module

from contextlib import redirect_stdout

name = "webbsida"


def test_webbsida():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]

    with redirect_stdout(f):
        import_module(name)

    assert re.search(r'\b400\b', f.getvalue()), \
        "400 förväntat, fick " + f.getvalue()
