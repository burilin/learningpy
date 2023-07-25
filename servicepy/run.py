import datetime
import json
# создать столько файлов в количестве отраслей. каждая отрасль в отдельный файл json
# сделать commit
#
#

def main():
    print('!run.py!')
    

       
def fullinfo():
    stroka = input("введи название интересующей компании ")
    return stroka 


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




def writer():
   
    with open("../data/data_stocks.json","r",encoding="utf-8") as file:
       stocks = json.load(file)
    return stocks 


def output():
    out = selsect_stocks()
    if out:
        for i in out:
            print(f"{i}\n\n")
    else:
        print("такой компании нет")

   


if __name__ == '__main__':
    output()
    

