#!/usr/bin/python3
# coding=utf-8

import pytest
import sys, inspect

import funktion2 as funktion


def test_ladda():
    assert 'maxtal' in dir(funktion), \
        "hittar inte maxtal"
    assert inspect.isfunction(funktion.maxtal), \
        "maxtal är inte en funktion"


def test_anrop():
    assert funktion.maxtal([12, -6, 8]) == 12, \
        "maxtal([12, -6, 8]) ska vara 12"
    assert funktion.maxtal([1, 2, 4, 3]) == 4, \
        "maxtal([1, 2, 4, 3]) ska vara 4"
    assert funktion.maxtal([2.5, -19.4, 12.5]) == 12.5, \
        "maxtal([2.5, -19.4, 12.5]) ska vara 12.5"
    assert funktion.maxtal([-1, -2, -4, -3]) == -1, \
        "maxtal([-1, -2, -4, -3]) ska vara -1"


def test_tom():
    assert funktion.maxtal([]) is None, \
        "maxtal([]) ska vara None"


def test_junk():
    assert funktion.maxtal([1, 2, 3, 'kalle', 0]) is None, \
        "maxtal([1, 2, 3, 'kalle', 0]) ska vara None"


def test_tupel():
    assert funktion.maxtal((1, 2, 4, 3)) == 4, \
        "maxtal( (1,2,4,3) ) ska vara 4"


def test_reversed():
    assert funktion.maxtal(reversed([1, 2, 4, 3])) == 4, \
        "maxtal(reversed([1, 2, 4, 3])) ska vara 4"


if __name__ == '__main__':
    pytest.main(['-vx'])
