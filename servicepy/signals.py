from graphic import Graphic
import datetime
from tinkoff_data import TinkoffData
import os
class Signals(Graphic, TinkoffData):
    def __init__(self):
        self.time = str(datetime.datetime.now())[:10]
        self.back_time = str(datetime.datetime.now() - datetime.timedelta(days=2))[:10]

    def __repr__(self) -> str:
        return "class_signals"
    
    def signal(self, figi) -> str:
        if  os.path.exists(f"../data/candles/{figi}.json"):
            self.middle = self.get_middle_price(figi)
            load = self.loader(figi, self.back_time, self.time)
            if load:
                intersections = self.get_intersection(figi)
                for i in range(len(intersections)):
                    if intersections[i]["пробой в"][0][:10] == self.time:
                        return intersections[i]["рекомендация"]
            return "пробоя нет"
        else:
            return "для начала загрузите файл с данным figi"
            

# как я получу сигнал, если у меня есть среднее значение и массив пробоев, но в этом массиве нет данных за сегодняшнюю дату?
# можно делать запрос на сегодня и получать сигнал

if __name__ == "__main__":
    ob = Signals()
    print(ob.signal("TCS109805522"))
    print(ob.signal("TCS109029540"))