#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, os, inspect
import re, locale

from importlib import import_module
from contextlib import redirect_stdout, redirect_stderr

name = "slurp"

mod = import_module(name)


def test_ladda():
    assert 'webbsida' in dir(mod), \
        "webbsida ska finnas i " + name
    assert inspect.isfunction(mod.webbsida), \
        "webbsida ska vara en funktion"


def check_url(url, substr):
    res = mod.webbsida(url)
    assert isinstance(res, str), \
        "webbsida ska returnera en sträng, fick " + str(type(res))

    assert res.find(substr) >= 0, \
        url + " ska innehålla " + substr


def test_url1():
    check_url("http://beta4.bredbandskollen.se/api/servers", "Sundsvall")


def test_url2():
    check_url("http://lab02.bredbandskollen.se/ticket", "ttl")


if __name__ == '__main__':
    pytest.main(['-vx'])
