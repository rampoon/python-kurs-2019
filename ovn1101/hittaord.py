#!/usr/bin/python3
# coding: utf-8

"""Övning 11.1

* Skapa funktionen allaord som tar ett filnamn som argument.

* Funktionen ska returnera en sträng bestående av alla ord från filen,
  sorterade i svensk bokstavsordning, separerade av blanktecken.
  (Om locale sv_SE.UTF-8 inte är installerad, så sortera istället i
  lexikografisk ordning.)

* Med ”ord” menas här en följd av bokstäver
 (ej kommatecken, siffror, kolon osv.)

* Förutsätt att filen är kodad i utf-8.

* Versaler och gemener ska betraktas som olika.

* Om filen inte kan läsas ska None returneras.

* Om det inte finns några ord i filen ska en tom sträng returneras.

"""

