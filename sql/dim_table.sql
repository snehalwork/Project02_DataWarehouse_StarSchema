CREATE DATABASE IF NOT EXISTS retail_dw;

USE retail_dw;

-- dim_customer
CREATE TABLE dim_customer (
    customer_key INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    gender VARCHAR(20),
    city VARCHAR(50),
    email VARCHAR(100),
    created_date DATE,
    start_date DATE,
    end_date DATE,
    is_current CHAR(1)
);

--dim_product
CREATE TABLE dim_product (
    product_key INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    product_name VARCHAR(100),
    category VARCHAR(50),
    brand VARCHAR(50),
    price DECIMAL(10,2)
);

--dim_region
CREATE TABLE dim_region (
    region_key INT AUTO_INCREMENT PRIMARY KEY,
    region_id INT,
    region_name VARCHAR(50),
    state VARCHAR(50),
    country VARCHAR(50)
);