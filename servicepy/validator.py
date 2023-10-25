import json
class Validator:

    def __init__(self):
        self.main_file_name = "../data/data_stocks.json"
        
    def __repr__(self) -> str:
        return "class validator"
    
    def check_figi(self, figi:str) -> bool:
        

        with open(self.main_file_name,"r",encoding="utf-8") as file:
            stocks = json.load(file)['instruments']
    
        for i in range(len(stocks)-1):
            if stocks[i]['figi'] == figi:
                return True
            
        return False


    def check_data_from(self,date_from, figi):
        with open(self.main_file_name,"r",encoding="utf-8") as file:
            stocks = json.load(file)['instruments']
    
        for i in range(len(stocks)-1):
            if stocks[i]['figi'] == figi and  stocks[i]["first1dayCandleDate"]<date_from:
                return True
            
        return False
if __name__ == "__main__":
    val = Validator()
    print(val.check_figi("fdfsd"))