# 🏦 Banking Data Warehouse - End-to-End ETL Pipeline

## 👋 Hello!
Welcome to my very first fully automated End-to-End ETL Pipeline! 

This project simulates a real-world Data Engineering scenario. It takes raw, banking data (CSV files from Kaggle "Finance Fraud & Loans Dataset – TestDataBox"), cleans it up, transforms it, and securely loads it into a PostgreSQL database, organizing it into a clean Star Schema. 

I built this project to practice writing production-ready code. That means focusing on clean architecture, data safety, and automation rather than just getting the script to run once.

## The Architecture
I structured the pipeline using **Object-Oriented Programming (OOP)** to keep the code modular, readable, and easy to maintain. The process is broken down into three main classes:

* **`DataExtractor` (Extract):** Safely reads the raw data from local files into memory.
* **`DataTransformer` (Transform):** The workhorse of the pipeline. It handles merging tables, imputing missing values (NULLs), standardizing dates, and most importantly, dropping duplicates based on Primary Keys.
* **`DataLoader` (Load):** Connects to the PostgreSQL database using `SQLAlchemy`. It sets up the database architecture (DDL) and pushes the clean DataFrames to the database.

> **💡 Note on Idempotency:** The pipeline is designed to be completely idempotent. Thanks to the use of `TRUNCATE CASCADE` before loading, you can run this script 100 times a day, and it will never create duplicate records or break the database. 

## 🛠️ Tech Stack
* **Language:** Python
* **Data Processing:** Pandas
* **Database Management:** PostgreSQL, SQLAlchemy
* **Security:** `python-dotenv` (to keep database credentials safely hidden out of the source code)

## 🗄️ Database Schema (Star Schema)
The data is structured into a classic Data Warehouse model optimized for querying:
* **Fact Table:** `fact_transactions` (Records every movement of money)
* **Dimension Tables:** `dim_customer` (Customer details), `dim_account` (Account details linked to customers)

## 🚀 How to Run It Yourself
If you want to clone this repo and try it out:

1. Clone the repository to your local machine.
2. Place the raw CSV files inside the `data/` folder (not included in the repo for privacy reasons).
3. Create a file named exactly `.env` in the root directory and add your database credentials like this:
   ```text
   DB_USER=your_postgres_username
   DB_PASS=your_password
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=your_database_name
