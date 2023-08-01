import time
import json,os
import collections

### Tasks ###
# Cоздать столько файлов в количестве отраслей. каждая отрасль в отдельный файл json+
# Cделать commit опубликовать свои изменения на  GitHub+-
# Поиск информации об акциях по наименованию компанию (вхождение строки символов в название)+

# Полностью ориентироваться в структуре данного json Делать поиски и выборки условно любых запросов.+-
# Например, найти самую старую компанию по размещению акций. Выбрать все акции размещенные на бирже в 2010 году+
# Рассчитать популярные страны по юрисдикции торгуемых акций. В какой стране выпущены акции наиболее популярные после РФ+
# Консольное пользовательское меню реализовать с модуляцией диалога (выберите задачу из меню, продолжить/завершить)-

### Notes ###
# Структура файлов проекта (мусор в папках)
# Надо обратить внимание на состав функций (познакомиться с принципами SOLID и структурного программирования)
# Общий синтаксис функций в питоне (параметры и типизация возвращаемых значений)
# Связь логики программы с архитектурой (составом функций и модулей)
# Эффективные алгоритмы поиска, обходов списков и словарей. Генераторы.

def main() -> None:
    print('старт')
    time_start = time.time()
    creating_json()
    time_end = time.time()
    print("конец, время выполнения = ", time_end - time_start)
       

# ввод имени компании
def fullinfo() -> str:
    stroka = input("введи название интересующей компании ")
    return stroka 

# поиск компаний по заданной строке
def selsect_stocks() -> list:
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
def writer() -> dict:
   
    with open("../data/data_stocks.json","r",encoding="utf-8") as file:
       stocks = json.load(file)
    return stocks 

# вывод 
def output() -> None:
    out = selsect_stocks()
    if out:
        for i in out:
            print(f"{i}\n\n")
    else:
        print("такой компании нет")

   
#---------------------------------------------------
def creating_json() -> None:
    stocks = writer()
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
    except Exception:
        print("невозможно отсортировать по данному ключу")
    
    
# возвращает строку, являющейся параметром для сортировки json
def choose_data() -> str:
    stocks = writer()
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
def country_popularity_rating() -> None:
    stocks = writer()
    country_list = [stocks['instruments'][i]['countryOfRiskName'] for i in range(len(stocks['instruments']))]
    result = collections.Counter(country_list)
    print(result)



def companies_2010():
    stocks = writer()

    companies_list = []


    for i in range(len(stocks['instruments'])):
        keys = stocks['instruments'][i].keys()
        if 'first1dayCandleDate' in keys and '2010' in stocks['instruments'][i]['first1dayCandleDate']:
            companies_list.append(stocks['instruments'][i])
    print(companies_list)


def the_oldest_company():
    stocks = writer()

    dates_list = []
    the_company = []

    for i in range(len(stocks['instruments'])):
        keys = stocks['instruments'][i].keys()
        if 'first1dayCandleDate' in keys:
            dates_list.append(stocks['instruments'][i]['first1dayCandleDate'][:4])
    first_date = min(list(map(int,dates_list)))
    print(first_date)

    for i in range(len(stocks['instruments'])):
        keys = stocks['instruments'][i].keys()
        if 'first1dayCandleDate' in keys:
            if str(first_date) in stocks['instruments'][i]['first1dayCandleDate'][:4]:
                the_company.append(stocks['instruments'][i])
    print(the_company)




if __name__ == '__main__':
    #output()
    #creating_json()
    #main()
    #choose_data()
    #country_popularity_rating()
    #companies_2010()
    the_oldest_company()
    
