import datetime
import json





def main():
    with open('../data/data_stocks.json') as f:
        templates = json.load(f)

    print(templates['instruments'][0])


    print('!run.py!')






if __name__ == '__main__':
    main()

