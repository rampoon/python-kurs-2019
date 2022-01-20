#!/usr/bin/python3
# coding=utf-8

import pytest
import sys, inspect, os

import vokaler


def antal_vokaler2(filnamn):
    antal = 0
    vokaler = frozenset("aouåeiyäö")
    with open(filnamn, encoding="utf-8") as fh:
        for rad in fh:
            for bokstav in rad.lower():
                antal += bokstav in vokaler

    return antal


def test_ladda():
    assert 'antal_vokaler' in dir(vokaler), \
        "hittar inte antal_vokaler"
    assert inspect.isfunction(vokaler.antal_vokaler), \
        "antal_vokaler är inte en funktion"


def anropa(filename):
    os.chdir(os.path.dirname(__file__))
    data = antal_vokaler2(filename)
    rdata = vokaler.antal_vokaler(filename)
    assert data == rdata, \
        "fick " + str(rdata) + " skulle få " + str(data)


def test_fil():
    anropa("fil.txt")


def test_carlsson():
    anropa("carlsson.txt")
