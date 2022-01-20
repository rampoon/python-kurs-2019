#!/usr/bin/python3
# coding: utf-8

"""Övning 12.1

* Skriv en funktion med namnet maxtal som tar en lista av tal som parameter
  och returnerar det största talet i listan.
  T.ex. ska maxtal([13, 5, 23, 8]) returnera 23.

* Om listan är tom ska funktionen returnera None.

* Om listan innehåller något som inte är int eller float, så ska funktionen
  returnera None.

* Det ska gå att anropa med en tupel eller range, inte enbart en lista.

* Det ska gå att anropa med en godtycklig sekvens (”lazy evaluation”),
  t.ex. maxtal(reversed([5, 55, -5])).

* Skriv ett antal testfall med pytest för funktionaliteten ovan.

"""

# Klistra in funktionen här


# Lägg till testfall här


if __name__ == '__main__':
    import pytest
    pytest.main([__file__, "-vx"])
