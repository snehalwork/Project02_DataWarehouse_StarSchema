from src.database import Database
from src.extract import Extract
from src.transform import Transform
from src.load_dimension import LoadDimension

db = Database()
extract = Extract()
transform = Transform()
loader = LoadDimension()

engine = db.connect()

df = extract.read_csv("data/customers.csv")

transform.validate_columns(
    df,
    [
        "customer_id",
        "first_name",
        "last_name",
        "gender",
        "city",
        "email",
        "created_date",
    ],
)

df = transform.remove_duplicates(df)
df = transform.fill_missing_values(df)
df = transform.clean_strings(df)
df = transform.convert_dates(df, ["created_date"])

loader.load_customers(engine, df)