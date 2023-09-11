import json
import os
import collections
# создать экземпляр класса, чтобы проверить creating json, изменив структуру создания json+
# переименовать класс Stocks в Instruments+ 
# переименовать writer в reader +
# file_path_out/ file_path_in-
# передать как параметры поиска search_key, value+

class Instruments:

    def __init__(self, file_path = "../data/data_stocks.json" ):
        self.file_path = file_path
        self.stocks = self.reader()
        self.len_stocks = len(self.stocks)

    def __repr__(self) -> str:
        return str("self.stocks_list_dict")
    

    def reader(self) -> list:   # opening file

        with open(self.file_path,"r",encoding="utf-8") as file:
            stocks = json.load(file)
        return stocks['instruments'] 
    
    
    def select_stocks(self, search_key:str ,search_value:str ) -> list: # slow select stocks by string(name)
        try:
    
            res = []

            for i in range(self.len_stocks):

                if search_value.lower() in f"{self.stocks[i][search_key].lower()}":
                    res.append(f"{self.stocks[i]}")        
            return res 
        except Exception as ex:
            return f'Error. {ex}.'
    


    def sort_list_dict(self, stocks:list, search_key:str ) -> list:  # quick sorting
        if len(stocks) <=1:
            return stocks
        base_elem = stocks[0]

        left = [elem for elem in stocks if elem[search_key] < base_elem[search_key]]  
        center = [i for i in stocks if i[search_key] == base_elem[search_key]]
        right = [elem for elem in stocks if elem[search_key] > base_elem[search_key]]
        return self.sort_list_dict(left, search_key) + center + self.sort_list_dict(right, search_key)
    

    def sort_list_dict_public(self, search_key):
        copy_stocks = self.stocks
        result = self.sort_list_dict(copy_stocks, search_key)
        return result


    def select_stocks2(self, search_key:str, search_value:str) -> list: # binary search by the key and its value
        list_dict = self.sort_list_dict_public(search_key)



        left,right = 0, len(list_dict) - 1

        while left<=right:
            mid = (left+right)//2

            if list_dict[mid][search_key] == search_value:
                return list_dict[mid]
            if list_dict[mid][search_key] > search_value:
                right = mid - 1
            if list_dict[mid][search_key] < search_value:
                left = mid + 1
        return "not found"
    
    def writer(self, search_par:str, name_key:str, data:list):
        with open(f'../data/{str(search_par)}/'+str(name_key)+'.json','w',encoding='utf-8') as file:
            main_data ={'instruments': data}
            json.dump(main_data, file, indent= 4)
    
    def json_creater(self, search_par:str) -> str:    #creating json using searching par

        params = set()
        
        try:
            for i in range(self.len_stocks):
                params.add(self.stocks[i][search_par])
            os.makedirs(f'../data/{str(search_par)}')
            for i in params:
            
                data =[]
                for j in range(self.len_stocks):
                    if i == self.stocks[j][search_par]:
                        data.append(self.stocks[j])
                    
                self.writer(search_par=search_par,name_key=i,data=data)
            return "success"
        except Exception as ex:
            return f"it's impossible to write and sort by this tag\n Exceprion : {ex}"
        
        
    def country_popularity_rating(self) -> collections:  # rate stocks by popularity
        country_list = [self.stocks[i]['countryOfRiskName'] for i in range(self.len_stocks)]
        result = collections.Counter(country_list)
        return result
    

    def companies_by_date(self, year:str) -> list: # searching companies by year
        companies_list = []


        for i in range(self.len_stocks):
            keys = self.stocks[i].keys()
            if 'first1dayCandleDate' in keys and year in self.stocks[i]['first1dayCandleDate']:
                companies_list.append(self.stocks[i])
        if companies_list:
            return companies_list
        return "not found"
    
    def the_oldest_company(self) -> str: #searching the oldest company
        dates_list = []
        the_company = ''

        for i in range(self.len_stocks):
            keys = self.stocks[i].keys()
            if 'first1dayCandleDate' in keys:
                dates_list.append(self.stocks[i]['first1dayCandleDate'][:4])
        first_date = min(list(map(int,dates_list)))
        

        for i in range(self.len_stocks):
            keys = self.stocks[i].keys()
            if 'first1dayCandleDate' in keys:
                if str(first_date) in self.stocks[i]['first1dayCandleDate'][:4]:
                    the_company=self.stocks[i]
        return the_company

