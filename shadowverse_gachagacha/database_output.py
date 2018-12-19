# coding: utf-8

import sqlite3

cont = sqlite3.connect("card_data.db")
c = cont.cursor()
for row in c.execute('SELECT * FROM PackData WHERE series = "Evolved" ORDER BY series'):
    print(row)