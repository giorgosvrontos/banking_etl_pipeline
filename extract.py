import pandas as pd
class DataExtractor:
    def get_raw_data(self):
        
        customers_df = pd.read_csv("data/customers.csv")
        customer_type_df = pd.read_csv("data/customer_types.csv")
        transactions_df = pd.read_csv("data/transactions.csv")
        transactions_type_df = pd.read_csv("data/transaction_types.csv")
        dim_accounts = pd.read_csv("data/accounts.csv")
        
        return customers_df, customer_type_df, transactions_df, transactions_type_df, dim_accounts