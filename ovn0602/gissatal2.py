#!/usr/bin/python3
# coding: utf-8

"""Övning 6.2

* Som i övning 3.3, men lägg till felhantering så att programmet inte kraschar
  ifall man råkar mata in något som inte är ett heltal. (Gissningar som inte är
  heltal ska inte räknas in i det totala antalet gissningar som skrivs ut i
  slutet, se exempel nedan.)

    $ python3 gissatal.py
    Gissa tal (1-1000): 500
    För stort! Gissa tal (1-1000): g300
    inget heltal, försök igen
    Gissa tal (1-1000): 300
    För stort
    Gissa tal (1-1000): 100
    För litet
    Gissa tal (1-1000): 213
    OK efter 4 gissningar.
    $

"""

