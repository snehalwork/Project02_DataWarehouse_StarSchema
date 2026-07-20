from src.database import Database

db = Database()

engine = db.connect()

print(engine)