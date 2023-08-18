import time
import json
import os
import collections
### Tasks ###
# Cоздать столько файлов в количестве отраслей. каждая отрасль в отдельный файл json+
# Cделать commit опубликовать свои изменения на  GitHub+-
# Поиск информации об акциях по наименованию компанию (вхождение строки символов в название)+

# Полностью ориентироваться в структуре данного json Делать поиски и выборки условно любых запросов.+-
# Например, найти самую старую компанию по размещению акций. Выбрать все акции размещенные на бирже в 2010 году+
# Рассчитать популярные страны по юрисдикции торгуемых акций. В какой стране выпущены акции наиболее популярные после РФ+
# Консольное пользовательское меню реализовать с модуляцией диалога (выберите задачу из меню, продолжить/завершить)+

### Notes ###
# Структура файлов проекта (мусор в папках)
# Надо обратить внимание на состав функций (познакомиться с принципами SOLID и структурного программирования)
# Общий синтаксис функций в питоне (параметры и типизация возвращаемых значений)
# Связь логики программы с архитектурой (составом функций и модулей)
# Эффективные алгоритмы поиска, обходов списков и словарей. Генераторы.


#---------------------------------------------------------------------------------------------------------------------------
#основной код
PATH_FILE = "../data/data_stocks.json"
DATE = 2010


#главная функция для тестирования времени выполнения иной функции
def time_measuring(func, *args) -> str:
    print('старт')
    time_start = time.time()
    func(*args)
    time_end = time.time()
    return f" время выполнения =  {time_end - time_start} "
       




# вспомогательная функция для ввода имени компании (вызывается в другой функции)
# ввод имени компании


def fullinfo() -> str:
    stroka = input("введи название интересующей компании ")
    return stroka 


# поиск компаний по заданной строке
def selsect_stocks() -> list:
    # в переменной companies храним название компаний
    companies = []
    stroka = fullinfo()

    stocks = writer(PATH_FILE)

    
    for i in range(len(stocks['instruments'])):
       companies.append( f"{stocks['instruments'][i]['name']}")

    res = []

    for i in range(len(stocks['instruments'])):

        if stroka.lower() in f"{stocks['instruments'][i]['name']}":
            res.append(f"{stocks['instruments'][i]}")        
    return res 





# вспомогательная функция для открытия главного (начального) json 
# открытие json файла

def writer(file_path:str) -> dict:
   
    with open(file_path,"r",encoding="utf-8") as file:
       stocks = json.load(file)
    return stocks 



   
#---------------------------------------------------
# функция для создания папки с файлом по определенному слову
def creating_json() -> str:
    stocks = writer(PATH_FILE)
    search_par = choose_data()
    par = set()
    
    try:
        for i in range(len(stocks['instruments'])):
            par.add(stocks['instruments'][i][search_par])
        os.makedirs(f'../data/{str(search_par)}')
        for i in par:
        
            data =[]
            for j in range(len(stocks['instruments'])):
                if i == stocks['instruments'][j][search_par]:
                    data.append(stocks['instruments'][j])
                
            
            with open(f'../data/{str(search_par)}/'+str(i)+'.json','w',encoding='utf-8') as file:
                main_data ={'main': data}
                json.dump(main_data, file, indent= 4)
        return "success"
    except Exception:
        return "it's impossible to sort by this tag"
    
    
# возвращает строку, являющейся параметром для сортировки json в функции creating_json
def choose_data() -> str:
    stocks = writer(PATH_FILE)
    datas = []

    for i in range(len(stocks['instruments'])):
        datas.extend(tuple(stocks['instruments'][i].keys()))
    datas = set(datas)
    #print (set(datas))
    choose = input(f"Выбери параметр, по которому мы сможем создать и отсортировать json файлы: {datas}")
    if choose in datas:
        return choose
    else:
        return "error"



# рейтинг стран по популярности (акции)
def country_popularity_rating() -> collections:
    stocks = writer(PATH_FILE)
    country_list = [stocks['instruments'][i]['countryOfRiskName'] for i in range(len(stocks['instruments']))]
    result = collections.Counter(country_list)
    return result


# функция для того, чтобы найти акции, появившиеся на бирже в 2010 году 
def companies_by_date(date:int) -> list:
    stocks = writer(PATH_FILE)

    companies_list = []


    for i in range(len(stocks['instruments'])):
        keys = stocks['instruments'][i].keys()
        if 'first1dayCandleDate' in keys and str(date) in stocks['instruments'][i]['first1dayCandleDate']:
            companies_list.append(stocks['instruments'][i])
    return companies_list


# поиск самой старой компании по размещению акций на бирже
def the_oldest_company() -> str:
    stocks = writer(PATH_FILE)


    dates_list = []
    the_company = ''

    for i in range(len(stocks['instruments'])):
        keys = stocks['instruments'][i].keys()
        if 'first1dayCandleDate' in keys:
            dates_list.append(stocks['instruments'][i]['first1dayCandleDate'][:4])
    first_date = min(list(map(int,dates_list)))
    

    for i in range(len(stocks['instruments'])):
        keys = stocks['instruments'][i].keys()
        if 'first1dayCandleDate' in keys:
            if str(first_date) in stocks['instruments'][i]['first1dayCandleDate'][:4]:
                the_company=stocks['instruments'][i]
    return the_company




def main() -> None:
    con = True
    while con:
        num = int(input("""Выберите из предложенного списка доступные возможности(напишите выбранный пукнт, т е цифру): 
            1) поиск компаний по заданной строке
            2) создание папки с файлом по определенному слову
            3) рейтинг стран по популярности (акции)
            4) акции, появившиеся на бирже в опредедлённом году 
            5) поиск самой старой компании по размещению акций на бирже
            """))
        
        if num == 1:
            print(selsect_stocks())
        elif num == 2:
            print(creating_json())
        elif num == 3:
            print(country_popularity_rating())
        elif num == 4:
           print(companies_by_date(DATE)) 
        elif num == 5:
            print(the_oldest_company())
        else:
            print("такого функционала нет")

        con = int(input("продолжаем? (введи 1 если да, 0 - если нет) "))



if __name__ == '__main__':
    main()
    
    

