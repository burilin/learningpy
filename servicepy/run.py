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
NAME_KEY = "ticker"
SEARCH_VALUE = "SBERP"
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
def select_stocks(stocks:dict,stroka:str ) -> list:
    # в переменной companies храним название компаний
    companies = []
    
    for i in range(len(stocks['instruments'])):
       companies.append( f"{stocks['instruments'][i]['name']}")

    res = []

    for i in range(len(stocks['instruments'])):

        if stroka.lower() in f"{stocks['instruments'][i]['name']}":
            res.append(f"{stocks['instruments'][i]}")        
    return res 





def sort_list_dict(list_dict:list, key_name_sort) -> list:
    
    if len(list_dict) <=1:
        return list_dict
    base_elem = list_dict[0]

    left = [elem for elem in list_dict[0:] if elem[key_name_sort] < base_elem[key_name_sort]]
    center = [i for i in list_dict if i[key_name_sort] == base_elem[key_name_sort]]
    right = [elem for elem in list_dict[0:] if elem[key_name_sort] > base_elem[key_name_sort]]
    return sort_list_dict(left,key_name_sort) + center + sort_list_dict(right,key_name_sort)



def select_stocks2(list_dict:list, search_key:str, search_value:str) -> list:
    list_dict = sort_list_dict(list_dict,search_key)



    left,right = 0, len(list_dict) - 1

    while left<=right:
        mid = (left+right)//2

        if list_dict[mid][search_key] == search_value:
            return list_dict[mid]
        if list_dict[mid][search_key] > search_value:
            right = mid - 1
        if list_dict[mid][search_key] < search_value:
            left = mid + 1
        





# вспомогательная функция для открытия главного (начального) json 
# открытие json файла

def writer(file_path:str) -> dict:
   
    with open(file_path,"r",encoding="utf-8") as file:
       stocks = json.load(file)
    return stocks 




#---------------------------------------------------
# функция для создания папки с файлом по определенному слову
def creating_json(stocks:dict, search_par:str) -> str:

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
def choose_data(stocks:dict) -> str:
    
    datas = []

    for i in range(len(stocks['instruments'])):
        datas.extend(tuple(stocks['instruments'][i].keys()))
    datas = set(datas)
    choose = input(f"Выбери параметр, по которому мы сможем создать и отсортировать json файлы: {datas}")
    if choose in datas:
        return choose
    else:
        return "error"



# рейтинг стран по популярности (акции)
def country_popularity_rating(stocks:dict) -> collections:
    country_list = [stocks['instruments'][i]['countryOfRiskName'] for i in range(len(stocks['instruments']))]
    result = collections.Counter(country_list)
    return result


# функция для того, чтобы найти акции, появившиеся на бирже в 2010 году 
def companies_by_date(date:int, stocks:dict) -> list:
    companies_list = []


    for i in range(len(stocks['instruments'])):
        keys = stocks['instruments'][i].keys()
        if 'first1dayCandleDate' in keys and str(date) in stocks['instruments'][i]['first1dayCandleDate']:
            companies_list.append(stocks['instruments'][i])
    return companies_list


# поиск самой старой компании по размещению акций на бирже
def the_oldest_company(stocks:dict) -> str:
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



def main(*args) -> None:
    
    tasks = {
        1: select_stocks,
        2: creating_json,
        3: country_popularity_rating,
        4: companies_by_date,
        5: the_oldest_company,
        6: select_stocks2
    }


    task = int(input(f"выбери функцию {tasks} "))

    return tasks[task](*args)




if __name__ == '__main__':
    print(main(writer(PATH_FILE)['instruments'],NAME_KEY,SEARCH_VALUE))
    

