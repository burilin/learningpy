from instruments import Instruments
import collections
class Stocks(Instruments):

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
    



# if __name__ == "__main__":
#     stock = Stocks("../data/sector/it.json")
#     print(stock.country_popularity_rating())