CREATE SCHEMA IF NOT EXISTS banking_dw;
SET search_path TO banking_dw;

DROP TABLE IF EXISTS banking_dw.fact_transactions CASCADE;
DROP TABLE IF EXISTS banking_dw.dim_account CASCADE;
DROP TABLE IF EXISTS banking_dw.dim_customer CASCADE;

CREATE TABLE dim_customer (
    customer_id INTEGER PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    date_of_birth DATE,
    address_id INTEGER,
    customer_type_id INTEGER,
    customer_type_name VARCHAR(50),
    full_name VARCHAR(200)
);

CREATE TABLE dim_account (
    account_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    balance DECIMAL(15, 2),
    opening_date DATE,
    CONSTRAINT fk_customer FOREIGN KEY (customer_id) REFERENCES dim_customer (customer_id)
);

CREATE TABLE fact_transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_origin_id INTEGER,
    account_destination_id INTEGER,
    transaction_type_id INTEGER,
    amount DECIMAL(15, 2),
    transaction_date TIMESTAMP,
    type_name VARCHAR(50),
    CONSTRAINT fk_origin_account FOREIGN KEY (account_origin_id) REFERENCES dim_account (account_id),
    CONSTRAINT fk_dest_account FOREIGN KEY (account_destination_id) REFERENCES dim_account (account_id)
);
