import datetime
import json


### Tasks ###
# Cоздать столько файлов в количестве отраслей. каждая отрасль в отдельный файл json
# Cделать commit опубликовать свои изменения на  GitHub
# Поиск информации об акциях по наименованию компанию (вхождение строки символов в название)

# Полностью ориентироваться в структуре данного json Делать поиски и выборки условно любых запросов.
# Например, найти самую старую компанию по размещению акций. Выбрать все акции размещенные на бирже в 2010 году
# Рассчитать популярные страны по юрисдикции торгуемых акций. В какой стране выпущены акции наиболее популярные после РФ
# Консольное пользовательское меню реализовать с модуляцией диалога (выберите задачу из меню, продолжить/завершить)

### Notes ###
# Структура файлов проекта (мусор в папках)
# Надо обратить внимание на состав функций (познакомиться с принципами SOLID и структурного программирования)
# Общий синтаксис функций в питоне (параметры и типизация возвращаемых значений)
# Связь логики программы с архитектурой (составом функций и модулей)
# Эффективные алгоритмы поиска, обходов списков и словарей. Генераторы.

def main():

    print('!run.py!')
    

# ввод имени компании
def fullinfo():
    stroka = input("введи название интересующей компании ")
    return stroka 

# поиск компаний по заданной строке
def selsect_stocks():
    # в переменной companies храним название компаний
    companies = []
    stroka = fullinfo()
    stocks = writer()
    
    for i in range(len(stocks['instruments'])):
       companies.append( f"{stocks['instruments'][i]['name']}")

    res = []

    for i in range(len(stocks['instruments'])):
        if stroka in f"{stocks['instruments'][i]['name']}":
            res.append(f"{stocks['instruments'][i]}")        
    return res 

# открытие json файла
def writer():
   
    with open("../data/data_stocks.json","r",encoding="utf-8") as file:
       stocks = json.load(file)
    return stocks 

# вывод 
def output():
    out = selsect_stocks()
    if out:
        for i in out:
            print(f"{i}\n\n")
    else:
        print("такой компании нет")

   

def creating_json():
    stocks = writer()

    sectors = set()

    for i in range(len(stocks['instruments'])):
        sectors.add(stocks['instruments'][i]["sector"])
    
    for i in sectors:
    
        data =[]
        for j in range(len(stocks['instruments'])):
            if i == stocks['instruments'][j]["sector"]:
                data.append(stocks['instruments'][j])
            

        with open(i+'.json','w') as file:
            main_data ={'main': data}
            json.dump(main_data, file, indent= 4)
    
    








if __name__ == '__main__':
    #output()
    creating_json()

