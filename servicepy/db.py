import sqlite3 as sq

class DateBase:
    def __init__(self, dp_path = "db/quots.db") -> None:
        self.dp_path = dp_path
        self.db = sq.connect(self.dp_path)

        

    def __repr__(self) -> str:
        return "db class"
    

    def create_table(self, table_name:str, fields:str):
        before_query = f"DROP TABLE IF EXISTS {table_name}"
        sql_query = f"CREATE TABLE {table_name} ({fields})"
        self.db.execute(before_query)
        self.db.execute(sql_query) 
        
    
    def inner_join(self):
        sql_join = "SELECT * FROM quots q INNER JOIN stocks s ON q.uuid_stocks = s.uuid"
        self.db.execute(sql_join)

    def inset_data(self, table_name:str, *insert_values):
        val = str(insert_values)
        val = val.replace('(',"")
        val = val.replace(')',"")

        if val[-1] == ',':
            val = val[:-1]
        
        if table_name == 'stocks':
            sql_insert = 'INSERT INTO {} (uuid, figi, name) VALUES({})'.format(table_name,val)
        else:
            sql_insert = 'INSERT INTO {} (uuid, time, price, uuid_stocks) VALUES({})'.format(table_name,val)
        sql_insert = sql_insert.replace("'",'"')
        self.db.execute(sql_insert)
    

    def check_name(self,name_stock):
        sql_select = f"SELECT name FROM stocks"
        answer = self.db.execute(sql_select)
        if str(answer.fetchall()[0][0]) == name_stock:
            sql_select_data = "SELECT time, price FROM quots"
            return self.db.execute(sql_select_data)
        return False
    
    
    def db_close(self):
        self.db.commit()
        self.db.close()


if __name__ == "__main__":
    base = DateBase()