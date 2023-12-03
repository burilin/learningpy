import sqlite3 as sq
import uuid

class DateBase:
    def __init__(self, dp_path = "db/quots.db") -> None:
        self.dp_path = dp_path
        self.db = sq.connect(self.dp_path)

        

    def __repr__(self) -> str:
        return "db class"
    
    def create_table_quots(self): #, table_name:str, field:list):
        before_query = "DROP TABLE IF EXISTS quots"
        sql_query = "CREATE TABLE quots (uuid uuid PRIMARY KEY, time TEXT, price DECIMAL, uuid_stocks uuid REFERENCES stock(uuid) ON DELETE CASCADE)"
        self.db.execute(before_query)
        self.db.execute(sql_query)


    def create_table_stocks(self): #, table_name:str, field:list):
        before_query = "DROP TABLE IF EXISTS stocks"
        sql_query = "CREATE TABLE stocks (uuid uuid PRIMARY KEY, figi TEXT, name TEXT)"
        self.db.execute(before_query)
        self.db.execute(sql_query)    
        
    
    def inner_join(self): # как связать таблицы, в какой функции это делать?
        sql_join = "SELECT * FROM quots q INNER JOIN stocks s ON q.uuid_stocks = s.uuid"
        self.db.execute(sql_join)

    def inset_data(self, table_name:str, insert_value:list):
        pass


if __name__ == "__main__":
    base = DateBase()
    print(base.create_table_quots(), base.create_table_stocks(), base.inner_join())