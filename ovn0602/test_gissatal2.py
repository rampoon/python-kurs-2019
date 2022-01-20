#!/usr/bin/python3
# coding=utf-8

import io, sys, pytest
import re
from importlib import import_module

from contextlib import redirect_stdout

name = "gissatal2"

logfile = open("log.txt", "w")
all_numbers = "\n".join(map(str, range(1, 1001)))


def test_load():
    f = io.StringIO()
    if name in sys.modules: del sys.modules[name]
    with redirect_stdout(f):
        sys.stdin = io.StringIO(all_numbers)
        try:
            import_module(name)
        except EOFError:
            pass


def test_prompt():
    f = io.StringIO()
    with redirect_stdout(f):
        if name in sys.modules: del sys.modules[name]
        sys.stdin = io.StringIO(all_numbers)
        import_module(name)
        assert re.search("1000|1001", f.getvalue()), \
            "ska fråga efter tal mellan 1 och 1000"


def test_play():
    f = io.StringIO()
    with redirect_stdout(f):
        if name in sys.modules: del sys.modules[name]
        user = MockUser(f)
        sys.stdin = user
        import_module(name)

    assert user.check_count(), \
        "antalet gissningar var " + str(user.no_guesses())


def test_badinput():
    f = io.StringIO()
    with redirect_stdout(f):
        if name in sys.modules: del sys.modules[name]
        user = MockUser(f, [1, "ella", 2, "ulla", 4, "ylva"])
        sys.stdin = user
        import_module(name)

    assert user.check_count(), \
        "antalet gissningar var " + str(user.no_guesses())


class MockUser:

    def __init__(self, output, guesses=[]):
        self.count = 0
        self.last_guess = 0
        self.output = output
        self.pos = 0
        self.min = 1
        self.max = 1000
        self.guesses = guesses

    def readline(self):

        if len(self.guesses) > 1 and self.guesses[0] == self.count:
            g = self.guesses[1]
            del self.guesses[0:2]
            logfile.write(str(g))
            return g

        self.count += 1
        if self.count > 12:
            raise EOFError

        s = self.output.getvalue()[self.pos:]

        if self.count == 1:
            self.last_guess = 500
        else:
            if re.search("stor|large|big", s, re.I):
                self.max = self.last_guess - 1
                assert self.max > 0, \
                    "svaret ska vara minst 1"
            elif re.search("lite|little|small", s, re.I):
                self.min = self.last_guess + 1
                assert self.min < 1001, \
                    "svaret ska vara högst 1000"
            else:
                pass
            g = int((self.min + self.max) / 2)
            assert g != self.last_guess, \
                "svaret måste vara ett heltal"
            self.last_guess = g

        self.pos = len(self.output.getvalue())
        logfile.write(s + str(self.last_guess) + "\n")
        return str(self.last_guess)

    def no_guesses(self):
        return self.count

    def check_count(self):
        s = self.output.getvalue()[self.pos:]
        logfile.write(s)
        if re.search(r"\D" + str(self.count) + r"\D", " " + s + " "):
            return True
        else:
            return False


if __name__ == '__main__':
    pytest.main(['-vx'])
