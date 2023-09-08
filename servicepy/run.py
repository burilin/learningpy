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


#---------------------------------------------------------------------------------------------------------------------------

instrument = instruments.Instruments()
instrument2 = instruments.Instruments(file_path="../data/sector/consumer.json")


def main() -> None:

    
    tasks = {
        1: {"name_task_rus" : "Поиск акций по наименованию(частичное вхождение)", "sys_name_function" : instrument.select_stocks, "funcs_params":{"params_names":["search_value", "search_key"], "params_type":"str"}},
        2: {"name_task_rus" : "Создание папки с файлами по ключу", "sys_name_function" : instrument.writer,  "funcs_params":{"par_name":"search_par", "par_type":"str"}},
        3: {"name_task_rus" : "Рейтинг по частоте появления акций различных стран" ,"sys_name_function" : instrument.country_popularity_rating,  "funcs_params":"No need in params"},
        4: {"name_task_rus" : "Поиск компаний по заданному году пояления акций на бирже" ,"sys_name_function" : instrument.companies_by_date,  "funcs_params":{"par_name":"year", "par_type":"int"}},
        5: {"name_task_rus" : "Поиск компании, чьи акции появились появились раньше других" ,"sys_name_function" : instrument.the_oldest_company,"funcs_params":"No need in params"},
        6: {"name_task_rus" : "Поиск акций по наименованию(полное вхождение)" ,"sys_name_function" : instrument.select_stocks2,"funcs_params":{"params_names":["search_value", "search_key"], "params_type":"str"}}
    }
    lis_no_params = [i for i in range(1,len(tasks)+1) if tasks[i]['funcs_params']=="No need in params"]
    lis_one_param = [i for i in range(1,len(tasks)+1) if "par_name" in tasks[i]['funcs_params']]
    lis_some_params = [i for i in range(1,len(tasks)+1) if "params_names" in tasks[i]['funcs_params']]


    print("Привет, выбери функцию для работы с json-обьектом (введи номер из списка ниже)")
    [print(str(i) +' ------- ' + tasks[i]['name_task_rus']) for i in range(1,len(tasks)+1)]
    task = int(input())  #сделать красивый и понятный input
    if task in lis_no_params:
        return tasks[task]['sys_name_function']()
    elif task in lis_one_param:
        param = input(f"Вы выбрали функцию, для выполнения которой нужен параметр (введи его): {tasks[task]['funcs_params']}: ")
        return tasks[task]['sys_name_function'](param)
    elif task in lis_some_params:
        params = input(f"""Вы выбрали функцию, для выполнения которой нужны параметры: {tasks[task]['funcs_params']}
Введите параметры через запятую без пробела: """).split(',')
        return tasks[task]['sys_name_function'](*params)
    else:
        return "функции под таким номером не существует"




if __name__ == '__main__':
    result = main()
    print(result)
    

