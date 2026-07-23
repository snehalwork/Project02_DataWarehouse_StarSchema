#  Project 02 - Data Warehouse ETL Pipeline (Star Schema)

A complete end-to-end Data Warehouse ETL project built using **Python**, **Pandas**, **SQLAlchemy**, and **MySQL** following a **Star Schema** architecture.

This project extracts data from CSV files, performs data cleaning and validation, loads dimension and fact tables into a MySQL Data Warehouse, implements **SCD Type 2**, and provides a reusable ETL pipeline.

---

#  Technologies Used

- Python 3
- Pandas
- SQLAlchemy
- PyMySQL
- MySQL
- Git
- VS Code

---

#  Project Structure

```
Project02_DataWarehouse_StarSchema/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── regions.csv
│   └── sales.csv
│
├── logs/
│   └── etl.log
│
├── sql/
│   └── create_tables.sql
│
├── src/
│   ├── config.py
│   ├── database.py
│   ├── extract.py
│   ├── transform.py
│   ├── generic_loader.py
│   ├── load_dimension.py
│   ├── load_fact.py
│   ├── logger.py
│   ├── main.py
│   └── scd_loader.py
│
├── tests/
│
├── README.md
├── requirements.txt
├── .gitignore
└── .env
```

---

#  Project Architecture

```
CSV Files
     │
     ▼
Extract Layer
     │
     ▼
Transform Layer
     │
     ▼
Generic Dimension Loader
     │
     ├────────► dim_customer (SCD Type 2)
     ├────────► dim_product
     ├────────► dim_region
     └────────► dim_date
                     │
                     ▼
             Surrogate Key Lookup
                     │
                     ▼
                fact_sales
                     │
                     ▼
             MySQL Data Warehouse
```

---

#  Star Schema

                 dim_customer
                      │
                      │
dim_product ───── fact_sales ───── dim_region
                      │
                      │
                  dim_date

## Dimension Tables

- dim_customer
- dim_product
- dim_region
- dim_date

## Fact Table

- fact_sales

---

#  ETL Pipeline

The ETL process performs the following steps:

1. Extract CSV files
2. Validate required columns
3. Remove duplicate records
4. Handle missing values
5. Clean string columns
6. Convert date columns
7. Load dimension tables
8. Generate date dimension
9. Lookup surrogate keys
10. Load fact table
11. Write execution logs

---

#  Features

- End-to-End ETL Pipeline
- Star Schema Data Warehouse
- Generic Dimension Loader
- Surrogate Key Mapping
- Slowly Changing Dimension (Type 2)
- Logging
- Modular Project Structure
- Reusable Components

---

#  Data Validation

The pipeline validates:

- Required columns
- Missing values
- Duplicate records
- Date conversion
- String cleaning

---

#  Logging

Execution logs are stored in:

```
logs/etl.log
```

Example:

```
Database Connected Successfully.
Loaded dim_customer (10 records)
Loaded dim_product (10 records)
Loaded dim_region (7 records)
Loaded fact_sales (10 records)
```

---

#  How to Run

## Clone Repository

```bash
git clone <repository-url>
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Create Database

```sql
CREATE DATABASE retail_dw;
```

---

## Execute SQL

Run:

```
sql/create_tables.sql
```

---

## Configure Database

Update:

```
src/config.py
```

---

## Run ETL

```bash
python -m src.main
```

---

#  Learning Outcomes

This project demonstrates:

- Python Programming
- Object-Oriented Programming
- Pandas Data Processing
- SQLAlchemy
- Data Warehousing
- Star Schema
- ETL Design
- SCD Type 2
- Logging
- MySQL Integration

---

#  Future Enhancements

- Apache Airflow Scheduling
- PySpark ETL
- Incremental Loading
- Docker Support
- Unit Tests
- CI/CD Pipeline

---

#  Author

Snehal Dhagadi

Data Engineer

Thank you!
