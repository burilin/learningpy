import instruments
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

# переделать меню
#---------------------------------------------------------------------------------------------------------------------------
instrument = instruments.Instruments()
#instrument2 = instruments.Instruments(file_path="../data/sector/consumer.json")


def main():
    
    tasks = {
        1: {"name_task_rus" : "Поиск акций по значению указанного ключа(частичное вхождение)", "sys_name_function" : instrument.select_stocks, "funcs_params":["search_key", "search_value"]},
        2: {"name_task_rus" : "Создание папки с файлами по ключу", "sys_name_function" : instrument.json_creater,  "funcs_params":["search_key"]},
        3: {"name_task_rus" : "Рейтинг по частоте появления акций различных стран" ,"sys_name_function" : instrument.country_popularity_rating,  "funcs_params":[None]},
        4: {"name_task_rus" : "Поиск компаний по заданному году пояления акций на бирже" ,"sys_name_function" : instrument.companies_by_date,  "funcs_params":["year"]},
        5: {"name_task_rus" : "Поиск компании, чьи акции появились появились раньше других" ,"sys_name_function" : instrument.the_oldest_company,"funcs_params":[None]},
        6: {"name_task_rus" : "Поиск акций по значению указанного ключа(полное вхождение)" ,"sys_name_function" : instrument.select_stocks2,"funcs_params":["search_key", "search_value"]}
    }
    

    print("Привет, выбери функцию для работы с json-обьектом (введи номер из списка ниже)")
    [print(str(i) +' ------- ' + tasks[i]['name_task_rus']) for i in range(1,len(tasks)+1)]

    task = int(input())  #сделать красивый и понятный input
    params = [input(f"Введи значение параметра {i} ") for i in tasks[task]["funcs_params"] if i]

    return tasks[task]["sys_name_function"](*params)    


if __name__ == '__main__':
    result = main()
    print(result)
    

