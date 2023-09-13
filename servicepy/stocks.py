from instruments import Instruments
import collections
import time


class Stocks(Instruments):

    def country_popularity_rating(self) -> collections:  # rate stocks by popularity
        start = time.time()
        country_list = [self.stocks[i]['countryOfRiskName'] for i in range(self.len_stocks)]
        result = collections.Counter(country_list)
        end = time.time()
        return result
    



if __name__ == "__main__":
    stock = Stocks("data/sector/it.json")
    print(stock.country_popularity_rating())