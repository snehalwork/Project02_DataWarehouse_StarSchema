from src.extract import Extract

extract=Extract()

df=extract.read_csv("data/customers.csv")
# print(f"First 5 records:\n {df.head()}")