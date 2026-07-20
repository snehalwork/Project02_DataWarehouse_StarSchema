
'''
Handle missing values
Remove duplicates
Clean string columns
Convert date columns
Validate required columns
'''

import pandas as pd 

class Transform:

    def remove_duplicates(self, df:pd.DataFrame)-> pd.DataFrame:
        before=len(df)
        df =df.drop_duplicates()
        after=len(df)
        print(f"Removed {before -after } duplicate records. ")
        
        return df
    
    def fill_missing_values(self, df:pd.DataFrame)-> pd.DataFrame:
        df=df.fillna("Unknown")
        print("Missing Values are handled. ")

        return df
    
    def clean_strings(self, df:pd.DataFrame)-> pd.DataFrame:
        string_columns = df.select_dtypes(include=["object", "string"]).columns
        for col in string_columns:
            df[col]=df[col].astype(str).str.strip()
        
        print("String columns cleaned.")

        return df
    
    def convert_dates(self, df:pd.DataFrame, columns : list)->pd.DataFrame:
        for col in columns:
            df[col]=pd.to_datetime(df[col])

        print("Date columns converted.")

        return df
   
    def validate_columns(self, df: pd.DataFrame, expected_columns: list): 
        missing=set(expected_columns)-set(df.columns)

        if missing:
            raise ValueError(f"Missing column:{missing}")
        
        print("Columns validation Successful. ")