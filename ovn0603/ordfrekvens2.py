#!/usr/bin/python3
# coding: utf-8

"""Övning 6.3

* Lägg till felhantering i övning 5.6 så att programmet inte kraschar, utan ger
  vettiga felmeddelanden till stderr och sedan avslutar med SystemExit, ifall:
    - filen inte går att öppna, eller
    - filen inte är kodad i utf-8.
  Exempel:
    $ python3 ordfrekvens.py finns.ej
    Kan inte öppna filen
    $ python3 ordfrekvens.py /usr/bin/python3
    Filen är inte i utf-8
    $

"""

