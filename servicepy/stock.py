import json
import os
import datetime
from tinkoff_data import TinkoffData
class Stock(TinkoffData):

    def __init__(self): 
        TinkoffData.__init__(self)

    def __repr__(self) -> str:
        return "class Stock"
    
    def reader(self, figi:str) -> list:   # opening file
        if os.path.exists(f"../data/candles/{figi}.json"):
            with open(f"../data/candles/{figi}.json","r",encoding="utf-8") as file:
                stock = json.load(file)
            return stock["candles"]
        else:
            load = self.loader(figi,date_from=f"{datetime.datetime.now()- datetime.timedelta(days=100)}"[:10])
            if load:
                self.reader(figi)
            return False
        
    def count_price_close(self,iteration:int, figi:str) -> float:
        if self.reader(figi):
            stock = self.reader(figi)
        else:
            return False
        return float(stock[iteration]["close"]['units']) + float(stock[iteration]["close"]['nano'])/1_000_000_000
        
    def get_points_closing_graphic(self, figi:str) -> list:
        if self.reader(figi):
            stock = self.reader(figi)
        else:
            return False
        
        return sorted([(stock[i]["time"],self.count_price_close(i, figi)) for i in range(len(stock))])
    

if __name__ == "__main__":
    ob = Stock()
    #print(ob.reader("TCS007661625"))
    print(ob.get_points_closing_graphic("TCS007661625"))
        



