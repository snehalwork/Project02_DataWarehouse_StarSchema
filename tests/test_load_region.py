from src.database import Database
from src.extract import Extract
from src.transform import Transform
from src.load_dimension import LoadDimension

db = Database()
extract = Extract()
transform = Transform()
loader = LoadDimension()

engine = db.connect()

df = extract.read_csv("data/regions.csv")

transform.validate_columns(
    df,
    [
        "region_id",
        "region_name",
        "state",
        "country"
    ]
)

df = transform.remove_duplicates(df)
df = transform.fill_missing_values(df)
df = transform.clean_strings(df)

loader.load_regions(engine, df)