from sqlalchemy import text
import pandas as pd
from src.logger import logger

class LoadFact:

    def load_sales(self, engine, df: pd.DataFrame):

        customer_query = text("""
            SELECT customer_key
            FROM dim_customer
            WHERE customer_id = :customer_id
        """)

        product_query = text("""
            SELECT product_key
            FROM dim_product
            WHERE product_id = :product_id
        """)

        region_query = text("""
            SELECT region_key
            FROM dim_region
            WHERE region_id = :region_id
        """)

        date_query = text("""
            SELECT date_key
            FROM dim_date
            WHERE full_date = :sale_date
        """)

        insert_query = text("""
            INSERT INTO fact_sales
            (
                customer_key,
                product_key,
                region_key,
                date_key,
                quantity,
                unit_price,
                total_price
            )
            VALUES
            (
                :customer_key,
                :product_key,
                :region_key,
                :date_key,
                :quantity,
                :unit_price,
                :total_price
            )
        """)

        inserted = 0

        with engine.begin() as connection:

            for _, row in df.iterrows():

                customer_key = connection.execute(
                    customer_query,
                    {"customer_id": row["customer_id"]}
                ).scalar()

                product_key = connection.execute(
                    product_query,
                    {"product_id": row["product_id"]}
                ).scalar()

                region_key = connection.execute(
                    region_query,
                    {"region_id": row["region_id"]}
                ).scalar()

                date_key = connection.execute(
                    date_query,
                    {"sale_date": row["sale_date"]}
                ).scalar()

                if None in (customer_key, product_key, region_key, date_key):
                    print(f"Skipped Sale ID {row['sale_id']} (Lookup Failed)")
                    continue

                connection.execute(
                    insert_query,
                    {
                        "customer_key": customer_key,
                        "product_key": product_key,
                        "region_key": region_key,
                        "date_key": date_key,
                        "quantity": row["quantity"],
                        "unit_price": row["unit_price"],
                        "total_price": row["total_price"],
                    },
                )

                inserted += 1

        print("\n========== LOAD FACT_SALES ==========")
        logger.info(f"Loaded fact_sales ({inserted} records)")
        print(f"Inserted Records : {inserted}")