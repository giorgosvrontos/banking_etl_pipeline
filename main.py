import os
from dotenv import load_dotenv
from extract import DataExtractor
from transform import DataTransformer
from load_to_postgres import DataLoader


def main():
    load_dotenv()
    db_url = f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASS')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"

    extractor = DataExtractor()
    transformer = DataTransformer()
    loader = DataLoader(db_url)

    try:
        # extraction
        
        customers_df, customer_type_df, transactions_df, transactions_type_df, dim_accounts = extractor.get_raw_data()

        # transformation
        
        clean_customer = transformer.process_customers(customers_df, customer_type_df)
        clean_transactions = transformer.process_transactions(transactions_df, transactions_type_df)
        clean_account = transformer.process_accounts(dim_accounts)


        # load 
        loader.setup_database()
        
        
        loader.load_data(clean_customer, clean_account, clean_transactions)

        print("Successful load.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()