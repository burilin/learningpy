import json
from instruments import Instruments

class Stock(Instruments):

    def __init__(self,file_path="../data/BBG004730N88_candles_day_stock.json"):
        self.file_path = file_path
        self.stock = self.reader()

    def __repr__(self) -> str:
        return "class Stock"
    
    def reader(self) -> list:   # opening file

        with open(self.file_path,"r",encoding="utf-8") as file:
            stock = json.load(file)
        return stock['candles'] 
    
    def count_price_close(self,iteration:int) -> float:
        return float(self.stock[iteration]["close"]['units']) + float(self.stock[iteration]["close"]['nano'])/1_000_000_000
        
    def get_points_closing_graphic(self) -> list:
        return[(self.count_price_close(i),self.stock[i]["time"]) for i in range(len(self.stock)-1)]
        



