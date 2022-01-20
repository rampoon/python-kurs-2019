#!/usr/bin/python3
# coding=utf-8

import inspect
import os
import pytest
import sqlite3
import sys

import databas


def create_db(filename):
    try:
        os.unlink(filename)
    except:
        pass
    conn = sqlite3.connect(filename)
    c = conn.cursor()

    c.execute('''
        CREATE TABLE dudes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT)
    ''')

    c.execute('''
        CREATE TABLE scores (
        dude INTEGER,
        score INT,
        FOREIGN KEY(dude) REFERENCES dudes(id))
    ''')

    conn.commit()


def insert_data(filename, dudes, scores):
    conn = sqlite3.connect(filename)
    c = conn.cursor()

    for d, s in zip(dudes, scores):
        c.execute('INSERT INTO dudes (name) VALUES (?)', (d,))
        c.execute('SELECT last_insert_rowid()')
        t = c.fetchone()
        sql = 'INSERT INTO scores (dude, score) VALUES (?, ?)'
        c.execute(sql, (t[0], s))

    conn.commit()


def find_score(filename, name):
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    sql = '''
        SELECT s.score, d.name FROM scores s
        LEFT JOIN dudes d on s.dude=d.id
        WHERE d.name = ?'''
    c.execute(sql, (name,))
    t = c.fetchone()
    return t[0] if t else None

    conn.commit()


def test_tabeller():
    os.chdir(os.path.dirname(__file__))
    filename = "t1.db"
    databas.create(filename)

    sql = '''
        SELECT name FROM sqlite_master 
        WHERE type ='table' AND name NOT LIKE 'sqlite_%'
    '''
    conn = sqlite3.connect(filename)
    c = conn.cursor()
    c.execute(sql)
    assert {t[0] for t in c} == {'scores', 'dudes'}


def test_infoga():
    os.chdir(os.path.dirname(__file__))
    filename = "t2.db"
    databas.create(filename)
    databas.add_dude(filename, 'Bill G', 120)
    databas.add_dude(filename, 'Steve J', 190)
    databas.add_dude(filename, 'Linus T', 330)
    assert find_score(filename, 'Linus T') == 330
    assert find_score(filename, 'Bill') is None


def test_search():
    os.chdir(os.path.dirname(__file__))
    filename = "t2.db"
    databas.create(filename)
    insert_data(filename, ['Bill G', 'Steve J', 'Linus T'],
                [120, 190, 330])
    assert databas.get_score(filename, 'Linus T') == 330
    assert databas.get_score(filename, 'Bill') is None


if __name__ == '__main__':
    pytest.main(["-vx"])
