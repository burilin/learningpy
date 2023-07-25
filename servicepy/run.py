import datetime
import json


def main():
    print('!run.py!')
    cur = set()
    with open("../data/data_stocks.json","r",encoding="utf-8") as file:
        stocks = json.load(file)
    for stock in range(len(stocks['instruments'])):
        cur.add(stocks['instruments'][stock]['currency'])
    #print(cur[0])
    
    choose = input(f"выберите валюту для справки из данного списка:  {' ,'.join(list(cur))}\n")
    if choose in cur:
        for i in range(len(stocks['instruments'])):
            
            if stocks['instruments'][i]['currency'] == choose or stocks['instruments'][i]['nominal']['currency'] == choose:
                print(f"{stocks['instruments'][i]}\n\n")
            else:
                print("такой валюты нет")
                main()
                break

       



def fullinfo():
    # в переменной companies храним название компаний
    companies = ""
    with open("../data/data_stocks.json","r",encoding="utf-8") as file:
       stocks = json.load(file)
    for i in range(len(stocks['instruments'])):
       companies += f"{stocks['instruments'][i]['name']}"
    
    company = input("введи интересующую компанию ")
    res = ""
    if company in companies:
        for i in range(len(stocks['instruments'])):
            if company == f"{stocks['instruments'][i]['name']}":
                res = f"{stocks['instruments'][i]}"
                break
        print(res)
    else:
        fullinfo()




def helper():
   
    with open("../data/data_stocks.json","r",encoding="utf-8") as file:
       stocks = json.load(file)
    for i in range(16):
        print(f"{stocks['instruments'][i]}\n\n")

       
   


if __name__ == '__main__':
    #main()
    fullinfo()
    #helper()
    

