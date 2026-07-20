from src.database import Database
from src.extract import Extract
from src.transform import Transform
from src.load_fact import LoadFact

db = Database()
extract = Extract()
transform = Transform()
loader = LoadFact()

engine = db.connect()

df = extract.read_csv("data/sales.csv")

transform.validate_columns(
    df,
    [
        "sale_id",
        "customer_id",
        "product_id",
        "region_id",
        "sale_date",
        "quantity",
        "unit_price",
        "total_price",
    ],
)

df = transform.remove_duplicates(df)
df = transform.fill_missing_values(df)
df = transform.clean_strings(df)
df = transform.convert_dates(df, ["sale_date"])

loader.load_sales(engine, df)