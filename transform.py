import pandas as pd

class DataTransformer:
    def process_customers(self, customers_df, customer_type_df):
        dim_customer = pd.merge(customers_df, customer_type_df, how='inner', on='CustomerTypeID')
        first_name = dim_customer['FirstName'].fillna('')
        last_name = dim_customer['LastName'].fillna('')
        dim_customer['FullName'] = (first_name + ' ' + last_name).str.strip()
        
        dim_customer['FirstName'] = dim_customer['FirstName'].fillna('Unknown')
        dim_customer['LastName'] = dim_customer['LastName'].fillna('Unknown')
        
        is_empty = dim_customer['FullName'] == ''
        dim_customer.loc[is_empty, 'FullName'] = 'Customer_' + dim_customer.loc[is_empty, 'CustomerID'].astype(str)
        
        dim_customer['DateOfBirth'] = pd.to_datetime(dim_customer['DateOfBirth'], errors='coerce').dt.date
        default_date = pd.Timestamp('1900-01-01').date()
        dim_customer['DateOfBirth'] = dim_customer['DateOfBirth'].fillna(default_date)

        rename_mapping = {
            'CustomerID': 'customer_id',
            'FirstName': 'first_name',
            'LastName': 'last_name',
            'DateOfBirth': 'date_of_birth',
            'AddressID': 'address_id',
            'CustomerTypeID': 'customer_type_id',
            'TypeName': 'customer_type_name',
            'FullName': 'full_name'
        }
        dim_customer = dim_customer.rename(columns=rename_mapping)
        
         
        dim_customer = dim_customer.drop_duplicates(subset=['customer_id'], keep='first')
        return dim_customer

    def process_transactions(self, transactions_df, transactions_type_df):
        transactions_df = transactions_df.drop(columns=['BranchID', 'Description'])
        fact_transactions = pd.merge(transactions_df, transactions_type_df, how='inner', on='TransactionTypeID')
        
        rename_transactions = {
            'TransactionID': 'transaction_id',
            'AccountOriginID': 'account_origin_id',
            'AccountDestinationID': 'account_destination_id',
            'TransactionTypeID': 'transaction_type_id',
            'Amount': 'amount',
            'TransactionDate': 'transaction_date',
            'TypeName': 'type_name'
        }
        fact_transactions = fact_transactions.rename(columns=rename_transactions)
        fact_transactions['transaction_date'] = pd.to_datetime(fact_transactions['transaction_date'], errors='coerce')
        meaningful_default = pd.to_datetime('1900-01-01 00:00:00')
        fact_transactions['transaction_date'] = fact_transactions['transaction_date'].fillna(meaningful_default)
        
         
        fact_transactions = fact_transactions.drop_duplicates(subset=['transaction_id'], keep='first')
        return fact_transactions

    def process_accounts(self, dim_accounts):
        dim_accounts = dim_accounts.drop(columns=['AccountTypeID', 'AccountStatusID'])
        
        rename_accounts = {
            'AccountID': 'account_id',
            'CustomerID': 'customer_id',
            'Balance': 'balance',
            'OpeningDate': 'opening_date'
        }
        dim_account = dim_accounts.rename(columns=rename_accounts)
        dim_account['opening_date'] = pd.to_datetime(dim_account['opening_date'], errors='coerce')
        default_date = pd.to_datetime('1900-01-01')
        dim_account['opening_date'] = dim_account['opening_date'].fillna(default_date)
        dim_account['opening_date'] = dim_account['opening_date'].dt.date
        
         
        dim_account = dim_account.drop_duplicates(subset=['account_id'], keep='first')
        return dim_account

   