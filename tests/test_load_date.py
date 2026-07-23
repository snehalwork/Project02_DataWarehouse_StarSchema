from datetime import datetime

from src.database import Database
from src.load_dimension import LoadDimension

db = Database()
loader = LoadDimension()

engine = db.connect()

loader.load_dates(
    engine,
    datetime(2025, 1, 1),
    datetime(2026, 12, 31),
)

