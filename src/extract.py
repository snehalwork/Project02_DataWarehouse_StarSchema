import pandas as pd 

class Extract:
    def read_csv(self, file_path: str)-> ps.DataFrame:
        try: 
            df=pd.read_csv(file_path)
            print(f"Sucessfully loaded {len(df)} records.")
            print(f"Columns: {list(df.columns)}")
            print(df.dtypes)

            return df
        
        except FileNotFoundError:
            print(f"Error: file not found -> {file_path}")

        except Exception as e:
            print(f"Unexpected Error: {e}")