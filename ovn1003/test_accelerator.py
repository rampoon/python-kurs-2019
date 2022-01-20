#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, os, inspect
import re, locale

from importlib import import_module
from contextlib import redirect_stdout, redirect_stderr

name = "accelerator"

mod = import_module(name)


def test_ladda():
    assert 'webbot' in dir(mod), \
        "webbot ska finnas i " + name
    assert inspect.isfunction(mod.webbot), \
        "webbot ska vara en funktion"


def check_url(url, kat, links):
    mod.webbot(url, kat)
    assert os.path.isdir(kat), \
        "webbsida ska skapa katalogen " + kat
    L = os.listdir(kat)
    assert "main.html" in L, \
        "webbsida ska skapa filen main.html i " + kat
    assert len(L) > len(links), \
        "webbsida ska spara hämtade sidor i " + kat
    found = set()
    for file in L:
        if file != "main.html":
            with open(os.path.join(kat, file), "rb") as fh:
                data = fh.read()
                for s in links:
                    if data.find(s) >= 0:
                        found.add(s)
    for s in links:
        assert s in found, \
            "sparad webbsida ska innehålla " + str(s)


def test_url():
    check_url("http://beta1.bredbandskollen.se/enkel.html", "enkel",
              {b"Sundsvall", b"ttl"})


if __name__ == '__main__':
    pytest.main(['-vx'])
