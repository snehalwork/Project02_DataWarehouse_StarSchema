from src.database import Database
from src.scd_loader import SCDLoader

db = Database()
engine = db.connect()

loader = SCDLoader()

loader.update_customer_city(
    engine,
    101,
    "Mumbai"
)