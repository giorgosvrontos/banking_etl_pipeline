# Data Cleaning Rules Applied

During the Transformation phase (`transform.py`), the following data cleaning and shaping rules were enforced on the raw datasets:

## 1. Customers Table (`dim_customer`)
* **Joins:** Merged `customers` with `customer_types` to denormalize the customer type name.
* **Null Imputation:** Replaced missing `FirstName` and `LastName` values with 'Unknown'.
* **Calculated Columns:** Created a clean `FullName` column. If both names were missing, a fallback format `Customer_{ID}` was generated.
* **Data Type Enforcement:** Converted `DateOfBirth` to a strict Date format. Missing or corrupted dates were filled with a default outlier date (`1900-01-01`) to maintain column integrity.

## 2. Accounts Table (`dim_account`)
* **Column Dropping:** Removed irrelevant columns (`AccountTypeID`, `AccountStatusID`) that are not needed for the final schema.
* **Date Standardization:** Standardized `OpeningDate`. Replaced NaT values with `1900-01-01`.

## 3. Transactions Table (`fact_transactions`)
* **Joins:** Merged with `transaction_types` to include the `type_name` directly in the fact table.
* **Missing Dates:** Imputed missing transaction timestamps with a meaningful default (`1900-01-01 00:00:00`).

## 4. General Shaping (Applied to All)
* **Naming Conventions:** Renamed all columns from PascalCase/CamelCase to `snake_case` to comply with PostgreSQL best practices.
* **Deduplication:** Applied `.drop_duplicates(subset=['id'], keep='first')` strictly based on the Primary Key of each table to ensure no unique constraint violations occur during loading.
