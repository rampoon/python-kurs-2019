#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, os, inspect
import re, locale

from importlib import import_module
from contextlib import redirect_stdout, redirect_stderr

name = "leta"

mod = import_module(name)


def test_ladda():
    assert 'allalankar' in dir(mod), \
        "allalankar ska finnas i " + name
    assert inspect.isfunction(mod.allalankar), \
        "allalankar ska vara en funktion"


def check_url(url, linkset):
    res = mod.allalankar(url)
    assert isinstance(res, set), \
        "webbsida ska returnera ett set, fick " + str(type(res))

    assert res & linkset == linkset, \
        url + " ska innehålla " + str(linkset)


def test_url():
    res = {
        "http://get.adobe.com/flashplayer/",
        "https://www.webbstjarnan.se/",
        'https://www.iis.se/',
    }
    check_url("http://beta1.bredbandskollen.se/", res)


def test_ingalankar():
    res = mod.allalankar("http://beta1.bredbandskollen.se/settings.php")
    assert res == set(), \
        "Webbsida utan länkar, skulle få tom mängd"


def test_baddomain():
    res = mod.allalankar("http://beta99.bredbandskollen.se/")
    assert res == set(), \
        "allalankar ska returnera tom mängd om hämtningen misslyckades"


if __name__ == '__main__':
    pytest.main(['-vx'])
