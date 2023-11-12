import json
import requests
import os
import datetime
from validator import Validator
# жетско зашить токен без передачи self.token_secret либо вынести в конфиг файл+
# убрать stocks_path, добавить массив figi, период (from/ to) в иннит+
# создать loader, путь сохранения+-
# назвать папку файлов свечи +
# вынести в меню+
# ввод данных от пользователя+
# если дата больше двух лет, то разбиваем на несколько запросов+
# stock.py посмотреть задания+
# удалить костыли мерки года+

# упростить дату+
# смотреть есть ли фиги в файле (написать класс валидотор для проверок или в ран пае)+
# создать класс, который будет создавать средние значение массива точек, для определения пробоя снизу и сверху+

ONE_YEAR = datetime.timedelta(365)

date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
class TinkoffData():

    def __init__(self,
                url_post = "https://sandbox-invest-public-api.tinkoff.ru/rest/tinkoff.public.invest.api.contract.v1.MarketDataService/GetCandles"):
        self.url_post = url_post
        self.token = "t.ZDlrOhEC9ykat6XRj1laFX4NLWoI6WgOYp-thfy7ceafgAt16S4hqMqQisDNp1sUceg1-2diDXa2J5dox9i_3Q"
        self.headers = {"Authorization": f"Bearer {self.token}",
                                "accept": "application/json",
                                "Content-Type": "application/json"}

        
    def create_data_json_private(self,figi:str, date_from:str, date_to:str)->list:     #setting data dictionary, depending on figi value
        return {
        "figi": figi, "from": date_from,
        "to": date_to, "interval": "CANDLE_INTERVAL_DAY"}

    def get_data_json(self, data_json: dict)->json:     #requesting to url, getting json using api 
        response = requests.post(self.url_post, headers=self.headers, data=json.dumps(data_json)).json()
        if response['candles']:
            return response['candles']
        raise KeyError

    def check_date_private(self, date_from:str, date_to:str) -> bool:
        try:
            parsed_date_from = datetime.datetime.strptime(date_from, "%Y-%m-%dT%H:%M:%S.%fZ")
            parsed_date_to = datetime.datetime.strptime(date_to, "%Y-%m-%dT%H:%M:%S.%fZ")
            if parsed_date_to - parsed_date_from <= ONE_YEAR:
                return True
            else:
                return False
        except ValueError:
            raise ValueError 

    def separate_date_private(self,figi:str, date_from:str, date_to:str) ->dict:
        dates = []

        parsed_date_from = datetime.datetime.strptime(date_from, "%Y-%m-%dT%H:%M:%S.%fZ")
        parsed_date_to = datetime.datetime.strptime(date_to, "%Y-%m-%dT%H:%M:%S.%fZ")
        while parsed_date_to > parsed_date_from:
            dates.append(parsed_date_from)
            parsed_date_from += ONE_YEAR
            
        dates.append(parsed_date_to)
        dates = [str(datetime.datetime.strftime(i, "%Y-%m-%dT%H:%M:%S.%fZ")) for i in dates]

        data = []
        for i in range(1,len(dates)):
            data.extend(self.get_data_json(self.create_data_json_private(figi, dates[i-1], dates[i])))
        return data


    def loader(self, figi:str = "BBG004730N88", date_from:str = "2022-06-19", date_to:str = f"{datetime.datetime.now()- datetime.timedelta(days=2)}"[:10]) -> bool:
        try:
            date_from += "T00:00:00.263Z"
            date_to += "T00:00:00.263Z"
            val = Validator()
            if val.check_figi(figi) and val.check_data_from(date_from,figi):
                if self.check_date_private(date_from,date_to):
                    try:
                        
                        if not os.path.isdir('../data/candles'):
                            os.makedirs('../data/candles')
                        
                        with open(f'../data/candles/{figi}.json', "w", encoding='utf-8') as file:
                            json.dump({"candles":self.get_data_json(self.create_data_json_private(figi, date_from, date_to))},file,indent=4)
                    except KeyError:
                        return False
                        

                    
                    return True
                else: 
                    data = {"candles":self.separate_date_private(figi, date_from,date_to)}
                    try:
                        
                        if not os.path.isdir('../data/candles'):
                            os.makedirs('../data/candles')
                        
                        with open(f'../data/candles/{figi}.json', "w", encoding='utf-8') as file:
                            json.dump(data,file,indent=4)
                        return True
                    except KeyError:
                        return False
                    
            else:
                return False
        except ValueError:
            return False
   

    def __repr__(self) -> str:
        return "class Tinkoff_Data"
    
if __name__ == "__main__":
    tin = TinkoffData()
    tin_func = tin.loader
    #print(tin.separate_date_private("BBG004730N88","2020-06-19","2022-09-19"))
    print(tin.loader("BBG000QJW156", date_from="2023-09-05"))