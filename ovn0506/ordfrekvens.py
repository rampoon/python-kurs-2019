#!/usr/bin/python3
# coding: utf-8

"""Övning 5.6

* Skriv ett program som läser in en textfil och beräknar antalet förekomster
  av varje ”ord” i filen. Utskriften ska vara sorterad så att de mest frekventa
  orden anges först. Namnet på filen ska tas som en kommandoradsparameter.
  Versaler och gemener ska betraktas som olika.
  Förutsätt att filen använder utf-8 som teckenkodning.

  Exempel: om filen innehåller

    Ett och två, tre
    och tre och fyra.

  ska utskriften bli

    och 3
    tre 2
    Ett 1
    två, 1
    fyra. 1

"""

