import json
import os
import collections
#создать экземпляр класса, чтобы проверить creating json
class Stocks:

    def __init__(self, file_path = "../data/data_stocks.json" , search_key = "ticker", search_value = "SBERP"):
        self.file_path = file_path
        self.search_key = search_key
        self.search_value = search_value
        self.stocks = self.writer()
        self.len_stocks = len(self.stocks)

    def __repr__(self) -> str:
        return str("self.stocks_list_dict")
    

    def writer(self) -> list:   # opening file

        with open(self.file_path,"r",encoding="utf-8") as file:
            stocks = json.load(file)
        return stocks['instruments'] 
    
    
    def select_stocks(self, string:str ) -> list: # slow select stocks by string(name)
        
        companies = []
        
        for i in range(self.len_stocks):
            companies.append( f"{self.stocks[i]['name']}")

        res = []

        for i in range(self.len_stocks):

            if string.lower() in f"{self.stocks[i]['name']}":
                res.append(f"{self.stocks[i]}")        
        return res 
    


    def sort_list_dict(self, stocks:list) -> list:  # quick sorting
        if len(stocks) <=1:
            return stocks
        base_elem = stocks[0]

        left = [elem for elem in stocks if elem[self.search_key] < base_elem[self.search_key]]
        center = [i for i in stocks if i[self.search_key] == base_elem[self.search_key]]
        right = [elem for elem in stocks if elem[self.search_key] > base_elem[self.search_key]]
        return self.sort_list_dict(left) + center + self.sort_list_dict(right)



    def select_stocks2(self) -> list: # binary search by the key and its value
        list_dict = self.sort_list_dict()



        left,right = 0, len(list_dict) - 1

        while left<=right:
            mid = (left+right)//2

            if list_dict[mid][self.search_key] == self.search_value:
                return list_dict[mid]
            if list_dict[mid][self.search_key] > self.search_value:
                right = mid - 1
            if list_dict[mid][self.search_key] < self.search_value:
                left = mid + 1
        return "not found"
    
    def creating_json(self, search_par:str) -> str:    #creating json using searching par

        par = set()
        
        try:
            for i in range(self.len_stocks):
                par.add(self.stocks[i][search_par])
            os.makedirs(f'../data/{str(search_par)}')
            for i in par:
            
                data =[]
                for j in range(self.len_stocks):
                    if i == self.stocks[j][search_par]:
                        data.append(self.stocks[j])
                    
                
                with open(f'../data/{str(search_par)}/'+str(i)+'.json','w',encoding='utf-8') as file:
                    main_data ={'main': data}
                    json.dump(main_data, file, indent= 4)
            return "success"
        except Exception:
            return "it's impossible to sort by this tag"
        
        
    def country_popularity_rating(self) -> collections:  # rate stocks by popularity
        country_list = [self.stocks[i]['countryOfRiskName'] for i in range(self.len_stocks)]
        result = collections.Counter(country_list)
        return result
    

    def companies_by_date(self, year:int) -> list: # searching companies by year
        companies_list = []


        for i in range(self.len_stocks):
            keys = self.stocks[i].keys()
            if 'first1dayCandleDate' in keys and str(year) in self.stocks[i]['first1dayCandleDate']:
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

