import json
from tinkoff_data import TinkoffData
class Stock(TinkoffData):

    def __init__(self): 
        pass

    def __repr__(self) -> str:
        return "class Stock"
    
    def reader(self, figi:str) -> list:   # opening file
        
        with open(f"../data/candles/{figi}.json","r",encoding="utf-8") as file:
            stock = json.load(file)
        return stock['candles']
        
    def count_price_close(self,iteration:int, figi:str) -> float:
        stock = self.reader(figi)
        return float(stock[iteration]["close"]['units']) + float(stock[iteration]["close"]['nano'])/1_000_000_000
        
    def get_points_closing_graphic(self, figi:str) -> list:
        stock = self.reader(figi)
        return sorted([(stock[i]["time"],self.count_price_close(i, figi)) for i in range(len(stock)-1)])
    

if __name__ == "__main__":
    ob = Stock()
    print(ob.reader("TCS109805522"))
    print(ob.get_points_closing_graphic("TCS109805522"))
        



