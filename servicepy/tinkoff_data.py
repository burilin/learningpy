import json
import requests
import os
import datetime
# жетско зашить токен без передачи self.token_secret либо вынести в конфиг файл+
# убрать stocks_path, добавить массив figi, период (from/ to) в иннит+
# создать loader, путь сохранения+-
# назвать папку файлов свечи +
# вынести в меню+
# ввод данных от пользователя+
# если дата больше двух лет, то разбиваем на несколько запросов+
# stock.py посмотреть задания+
class TinkoffData:

    def __init__(self,
                url_post = "https://sandbox-invest-public-api.tinkoff.ru/rest/tinkoff.public.invest.api.contract.v1.MarketDataService/GetCandles"):
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
        response = requests.post(self.url_post, headers=self.headers, data=json.dumps(data_json)).json()
        if response['candles']:
            return response
        raise KeyError

    def check_date_private(self, date_from:str, date_to:str):
        const_compare_date = datetime.datetime.strptime("2022-09-19T14:41:49.263Z", "%Y-%m-%dT%H:%M:%S.%fZ") - datetime.datetime.strptime("2021-09-19T14:41:49.263Z", "%Y-%m-%dT%H:%M:%S.%fZ")
        try:
            parsed_date_from = datetime.datetime.strptime(date_from, "%Y-%m-%dT%H:%M:%S.%fZ")
            parsed_date_to = datetime.datetime.strptime(date_to, "%Y-%m-%dT%H:%M:%S.%fZ")
            if parsed_date_to - parsed_date_from <= const_compare_date:
                return True
            else:
                return False
        except ValueError:
            raise ValueError 

    def separate_date_private(self,figi,  date_from, date_to):
        dates = []

        const_compare_date = datetime.datetime.strptime("2022-09-19T14:41:49.263Z", "%Y-%m-%dT%H:%M:%S.%fZ") - datetime.datetime.strptime("2021-09-19T14:41:49.263Z", "%Y-%m-%dT%H:%M:%S.%fZ")

        parsed_date_from = datetime.datetime.strptime(date_from, "%Y-%m-%dT%H:%M:%S.%fZ")
        parsed_date_to = datetime.datetime.strptime(date_to, "%Y-%m-%dT%H:%M:%S.%fZ")
        while parsed_date_to > parsed_date_from:
            dates.append(parsed_date_from)
            parsed_date_from += const_compare_date
            
        dates.append(parsed_date_to)
        dates = [ str(datetime.datetime.strftime(i, "%Y-%m-%dT%H:%M:%S.%fZ")) for i in dates]
        print(dates)
        data = []
        for i in range(1,len(dates)):
            data.extend(self.get_data_json(self.create_data_json_private(figi, dates[i-1], dates[i]))['candles'])
        print(data)

        # здесь должно быть продолжение функции

    def loader(self, figi:str = "BBG004730N88", date_from:str = "2022-06-19T14:41:49.263Z", date_to:str = "2022-09-19T14:41:49.263Z") -> bool:
        try:
            if self.check_date_private(date_from,date_to):
                try:
                    
                    if not os.path.isdir('../data/candles'):
                        os.makedirs('../data/candles')
                    
                    with open(f'../data/candles/{figi}.json', "w", encoding='utf-8') as file:
                        json.dump(self.get_data_json(self.create_data_json_private(figi, date_from, date_to)),file,indent=4)
                except KeyError():
                    return False

                
                return True
            else: 
                self.separate_date_private(figi, date_from,date_to)
        except ValueError:
            return False
        

    def __repr__(self) -> str:
        return "class Tinkoff_Data"
    
if __name__ == "__main__":
    tin = TinkoffData()
    tin_func = tin.loader
    assert tin_func("BBG004730N88",  "2021-09-19T14:41:49.263Z","2022-09-19T14:41:49.263Z") == True
    assert tin_func("BBG004730N88",  "2021-09-19T14:41:49.263","2022-09-19T14:41:49.263Z")== False
    assert tin_func("f",  "2021-09-19T14:41:49.263Z","2022-09-19T14:41:49.263Z")== False
    assert tin_func("BBG004730N88",  "f","2022-09-19T14:41:49.263Z")== False
    assert tin_func("BBG004730N88",  "2021-09-19T14:41:49.263Z","f")== False
    assert tin_func("BBG004730N88",  "2021-09-19","2022-09-19T14:41:49.263Z")== False
    assert tin_func("BBG004730N88",  "2021-09-19T14:41:49.263Z","2022-09")== False
    tin.separate_date_private("BBG004730N88","2020-06-19T14:41:49.263Z","2022-09-19T14:41:49.263Z")