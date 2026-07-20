from sqlalchemy import text
import pandas as pd

from src.logger import logger


class GenericDimensionLoader:

    def load_dimension(
        self,
        engine,
        df: pd.DataFrame,
        table_name: str,
        columns: list,
    ):

        column_string = ", ".join(columns)
        value_string = ", ".join([f":{col}" for col in columns])

        query = text(f"""
            INSERT INTO {table_name}
            (
                {column_string}
            )
            VALUES
            (
                {value_string}
            )
        """)

        inserted = 0

        with engine.begin() as connection:

            for _, row in df.iterrows():

                params = {
                    col: row[col]
                    for col in columns
                }

                connection.execute(query, params)
                inserted += 1

        logger.info(f"Loaded {table_name} ({inserted} records)")

        print(f"\n========== {table_name.upper()} ==========")
        print(f"Inserted Records : {inserted}")