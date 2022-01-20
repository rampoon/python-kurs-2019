#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys, re, os, inspect
from importlib import import_module

from contextlib import redirect_stdout, redirect_stderr

name = "stack"
klass = "Stack"

mod = import_module(name)


def test_modul():
    assert 'Stack' in dir(mod), \
        klass + " ska finnas i modulen " + name
    assert inspect.isclass(mod.Stack), \
        klass + " ska vara en klass"


def test_konstruktor():
    s = mod.Stack()


def test_push():
    s = mod.Stack()
    s.push(10)


def test_pop():
    s = mod.Stack()
    s.push(10)
    s.push(15)
    assert s.pop() == 15, \
        "pop() ska returnera senaste elementet 15"
    assert s.pop() == 10, \
        "pop() ska returnera senaste elementet 10"


def test_flera_objekt():
    s1 = mod.Stack()
    s1.push("Ella")
    s2 = mod.Stack()
    s2.push("Ulla")
    s1.push("Ylva")
    assert s1.pop() == "Ylva"
    assert s2.pop() == "Ulla"
    assert s1.pop() == "Ella"


def test_tomstack():
    assert "TomStack" in dir(mod), \
        "TomStack ska definieras i modulen " + name
    assert inspect.isclass(mod.TomStack), \
        "TomStack ska vara en klass"
    with pytest.raises(mod.TomStack):
        s = mod.Stack()
        s.pop()
    s = mod.Stack()
    s.push(0)
    s.pop()
    with pytest.raises(mod.TomStack):
        s.pop()


def test_printstack():
    s = mod.Stack()
    s.push("Linus")
    assert len(str(s)) > 0, \
        "det ska gå att skriva ut en " + klass
    assert str(s).find("Linus") >= 0, \
        "utskriften av en " + klass + " ska visa dess innehåll"
