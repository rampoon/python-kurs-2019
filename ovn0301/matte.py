#!/usr/bin/python3
# coding: utf-8

"""Övning 3.1

* Skapa en ny gren (branch) i Git/BitBucket, t.ex. via menyn VCS i PyCharm.
  Hitta på ett personligt namn åt grenen och pusha upp den till servern.
  Kolla om Jenkins kör testfallen.

* Kör testerna lokalt. Antingen genom att exekvera
  ovn0301/test_matte.py eller genom att köra ett kommandos som
  python3 -m pytest verify.py -vx --tb=line

"""

svar = 4
while True:
    gissning = int(input("What is 2+2: "))
    if gissning == svar:
        break
    print("Wrong!", end=" ")
print("Correct!")
