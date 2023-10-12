import stock

class Graphic(stock.Stock):
    def __init__(self):
        pass

    def __repr__(self) -> str:
        return "class graphic"
    

    def get_middle_price(self,figi:str) -> float:
        points = self.get_points_closing_graphic(figi)
        return sum([i[1] for i in points])/len(points)
        
    def get_intersection(self, figi:str):
        middle = self.get_middle_price(figi)
        price_points = self.get_points_closing_graphic_reversed(figi)


        left, right = 0, len(price_points) - 1
        while left<=right:
            mid = (left+right)//2
            if price_points[mid] < middle < price_points[mid+1]:
                return "пробой снизу"
            elif price_points[mid] > middle > price_points[mid+1]:
                return "пробой сверху"
            elif price_points[mid+1] < middle:
                left = mid+1
            elif price_points[mid+1] > middle:
                right = mid-1

        return False



    

if __name__ == "__main__":
    ob = Graphic()
    print(ob.get_intersection("BBG004730N88"))
    
    