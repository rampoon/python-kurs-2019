#!/usr/bin/python3
# coding: utf-8

"""Övning 4.4

* Öppna en connection till lab04.bredbandskollen.se port 80. Skicka kommandot

    GET /bigfile.bin?len=400 HTTP/1.0\r\n\r\n

  Läs svaret.  (Hur vet man när man läst hela svaret?) Programmet ska skriva ut
  antalet byte ”payload” i svaret (svaret består av en ”header” följt av en
  blankrad följt av det egentliga innehållet, alltså ”payload”).
  Ledning:   header, payload = reply.split('\r\n\r\n')

* Ifall man går via en proxy ska man istället skicka

   GET http://lab04.bredbandskollen.se/bigfile.bin?len=400 HTTP/1.1\r\n
   Host: lab04.bredbandskollen.se\r\n\r\n 

"""

