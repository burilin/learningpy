import json
import requests
import datetime
# url_post = "https://sandbox-invest-public-api.tinkoff.ru/rest/tinkoff.public.invest.api.contract.v1.MarketDataService/GetCandles"

# token = "t.ZDlrOhEC9ykat6XRj1laFX4NLWoI6WgOYp-thfy7ceafgAt16S4hqMqQisDNp1sUceg1-2diDXa2J5dox9i_3Q"
# headers = {"Authorization": "Bearer {}".format(token),
#                    "accept": "application/json",
#                    "Content-Type": "application/json"}
# data_json = {
#   "figi": "BBG004730N88",
#   "from": "2021-09-19T14:41:49.263000Z",
#   "to": "2022-09-19T14:41:49.263000Z",
#   "interval": "CANDLE_INTERVAL_DAY"






# tasks = {
    
#     1: {"name_task_rus" : "Поиск акций по значению указанного ключа(полное вхождение)" ,"sys_name_function" : instrument.select_stocks2,"funcs_params":["search_key", "search_value"]},
#     2: {"name_task_rus" : "Получение точек по закрытию (дата;цена)" ,"sys_name_function" : Stock.get_points_closing_graphic, "funcs_params":["figi"]},
#     3: {"name_task_rus" : "Отправляет сигнал о покупке/продаже той или иной акции" ,"sys_name_function" : signal.signal, "funcs_params":["figi"]}
# }

# @app.route("/", methods = ["POST", "GET"])
# def start():
    
#     ol_tasks = [str(i) +' ------- ' + tasks[i]['name_task_rus'] for i in range(1,len(tasks)+1)]  
#     return render_template("index.html", ol_tasks=ol_tasks)  


# @app.route("/get_args", methods = ["POST", "GET"])
# def get_args():
#     task = int(request.form["number"])
#     params = [i for i in tasks[task]["funcs_params"] if i]
#     return render_template("get_args.html", params=params)

# @app.route("/graf")
# def graf_stock():
#     res = Stock.get_points_closing_graphic('TCS109029540')
#     return f'<h1> {res[0]} </h1>'

# @app.route("/result/<list>", methods = ["POST", "GET"])    #здесь затык
# def result(list):
#     print(list)
#     return render_template('result.html')

# res = str(['search_key', 'search_value', 'figi']+[1])
# for i in ["'" ,"[" ,"]" ," "]:
#     res = res.replace(i,"")
# res = res.split(",")
# print(res)

print(f"{datetime.datetime.now() - datetime.timedelta(days=2)}"[:10])