#!/usr/bin/python3
# coding=utf-8

import pytest
import io, sys
from importlib import import_module

from contextlib import redirect_stdout

name = "matte"


def test_load():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]
    with redirect_stdout(f):
        sys.stdin = io.StringIO("")
        try:
            import_module(name)
        except EOFError:
            pass


def test_prompt():
    f = io.StringIO()
    with redirect_stdout(f):
        if name in sys.modules: del sys.modules[name]
        sys.stdin = io.StringIO("4\r\n")
        import_module(name)
        prompt = "What is 2+2: "
        assert f.getvalue()[0:len(prompt)] == prompt, \
            "Got " + f.getvalue() + ", expected " + prompt


def test_first_guess():
    f = io.StringIO()
    with redirect_stdout(f):
        if name in sys.modules: del sys.modules[name]
        sys.stdin = io.StringIO("4\r\n")
        import_module(name)
        assert f.getvalue() == "What is 2+2: Correct!\n", \
            "Wrong output: " + f.getvalue()


def test_second_guess():
    f = io.StringIO()
    with redirect_stdout(f):
        if name in sys.modules: del sys.modules[name]
        sys.stdin = io.StringIO("5\r\n4\r\n")
        import_module(name)
        out = "What is 2+2: Wrong! What is 2+2: Correct!\n"
        assert f.getvalue() == out, \
            "Wrong output: " + f.getvalue()


if __name__ == '__main__':
    import pytest
    pytest.main(["-vx"])
