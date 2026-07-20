from datetime import datetime

from src.database import Database
from src.extract import Extract
from src.transform import Transform
from src.load_fact import LoadFact
from src.load_dimension import LoadDimension
from src.generic_loader import GenericDimensionLoader
from src.logger import logger


def main():

    print("\n========== ETL PIPELINE STARTED ==========\n")
    logger.info("ETL Pipeline Started")

    db = Database()
    extract = Extract()
    transform = Transform()

    date_loader = LoadDimension()
    generic_loader = GenericDimensionLoader()
    fact_loader = LoadFact()

    engine = db.connect()

    # ==========================
    # CUSTOMER DIMENSION
    # ==========================

    customer_df = extract.read_csv("data/customers.csv")

    transform.validate_columns(
        customer_df,
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

    customer_df = transform.remove_duplicates(customer_df)
    customer_df = transform.fill_missing_values(customer_df)
    customer_df = transform.clean_strings(customer_df)
    customer_df = transform.convert_dates(
        customer_df,
        ["created_date"],
    )

    generic_loader.load_dimension(
        engine,
        customer_df,
        "dim_customer",
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

    # ==========================
    # PRODUCT DIMENSION
    # ==========================

    product_df = extract.read_csv("data/products.csv")

    transform.validate_columns(
        product_df,
        [
            "product_id",
            "product_name",
            "category",
            "brand",
            "price",
        ],
    )

    product_df = transform.remove_duplicates(product_df)
    product_df = transform.fill_missing_values(product_df)
    product_df = transform.clean_strings(product_df)

    generic_loader.load_dimension(
        engine,
        product_df,
        "dim_product",
        [
            "product_id",
            "product_name",
            "category",
            "brand",
            "price",
        ],
    )

    # ==========================
    # REGION DIMENSION
    # ==========================

    region_df = extract.read_csv("data/regions.csv")

    transform.validate_columns(
        region_df,
        [
            "region_id",
            "region_name",
            "state",
            "country",
        ],
    )

    region_df = transform.remove_duplicates(region_df)
    region_df = transform.fill_missing_values(region_df)
    region_df = transform.clean_strings(region_df)

    generic_loader.load_dimension(
        engine,
        region_df,
        "dim_region",
        [
            "region_id",
            "region_name",
            "state",
            "country",
        ],
    )

    # ==========================
    # DATE DIMENSION
    # ==========================

    date_loader.load_dates(
        engine,
        datetime(2026, 1, 1),
        datetime(2026, 12, 31),
    )

    # ==========================
    # FACT TABLE
    # ==========================

    sales_df = extract.read_csv("data/sales.csv")

    transform.validate_columns(
        sales_df,
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

    sales_df = transform.remove_duplicates(sales_df)
    sales_df = transform.fill_missing_values(sales_df)
    sales_df = transform.clean_strings(sales_df)
    sales_df = transform.convert_dates(
        sales_df,
        ["sale_date"],
    )

    fact_loader.load_sales(engine, sales_df)

    logger.info("ETL Pipeline Completed")
    print("\n========== ETL PIPELINE COMPLETED ==========\n")


if __name__ == "__main__":
    main()