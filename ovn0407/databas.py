#!/usr/bin/python3
# coding: utf-8

"""Övning 4.7

* Skapa funktionen create som tar en sträng (ett filnamn) som parameter.  Om filen finns, så ska den raderas.  Sedan ska en SQLite-databas skapas med tabellerna dudes och scores enligt nedan i den filen:


      CREATE TABLE dudes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT)

      CREATE TABLE scores (
        dude INTEGER,
        score INT,
        FOREIGN KEY(dude) REFERENCES dudes(id))

* Skapa funktionen add_dude som tar tre parametrar:
   - filnamn till SQLite-databasen
   - en sträng som ger ett namn på en person (t.ex. ”Steve”)
   - ett heltal som ger en poäng (t.ex. 19)
  Funktionen ska lägga in namnet i tabellen dudes och poängen (med referens
  till namnet i dudes) i tabellen scores.

* Skapa funktionen get_score som tar två strängar som parametrar.
  Den första parametern ska vara ett filnamnet till SQLite-databasen och den
  andra ska vara ett namn, t.ex. ”Steve”.
  Funktionen ska returnera poängen som personen med det namnet fick.
  Om personen inte fanns i databasen ska None returneras.

"""

