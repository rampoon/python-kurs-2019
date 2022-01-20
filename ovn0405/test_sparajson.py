#!/usr/bin/python3
# coding=utf-8

import pytest
import sys, inspect, os

import json
import sparajson


def test_funktioner():
    assert 'sparajson' in dir(sparajson), \
        "hittar inte sparajson"
    assert inspect.isfunction(sparajson.sparajson), \
        "sparajson är inte en funktion"
    assert 'laddajson' in dir(sparajson), \
        "hittar inte laddajson"
    assert inspect.isfunction(sparajson.laddajson), \
        "laddajson är inte en funktion"


def anropa(data, filename):
    os.chdir(os.path.dirname(__file__))
    sparajson.sparajson(data, filename)
    assert os.path.isfile(filename), \
        "Filen " + filename + " skapades inte"
    try:
        with open(filename) as fh:
            txt = fh.read()
            rdata = json.loads(txt)
            assert rdata == data, \
                "Fick " + txt + ", skulle få " + json.dumps(data)
    except json.decoder.JSONDecodeError:
        assert False, \
            "Ogiltig JSON sparades"
    except Exception as err:
        assert False, \
            "Kunde inte läsa in " + filename + ": " + str(err)
    rdata = sparajson.laddajson(filename)
    assert data == rdata, \
        "laddajson returnerade " + str(rdata) + " skulle få " + str(data)


def ladda(data, filname):
    os.chdir(os.path.dirname(__file__))


def test_lista():
    anropa([3, 4, 6], "ptst1.json")


def test_unicodesträngar():
    anropa(["Åsa", "Göran"], "ptst2.json")


def test_heltal():
    anropa(117, "ptst3.json")


def test_objekt():
    scores = dict(Bill=12, Steve=19, Linus=33, Ken=27)
    anropa(scores, "ptst4.json")


if __name__ == '__main__':
    pytest.main(['-vx'])
