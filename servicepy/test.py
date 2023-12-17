import instruments
import stocks
import stock
import tinkoff_data
import signals
from flask import Flask, render_template, url_for, request, redirect, g
import sqlite3 as sq


# instrument = instruments.Instruments()
# Stocks = stocks.Stocks()
# Stock = stock.Stock()
# tinkoff = tinkoff_data.TinkoffData()
# signal = signals.Signals()
# s = {'figi': 'TCS007661625', 'ticker': 'GAZP', 'classCode': 'SMAL', 'isin': 'RU0007661625', 'lot': 1, 'currency': 'rub', 'shortEnabledFlag': False, 'name': 'Газпром', 'exchange': 'MOEX_PLUS', 'ipoDate': '1998-12-30T00:00:00Z', 'issueSize': '23673512900', 'countryOfRisk': 'RU', 'countryOfRiskName': 'Российская Федерация', 'sector': 'energy', 'issueSizePlan': '23673512900', 'nominal': {'currency': 'rub', 'units': '5', 'nano': 0}, 'tradingStatus': 'SECURITY_TRADING_STATUS_NORMAL_TRADING', 'otcFlag': False, 'buyAvailableFlag': True, 'sellAvailableFlag': True, 'divYieldFlag': True, 'shareType': 'SHARE_TYPE_COMMON', 'minPriceIncrement': {'units': '0', 'nano': 10000000}, 'apiTradeAvailableFlag': False, 'uid': '9100df58-0e92-48ec-b962-4e788e6b61fd', 'realExchange': 'REAL_EXCHANGE_MOEX', 'positionUid': '4f9d0c81-cdf9-4735-8295-bacbfa3b8a51', 'forIisFlag': True, 'forQualInvestorFlag': False, 'weekendFlag': True, 'blockedTcaFlag': False, 'liquidityFlag': True, 'first1minCandleDate': '2018-03-08T04:23:00Z', 'first1dayCandleDate': '2018-03-13T07:00:00Z'}
# import json
# import ast

# list = "['search_key', 'search_value']"
# list = ast.literal_eval(list)
# print(list[1])

import uuid
dp_path = "db/quots.db"

db = sq.connect(dp_path)
cur = db.cursor()

cur.execute("DROP TABLE IF EXISTS quots;")
cur.execute ('DROP TABLE IF EXISTS stocks;')
cur.execute ('CREATE TABLE stocks (uuid uuid PRIMARY KEY NOT NULL, figi TEXT, name TEXT);')
cur.execute ('CREATE TABLE quots (uuid uuid PRIMARY KEY NOT NULL , time TEXT, price DECIMAL, uuid_stocks uuid REFERENCES  stocks(uuid) ON DELETE CASCADE);')
cur.execute ('SELECT * FROM quots q INNER JOIN stocks s ON q.uuid_stocks = s.uuid;')

cur.execute('INSERT INTO stocks (uuid, figi, name) VALUES("9ea8f9d5-bda9-4dc1-aacc-4a03f6cb17f0","TCS032", "Роснефть" );')
cur.execute('INSERT INTO stocks (uuid, figi, name) VALUES("ca9262e2-0429-4561-9b80-7d3734ba5822","BBG00321", "Газпром" );')
db.commit()
db.close()
