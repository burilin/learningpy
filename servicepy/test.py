import instruments
import stocks
import stock
import tinkoff_data
import signals
from flask import Flask, render_template, url_for, request, redirect, g



# instrument = instruments.Instruments()
# Stocks = stocks.Stocks()
# Stock = stock.Stock()
# tinkoff = tinkoff_data.TinkoffData()
# signal = signals.Signals()
# s = {'figi': 'TCS007661625', 'ticker': 'GAZP', 'classCode': 'SMAL', 'isin': 'RU0007661625', 'lot': 1, 'currency': 'rub', 'shortEnabledFlag': False, 'name': 'Газпром', 'exchange': 'MOEX_PLUS', 'ipoDate': '1998-12-30T00:00:00Z', 'issueSize': '23673512900', 'countryOfRisk': 'RU', 'countryOfRiskName': 'Российская Федерация', 'sector': 'energy', 'issueSizePlan': '23673512900', 'nominal': {'currency': 'rub', 'units': '5', 'nano': 0}, 'tradingStatus': 'SECURITY_TRADING_STATUS_NORMAL_TRADING', 'otcFlag': False, 'buyAvailableFlag': True, 'sellAvailableFlag': True, 'divYieldFlag': True, 'shareType': 'SHARE_TYPE_COMMON', 'minPriceIncrement': {'units': '0', 'nano': 10000000}, 'apiTradeAvailableFlag': False, 'uid': '9100df58-0e92-48ec-b962-4e788e6b61fd', 'realExchange': 'REAL_EXCHANGE_MOEX', 'positionUid': '4f9d0c81-cdf9-4735-8295-bacbfa3b8a51', 'forIisFlag': True, 'forQualInvestorFlag': False, 'weekendFlag': True, 'blockedTcaFlag': False, 'liquidityFlag': True, 'first1minCandleDate': '2018-03-08T04:23:00Z', 'first1dayCandleDate': '2018-03-13T07:00:00Z'}
import json
import ast

list = "['search_key', 'search_value']"
list = ast.literal_eval(list)
print(list[1])