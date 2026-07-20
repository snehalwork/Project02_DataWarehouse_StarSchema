from sqlalchemy import text
from datetime import timedelta
import pandas as pd
from src.logger import logger

class LoadDimension:

    # ==========================
    # Load Customer Dimension
    # ==========================
    def load_customers(self, engine, df: pd.DataFrame):

        query = text("""
            INSERT INTO dim_customer
            (
                customer_id,
                first_name,
                last_name,
                gender,
                city,
                email,
                created_date
            )
            VALUES
            (
                :customer_id,
                :first_name,
                :last_name,
                :gender,
                :city,
                :email,
                :created_date
            )
        """)

        inserted = 0

        with engine.begin() as connection:

            for _, row in df.iterrows():

                connection.execute(
                    query,
                    {
                        "customer_id": row["customer_id"],
                        "first_name": row["first_name"],
                        "last_name": row["last_name"],
                        "gender": row["gender"],
                        "city": row["city"],
                        "email": row["email"],
                        "created_date": row["created_date"],
                    },
                )

                inserted += 1

        print("\n========== LOAD DIM_CUSTOMER ==========")
        logger.info(f"Inserted {inserted} records into dim_customer")
        print(f"Inserted Records : {inserted}")

    # ==========================
    # Load Product Dimension
    # ==========================
    def load_products(self, engine, df: pd.DataFrame):

        query = text("""
            INSERT INTO dim_product
            (
                product_id,
                product_name,
                category,
                brand,
                price
            )
            VALUES
            (
                :product_id,
                :product_name,
                :category,
                :brand,
                :price
            )
        """)

        inserted = 0

        with engine.begin() as connection:

            for _, row in df.iterrows():

                connection.execute(
                    query,
                    {
                        "product_id": row["product_id"],
                        "product_name": row["product_name"],
                        "category": row["category"],
                        "brand": row["brand"],
                        "price": row["price"],
                    },
                )

                inserted += 1

        print("\n========== LOAD DIM_PRODUCT ==========")
        logger.info(f"Inserted {inserted} records into dim_product")
        print(f"Inserted Records : {inserted}")

    # ==========================
    # Load Region Dimension
    # ==========================
    def load_regions(self, engine, df: pd.DataFrame):

        query = text("""
            INSERT INTO dim_region
            (
                region_id,
                region_name,
                state,
                country
            )
            VALUES
            (
                :region_id,
                :region_name,
                :state,
                :country
            )
        """)

        inserted = 0

        with engine.begin() as connection:

            for _, row in df.iterrows():

                connection.execute(
                    query,
                    {
                        "region_id": row["region_id"],
                        "region_name": row["region_name"],
                        "state": row["state"],
                        "country": row["country"],
                    },
                )

                inserted += 1

        print("\n========== LOAD DIM_REGION ==========")
        logger.info(f"Inserted {inserted} records into dim_region")
        print(f"Inserted Records : {inserted}")

    # ==========================
    # Generate & Load Date Dimension
    # ==========================
    def load_dates(self, engine, start_date, end_date):

        query = text("""
            INSERT INTO dim_date
            (
                date_key,
                full_date,
                day,
                month,
                month_name,
                quarter,
                year,
                weekday_name
            )
            VALUES
            (
                :date_key,
                :full_date,
                :day,
                :month,
                :month_name,
                :quarter,
                :year,
                :weekday_name
            )
        """)

        inserted = 0
        current_date = start_date

        with engine.begin() as connection:

            while current_date <= end_date:

                connection.execute(
                    query,
                    {
                        "date_key": int(current_date.strftime("%Y%m%d")),
                        "full_date": current_date.date(),
                        "day": current_date.day,
                        "month": current_date.month,
                        "month_name": current_date.strftime("%B"),
                        "quarter": ((current_date.month - 1) // 3) + 1,
                        "year": current_date.year,
                        "weekday_name": current_date.strftime("%A"),
                    },
                )

                inserted += 1
                current_date += timedelta(days=1)

        print("\n========== LOAD DIM_DATE ==========")
        logger.info(f"Inserted {inserted} records into dim_date")
        print(f"Inserted Records : {inserted}")