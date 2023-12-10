import sqlite3 as sq
import uuid

class DateBase:
    def __init__(self, dp_path = "db/quots.db") -> None:
        self.dp_path = dp_path
        self.db = sq.connect(self.dp_path)

        

    def __repr__(self) -> str:
        return "db class"
    

    def create_table(self, table_name:str, fields:str):
        before_query = f"DROP TABLE IF EXISTS {table_name}"
        sql_query = f"CREATE TABLE {table_name} {(fields)}"
        self.db.execute(before_query)
        self.db.execute(sql_query)
    
    # def create_table(self, table_name:str, field:list):
    #     before_query = f"DROP TABLE IF EXISTS {table_name}"
    #     sql_query = "CREATE TABLE quots (uuid uuid PRIMARY KEY NOT NULL , time TEXT, price DECIMAL, uuid_stocks uuid REFERENCES stocks(uuid) ON DELETE CASCADE)"
    #     self.db.execute(before_query)
    #     self.db.execute(sql_query)


    # def create_table_stocks(self, table_name:str, field:list):
    #     before_query = f"DROP TABLE IF EXISTS {table_name}"
    #     sql_query = "CREATE TABLE stocks (uuid uuid PRIMARY KEY NOT NULL, figi TEXT, name TEXT)"
    #     self.db.execute(before_query)
    #     self.db.execute(sql_query)    
        
    
    def inner_join(self): # как связать таблицы, в какой функции это делать?
        sql_join = "SELECT * FROM quots q INNER JOIN stocks s ON q.uuid_stocks = s.uuid"
        self.db.execute(sql_join)

    def inset_data(self, table_name:str, *insert_values:tuple):
        if table_name == 'stocks':
            sql_insert = "INSERT INTO {} (uuid, figi, name) VALUES({})".format(table_name,*insert_values)
        else:
            sql_insert = "INSERT INTO {} (uuid, time, price, uuid_stocks) VALUES({}))".format(table_name,*insert_values)
        self.db.execute(sql_insert)


if __name__ == "__main__":
    base = DateBase()
    #print(base.create_table_stocks(), base.create_table_quots(), base.inner_join())