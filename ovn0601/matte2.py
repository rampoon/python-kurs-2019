#!/usr/bin/python3
# coding: utf-8

"""Övning 6.1

* Lägg till felhantering i programmet nedan så att det inte kraschar utan
  bara frågar igen ifall man råkar mata in något som inte är ett heltal.
  Ifall det inte går att läsa mer från stdin, så ska programmet avslutas
  (dvs. EOFError ska inte fångas, bara ValueError).
  Exempel:

    What is 2+2: vet ej
    What is 2+2: 5
    Wrong! What is 2+2: 4
    Correct!

"""

svar = 4
while True:
    gissning = int(input("What is 2+2: "))
    if gissning == svar:
        break
    print("Wrong!", end=" ")
print("Correct!")
