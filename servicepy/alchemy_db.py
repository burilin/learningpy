import sqlalchemy as db

class Alchemy:
    def __init__(self, db_path = "db/quots_alchemy") -> None:
        self.db_path = db_path
        self.engine = db.create_engine("sqlite:///db/quots_alchemy")
        self.connection = self.engine.connect()
        self.meatadata = db.MetaData()

    def create_quots(self):
        quots = db.Table('quots', self.meatadata,
        db.Column("uuid", db.Uuid, primary_key=True),
        db.Column("time", db.Text,),
        db.Column("price", db.Float,),
        db.Column("uuid_stocks", db.Text)
        )
        return quots
    
    def create_stocks(self):
        stocks = db.Table('stocks', self.meatadata,
        db.Column("uuid", db.Uuid, primary_key=True),
        db.Column("figi", db.Text,),
        db.Column("name", db.Text,)
        )
        return stocks
    
    

    

    
    def __repr__(self) -> str:
        return "Alchemy class"
    

