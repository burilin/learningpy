from graphic import Graphic
import datetime
from tinkoff_data import TinkoffData
import os
class Signals(Graphic, TinkoffData):
    def __init__(self):
        pass


    def __repr__(self) -> str:
        return "class_signals"
    

    def signal(self, figi) -> str:
        if  os.path.exists(f"../data/candles/{figi}.json"):
            intersections = self.get_intersection(figi)
            if intersections:
                for i in range(len(intersections)):
                    if i == 2:
                        return f" последние два пробоя: {intersections[-1]} \n {intersections[-2]}"
                    else:
                        return intersections
            return "продолжайте удерживать акцию"
        else:
            load = TinkoffData()
            res = load.loader(figi)
            if res == True:
                return self.signal(figi)
            else:
                return "такого фиги нет"

# как я получу сигнал, если у меня есть среднее значение и массив пробоев, но в этом массиве нет данных за сегодняшнюю дату?
# можно делать запрос на сегодня и получать сигнал

if __name__ == "__main__":
    ob = Signals()
    print(ob.signal("TCS007661625"))
    print(ob.signal('BBG000QJW156'))
    #'BBG000QJW156' - санкт петербург