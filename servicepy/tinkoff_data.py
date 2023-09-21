import json
import requests
import os

class Tinkoff_Data:

    def __init__(self,
                url_post = "https://sandbox-invest-public-api.tinkoff.ru/rest/tinkoff.public.invest.api.contract.v1.MarketDataService/GetCandles",
                token = "t.ZDlrOhEC9ykat6XRj1laFX4NLWoI6WgOYp-thfy7ceafgAt16S4hqMqQisDNp1sUceg1-2diDXa2J5dox9i_3Q",
                stocks_path = "../data/data_stocks.json"):
        self.url_post = url_post
        self.token = token
        self.stocks_path = stocks_path
        self.stocks = self.reader() # file data_stocks.json
        self.headers = {"Authorization": f"Bearer {token}",
                                "accept": "application/json",
                                "Content-Type": "application/json"}
    def get_figies_private(self) -> object:   #getting figies
        return [i["figi"] for i in self.stocks]
        
    def set_data_json(self,figi:str)->dict:     #setting data dictionary, depending on figi value
        return {
        "figi": figi, "from": "2022-06-19T14:41:49.263Z",
        "to": "2022-09-19T14:41:49.263Z", "interval": "CANDLE_INTERVAL_DAY"}

    def get_data_json(self, data_json: dict)->json:     #requesting to url, getting json using api 
        return requests.post(self.url_post, headers=self.headers, data=json.dumps(data_json)).json()
    
    def reader(self) -> list:   # opening file

        with open(self.stocks_path,"r",encoding="utf-8") as file:
            stocks = json.load(file)
        return stocks['instruments'] 

    def writer(self) -> str:
        try:
            os.makedirs('../data/figies_datas')
            for figi in self.get_figies_private():
                with open(f'../data/figies_datas/{figi}.json', "w", encoding='utf-8'):
                    self.get_data_json(self.set_data_json(figi))
        except Exception:
            return Exception
        
        return "success"

    def __repr__(self) -> str:
        return "class Tinkoff_Data"
    
tin = Tinkoff_Data()
print(tin.writer())
