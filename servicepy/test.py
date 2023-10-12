import json
import requests
import datetime
# url_post = "https://sandbox-invest-public-api.tinkoff.ru/rest/tinkoff.public.invest.api.contract.v1.MarketDataService/GetCandles"

# token = "t.ZDlrOhEC9ykat6XRj1laFX4NLWoI6WgOYp-thfy7ceafgAt16S4hqMqQisDNp1sUceg1-2diDXa2J5dox9i_3Q"
# headers = {"Authorization": "Bearer {}".format(token),
#                    "accept": "application/json",
#                    "Content-Type": "application/json"}
# data_json = {
#   "figi": "BBG004730N88",
#   "from": "2021-09-19T14:41:49.263000Z",
#   "to": "2022-09-19T14:41:49.263000Z",
#   "interval": "CANDLE_INTERVAL_DAY"

# }

# resp = requests.post(url_post, headers=headers, data=json.dumps(data_json))
# fromm = datetime.datetime.strptime("2021-09-19T14:41:49.263Z", "%Y-%m-%dT%H:%M:%S.%fZ")
# to = datetime.datetime.strptime("2024-06-19T14:41:49.263Z", "%Y-%m-%dT%H:%M:%S.%fZ")
# print((to - fromm)//3)


# d = datetime.datetime.strptime("2021-09-19T14:41:49.263Z", "%Y-%m-%dT%H:%M:%S.%fZ")
# print(str(d)[:-3])
# d1=datetime.datetime.strftime(str(d), "%Y-%m-%dT%H:%M:%S.%fZ")
# print(d1)

