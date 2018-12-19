# coding: utf-8

import sqlite3
import CPData as cp

dbfile = sqlite3.connect('card_data.db')
c = dbfile.cursor()


sql = 'create table PackData(id int IDENTITY(1,1), series text,reality text,card text, effect_before text,effect_after text);'
c.execute(sql)

for std in cp.CardPack.standard_bronze:
    sql = "insert into PackData(series, reality, card) values(?, ?, ?)"
    data = ("standard", "bronze", std)
    c.execute(sql, data)

for std in cp.CardPack.standard_silver:
    sql = "insert into PackData(series, reality, card) values(?, ?, ?)"
    data = ("standard", "silver", std)
    c.execute(sql, data)

for std in cp.CardPack.standard_gold:
    sql = "insert into PackData(series, reality, card) values(?, ?, ?)"
    data = ("standard", "gold", std)
    c.execute(sql, data)

for std in cp.CardPack.standard_legend:
    sql = "insert into PackData(series, reality, card) values(?, ?, ?)"
    data = ("standard", "legend", std)
    c.execute(sql, data)


for std in cp.CardPack.evolved_bronze:
    sql = "insert into PackData(series, reality, card) values(?, ?, ?)"
    data = ("Evolved", "bronze", std)
    c.execute(sql, data)

for std in cp.CardPack.evolved_silver:
    sql = "insert into PackData(series, reality, card) values(?, ?, ?)"
    data = ("Evolved", "silver", std)
    c.execute(sql, data)

for std in cp.CardPack.evolved_gold:
    sql = "insert into PackData(series, reality, card) values(?, ?, ?)"
    data = ("Evolved", "gold", std)
    c.execute(sql, data)

for std in cp.CardPack.evolved_legend:
    sql = "insert into PackData(series, reality, card) values(?, ?, ?)"
    data = ("Evolved", "legend", std)
    c.execute(sql, data)


for std in cp.CardPack.bahamut_bronze:
    sql = "insert into PackData(series, reality, card) values(?, ?, ?)"
    data = ("Bahamut", "bronze", std)
    c.execute(sql, data)

for std in cp.CardPack.bahamut_silver:
    sql = "insert into PackData(series, reality, card) values(?, ?, ?)"
    data = ("Bahamut", "silver", std)
    c.execute(sql, data)

for std in cp.CardPack.bahamut_gold:
    sql = "insert into PackData(series, reality, card) values(?, ?, ?)"
    data = ("Bahamut", "gold", std)
    c.execute(sql, data)

for std in cp.CardPack.bahamut_legend:
    sql = "insert into PackData(series, reality, card) values(?, ?, ?)"
    data = ("Bahamut", "legend", std)
    c.execute(sql, data)

dbfile.commit()
dbfile.close()
