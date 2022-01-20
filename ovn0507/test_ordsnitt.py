#!/usr/bin/python3
# coding=utf-8

import pytest
import sys, inspect, os

import ordsnitt


def allaord(fh):
    orden = set()
    for rad in fh:
        for ordet in rad.split():
            orden.add(ordet.rstrip("-!?:,."))
    return orden


def gem_ord(f1, f2):
    with open(f1, encoding="utf-8") as fh1, open(f2, encoding="utf-8") as fh2:
        m1 = allaord(fh1)
        m2 = allaord(fh2)
        return m1 & m2


def test_ladda():
    assert 'gemensamma_ord' in dir(ordsnitt), \
        "hittar inte gemensamma_ord"
    assert inspect.isfunction(ordsnitt.gemensamma_ord), \
        "gemensamma_ord är inte en funktion"


def anropa(fn1, fn2):
    os.chdir(os.path.dirname(__file__))
    data = gem_ord(fn1, fn2)
    rdata = ordsnitt.gemensamma_ord(fn1, fn2)
    assert data == rdata, \
        "fick " + str(rdata) + " skulle få " + str(data)


def test_anrop():
    anropa("fil.txt", "carlsson.txt")


if __name__ == '__main__':
    pytest.main(['-vx'])
