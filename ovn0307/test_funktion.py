#!/usr/bin/python3
# coding=utf-8

import pytest
import sys, inspect

import funktion


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


if __name__ == '__main__':
    pytest.main(['-vx'])
