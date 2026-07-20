from src.extract import Extract
from src.transform import Transform

extract=Extract()
transform=Transform()

df=extract.read_csv("data/customers.csv")

transform.validate_columns(
    df, [
        "customer_id",
        "first_name",
        "last_name",
        "gender",
        "city",
        "email",
        "created_date",
        ],
        )
df=transform.remove_duplicates(df)
df=transform.fill_missing_values(df)
df=transform.clean_strings(df)
df=transform.convert_dates(
    df,
    ["created_date"],
    )

print("\nTransformation Completed.")

print(df.dtypes)

print(df.head())