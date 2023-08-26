import time
import json
import os
import collections

class Stocks:

    def __init__(self, FILE_PATH = "../data/data_stocks.json" , DATE = 2010, SEARCH_KEY = "ticker", SEARCH_VALUE = "SBERP") -> None:
        self.file_path = FILE_PATH
        self.date = DATE
        self.search_key = SEARCH_KEY
        self.search_value = SEARCH_VALUE


    def __repr__(self) -> str:
        return 'stocks'


    def writer(self) -> list:   # opening file

        with open(self.file_path,"r",encoding="utf-8") as file:
            stocks = json.load(file)
        return stocks['instruments'] 
    


    def main(self,*args) -> str:   # func main to choose other funcs
    
        tasks = {
            1: self.select_stocks,
            2: self.creating_json,
            3: self.country_popularity_rating,
            4: self.companies_by_date,
            5: self.the_oldest_company,
            6: self.select_stocks2
        }


        task = int(input(f"выбери функцию {tasks} "))

        return tasks[task](*args)
    


    def get_str(self) -> str:   # return a string, which is a name of the company
        stroka = input("введи название интересующей компании ")
        return stroka 


    
    def select_stocks(self, stocks:list, stroka:str ) -> list: # slow select stocks by string(name)
        
        companies = []
        
        for i in range(len(stocks)):
            companies.append( f"{stocks[i]['name']}")

        res = []

        for i in range(len(stocks)):

            if stroka.lower() in f"{stocks[i]['name']}":
                res.append(f"{stocks[i]}")        
        return res 
    


    def sort_list_dict(self, list_dict:list, search_key: str) -> list:  # quick sorting
        
        if len(list_dict) <=1:
            return list_dict
        base_elem = list_dict[0]

        left = [elem for elem in list_dict[0:] if elem[search_key] < base_elem[search_key]]
        center = [i for i in list_dict if i[search_key] == base_elem[search_key]]
        right = [elem for elem in list_dict[0:] if elem[search_key] > base_elem[search_key]]
        return self.sort_list_dict(left, search_key) + center + self.sort_list_dict(right, search_key)



    def select_stocks2(self, list_dict:list, search_key:str, search_value:str) -> list: # binary search by the key and its value
        list_dict = self.sort_list_dict(list_dict,search_key)



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
    
    def creating_json(self, stocks:list, search_par:str) -> str:    #creating json using searching par

        par = set()
        
        try:
            for i in range(len(stocks)):
                par.add(stocks[i][search_par])
            os.makedirs(f'../data/{str(search_par)}')
            for i in par:
            
                data =[]
                for j in range(len(stocks)):
                    if i == stocks[j][search_par]:
                        data.append(stocks[j])
                    
                
                with open(f'../data/{str(search_par)}/'+str(i)+'.json','w',encoding='utf-8') as file:
                    main_data ={'main': data}
                    json.dump(main_data, file, indent= 4)
            return "success"
        except Exception:
            return "it's impossible to sort by this tag"
        
        
    def country_popularity_rating(self, stocks:list) -> collections:  # rate stocks by popularity
        country_list = [stocks[i]['countryOfRiskName'] for i in range(len(stocks))]
        result = collections.Counter(country_list)
        return result
    

    def companies_by_date(self, year:int, stocks:list) -> list: # searching companies by year
        companies_list = []


        for i in range(len(stocks)):
            keys = stocks[i].keys()
            if 'first1dayCandleDate' in keys and str(year) in stocks[i]['first1dayCandleDate']:
                companies_list.append(stocks[i])
        if companies_list:
            return companies_list
        return "not found"
    
    def the_oldest_company(self, stocks:list) -> str: #searching the oldest company
        dates_list = []
        the_company = ''

        for i in range(len(stocks)):
            keys = stocks[i].keys()
            if 'first1dayCandleDate' in keys:
                dates_list.append(stocks[i]['first1dayCandleDate'][:4])
        first_date = min(list(map(int,dates_list)))
        

        for i in range(len(stocks)):
            keys = stocks[i].keys()
            if 'first1dayCandleDate' in keys:
                if str(first_date) in stocks[i]['first1dayCandleDate'][:4]:
                    the_company=stocks[i]
        return the_company
    
    def time_measuring(func, *args) -> str: #measuring funcs' time
        print('старт')
        time_start = time.time()
        func(*args)
        time_end = time.time()
        return f" время выполнения =  {time_end - time_start} "

    

stock = Stocks()

print(stock.main())