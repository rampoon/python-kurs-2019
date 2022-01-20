#!/usr/bin/python3
# coding=utf-8

import inspect
import os
import pickle
import pytest
import sparapickle
import sys


def test_funktioner():
    assert 'sparapickle' in dir(sparapickle), \
        "hittar inte sparapickle"
    assert inspect.isfunction(sparapickle.sparapickle), \
        "sparapickle är inte en funktion"
    assert 'laddapickle' in dir(sparapickle), \
        "hittar inte laddapickle"
    assert inspect.isfunction(sparapickle.laddapickle), \
        "laddapickle är inte en funktion"


def anropa(data, filename):
    os.chdir(os.path.dirname(__file__))
    sparapickle.sparapickle(data, filename)
    assert os.path.isfile(filename), \
        "Filen " + filename + " skapades inte"
    try:
        with open(filename, "rb") as fh:
            rdata = pickle.load(fh)
            assert rdata == data, \
                "Fick " + str(rdata) + ", skulle få " + str(data)
    except pickle.UnpicklingError:
        assert False, \
            "Ogiltig Pickledata sparades"
    except Exception as err:
        assert False, \
            "Kunde inte läsa in " + filename + ": " + str(err)
    rdata = sparapickle.laddapickle(filename)
    assert data == rdata, \
        "laddapickle returnerade " + str(rdata) + " skulle få " + str(data)


def ladda(data, filname):
    os.chdir(os.path.dirname(__file__))


def test_lista():
    anropa([3, 4, 6], "ptst1.pickle")


def test_unicodesträngar():
    anropa(["Åsa", "Göran"], "ptst2.pickle")


def test_heltal():
    anropa(117, "ptst3.pickle")


def test_objekt():
    scores = dict(Bill=12, Steve=19, Linus=33, Ken=27)
    anropa(scores, "ptst4.pickle")


if __name__ == '__main__':
    pytest.main(['-vx'])
