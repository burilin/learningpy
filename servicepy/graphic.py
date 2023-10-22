import stock
# заменить бин поиск на for из-за несправедливости
# класс сигнал
class Graphic(stock.Stock):
    def __init__(self):
        pass

    def __repr__(self) -> str:
        return "class graphic"
    

    def get_middle_price(self,figi:str) -> float:
        self.points = self.get_points_closing_graphic(figi)
        return sum([i[1] for i in self.points])/len(self.points)
        
    def get_intersection(self, figi:str) -> list:
        results = []
        middle = self.get_middle_price(figi)
        for i in range(1,len(self.points)):
            if self.points[i-1][1] < middle < self.points[i][1]:
                results.append({"пробой в":self.points[i], "рекомендация": "покупка акции(пробой снизу)"})

            if self.points[i-1][1] > middle > self.points[i][1]:
                results.append({"пробой в":self.points[i], "рекомендация": "продажа акции(пробой сверху)"})
        return results


if __name__ == "__main__":
    ob = Graphic()
    print(ob.get_middle_price("BBG000QJW156"))#4605.257142857143
    print(ob.get_intersection("BBG000QJW156"))
    print(ob.get_middle_price("TCS109029540"))#265
    print(ob.get_intersection("TCS109029540"))
    
    
    