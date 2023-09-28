import json
import requests
import os
# жетско зашить токен без передачи self.token_secret либо вынести в конфиг файл+
# убрать stocks_path, добавить массив figi, период (from/ to) в иннит+
# создать loader, путь сохранения+-
# назвать папку файлов свечи +
# вынести в меню+
class TinkoffData:

    def __init__(self,
                url_post = "https://sandbox-invest-public-api.tinkoff.ru/rest/tinkoff.public.invest.api.contract.v1.MarketDataService/GetCandles",
                figi = ["BBG004730N88"],
                date_from = "2022-06-19T14:41:49.263Z",
                date_to = "2022-09-19T14:41:49.263Z"):
        self.figies = figi
        self.date_from = date_from
        self.date_to = date_to
        self.url_post = url_post
        self.token = "t.ZDlrOhEC9ykat6XRj1laFX4NLWoI6WgOYp-thfy7ceafgAt16S4hqMqQisDNp1sUceg1-2diDXa2J5dox9i_3Q"
        self.headers = {"Authorization": f"Bearer {self.token}",
                                "accept": "application/json",
                                "Content-Type": "application/json"}

        
    def create_data_json_private(self,figi:str, date_from:str, date_to:str)->dict:     #setting data dictionary, depending on figi value
        return {
        "figi": figi, "from": date_from,
        "to": date_to, "interval": "CANDLE_INTERVAL_DAY"}

    def get_data_json(self, data_json: dict)->json:     #requesting to url, getting json using api 
        return requests.post(self.url_post, headers=self.headers, data=json.dumps(data_json)).json()
    


    def loader(self) -> str:
        if not os.path.isdir('../data/candles'):
            os.makedirs('../data/candles')
        for figi in self.figies:
            with open(f'../data/candles/{figi}.json', "w", encoding='utf-8') as file:
                json.dump(self.get_data_json(self.create_data_json_private(figi, self.date_from, self.date_to)),file,indent=4)

        
        return "success"

    def __repr__(self) -> str:
        return "class Tinkoff_Data"
    
