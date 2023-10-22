import instruments
import stocks
import stock
import tinkoff_data
import signals
from flask import Flask, render_template, url_for, request, redirect, g



instrument = instruments.Instruments()
Stocks = stocks.Stocks()
Stock = stock.Stock()
tinkoff = tinkoff_data.TinkoffData()
signal = signals.Signals()

# def main():
    
#     tasks = {
#         1: {"name_task_rus" : "Поиск акций по значению указанного ключа(частичное вхождение)", "sys_name_function" : instrument.select_stocks, "funcs_params":["search_key", "search_value"]},
#         2: {"name_task_rus" : "Создание папки с файлами по ключу", "sys_name_function" : instrument.json_creater,  "funcs_params":["search_key"]},
#         3: {"name_task_rus" : "Рейтинг по частоте появления акций различных стран" ,"sys_name_function" : Stocks.country_popularity_rating,  "funcs_params":[]},
#         4: {"name_task_rus" : "Поиск компаний по заданному году пояления акций на бирже" ,"sys_name_function" : Stocks.companies_by_date,  "funcs_params":["year"]},
#         5: {"name_task_rus" : "Поиск компании, чьи акции появились появились раньше других" ,"sys_name_function" : Stocks.the_oldest_company,"funcs_params":[]},
#         6: {"name_task_rus" : "Поиск акций по значению указанного ключа(полное вхождение)" ,"sys_name_function" : instrument.select_stocks2,"funcs_params":["search_key", "search_value"]},
#         7: {"name_task_rus" : "Получение точек по закрытию (дата;цена)" ,"sys_name_function" : Stock.get_points_closing_graphic, "funcs_params":["figi"]},
#         8: {"name_task_rus" : "Создание папки с файлами, где каждый файл - json-candle файл " ,"sys_name_function" : tinkoff.loader, "funcs_params":["figi", "date_from", "date_to"]},
#         9: {"name_task_rus" : "Отправляет сигнал о покупке/продаже той или иной акции" ,"sys_name_function" : signal.signal, "funcs_params":["figi"]}
#     }
    

#     print("Привет, выбери функцию для работы с json-обьектом (введи номер из списка ниже)")
#     [print(str(i) +' ------- ' + tasks[i]['name_task_rus']) for i in range(1,len(tasks)+1)]
    
#     task = int(input())
#     params = [input(f"Введи значение параметра {i} ") for i in tasks[task]["funcs_params"] if i]
#     return tasks[task]["sys_name_function"](*params)    

app = Flask(__name__)


@app.route("/", methods = ["POST", "GET"])
def main():
    global tasks
    tasks = {
        1: {"name_task_rus" : "Поиск акций по значению указанного ключа(частичное вхождение)", "sys_name_function" : instrument.select_stocks, "funcs_params":["search_key", "search_value"]},
        2: {"name_task_rus" : "Создание папки с файлами по ключу", "sys_name_function" : instrument.json_creater,  "funcs_params":["search_key"]},
        3: {"name_task_rus" : "Рейтинг по частоте появления акций различных стран" ,"sys_name_function" : Stocks.country_popularity_rating,  "funcs_params":[]},
        4: {"name_task_rus" : "Поиск компаний по заданному году пояления акций на бирже" ,"sys_name_function" : Stocks.companies_by_date,  "funcs_params":["year"]},
        5: {"name_task_rus" : "Поиск компании, чьи акции появились появились раньше других" ,"sys_name_function" : Stocks.the_oldest_company,"funcs_params":[]},
        6: {"name_task_rus" : "Поиск акций по значению указанного ключа(полное вхождение)" ,"sys_name_function" : instrument.select_stocks2,"funcs_params":["search_key", "search_value"]},
        7: {"name_task_rus" : "Получение точек по закрытию (дата;цена)" ,"sys_name_function" : Stock.get_points_closing_graphic, "funcs_params":["figi"]},
        8: {"name_task_rus" : "Создание папки с файлами, где каждый файл - json-candle файл " ,"sys_name_function" : tinkoff.loader, "funcs_params":["figi", "date_from", "date_to"]},
        9: {"name_task_rus" : "Отправляет сигнал о покупке/продаже той или иной акции" ,"sys_name_function" : signal.signal, "funcs_params":["figi"]}
    }
    

    
    ol_tasks = [str(i) +' ------- ' + tasks[i]['name_task_rus'] for i in range(1,len(tasks)+1)]  
    return render_template("index.html", ol_tasks=ol_tasks)  


@app.route("/get_args", methods = ["POST", "GET"])
def get_args():
    task = int(request.form["number"])
    params = [f"Введи значение параметра {i} " for i in tasks[task]["funcs_params"] if i]
    return render_template("get_args.html", params=params)

@app.route("/graf")
def graf_stock():
    res = Stock.get_points_closing_graphic('TCS109029540')
    return f'<h1> {res[0]} </h1>'

@app.route("/result", methods = ["POST", "GET"])    #здесь затык
def result():
    pass
    #return render_template('result.html', res=res)


if __name__ == '__main__':
    app.run(debug=True)
    # result = main()
    # print(result)
    

