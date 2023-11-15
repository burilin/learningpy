import instruments
import stocks
import stock
import tinkoff_data
import signals
from bokeh.embed import components
from bokeh.plotting import figure
from flask import Flask, render_template, url_for, request, redirect, g



instrument = instruments.Instruments()
Stocks = stocks.Stocks()
Stock = stock.Stock()
tinkoff = tinkoff_data.TinkoffData()
signal = signals.Signals()

def main():
    
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
    

    print("Привет, выбери функцию для работы с json-обьектом (введи номер из списка ниже)")
    [print(str(i) +' ------- ' + tasks[i]['name_task_rus']) for i in range(1,len(tasks)+1)]
    
    task = int(input())
    params = [input(f"Введи значение параметра {i} ") for i in tasks[task]["funcs_params"] if i]
    return tasks[task]["sys_name_function"](*params)    





app = Flask(__name__)
tasks = {
    
    1: {"name_task_rus" : "Поиск акций по значению указанного ключа(полное вхождение)" ,"sys_name_function" : instrument.select_stocks2,"funcs_params":["search_key", "search_value"]},
    2: {"name_task_rus" : "Получение точек по закрытию (дата;цена)" ,"sys_name_function" : Stock.get_points_closing_graphic, "funcs_params":[ "figi"]},
    3: {"name_task_rus" : "Отправляет сигнал о покупке/продаже той или иной акции" ,"sys_name_function" : signal.signal, "funcs_params":["start_date", "end_date","figi"]}
}

@app.route("/", methods = ["POST", "GET"])
def start():
    ol_tasks = [str(i) +' ------- ' + tasks[i]['name_task_rus'] for i in range(1,len(tasks)+1)]  
    return render_template("index.html", ol_tasks=ol_tasks)  


@app.route("/get_args", methods = ["POST", "GET"])
def get_args():
    task = int(request.form["number"])
    params = [i for i in tasks[task]["funcs_params"] if i]
    return render_template("get_args.html", params=params, task = task)



@app.route("/result/<list>/<task>", methods = ["POST", "GET"])
def result(list, task):
    for i in ["'" ,"[" ,"]" ," "]:
        list = list.replace(i,"")
    list = list.split(",")
    #print(list, task)
    par_list = [request.form[list[i]] for i in range(len(list))]
    print(request.form)
    #par_list = [request.form["figi"]]
    #par_list = [request.form.get("figi")]
    if task == 3:
        for i in range(2):
            par_list[i][5:7], par_list[i][-1:-3] = par_list[i][-1:-3], par_list[i][5:7]
    global res
    res = tasks[int(task)]["sys_name_function"](*par_list)
    return render_template('result.html', res = res, task=task)


 
# Root endpoint 
@app.route('/graphic')
def graphic():
    # Define Plot Data 
    labels = [i[0][:10] for i in res]
    
 
    data = [i[1] for i in res]
 
    # Return the components to the HTML template 
    return render_template(
        template_name_or_list='graphic.html',
        data=data,
        labels=labels,
    )


if __name__ == '__main__':
    app.run(debug=True)
    # result = main()
    # print(result)
    

