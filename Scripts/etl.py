import pandas as pd

def clean_data():
    # Load raw data
    customers = pd.read_csv("data/raw/customers.csv")
    products = pd.read_csv("data/raw/products.csv")
    transactions = pd.read_csv("data/raw/transactions.csv")

    # Data Cleaning
    customers.dropna(inplace=True)
    products.dropna(inplace=True)
    transactions.dropna(inplace=True)

    # Save cleaned data
    customers.to_csv("data/processed/customers_cleaned.csv", index=False)
    products.to_csv("data/processed/products_cleaned.csv", index=False)
    transactions.to_csv("data/processed/transactions_cleaned.csv", index=False)

if __name__ == "__main__":
    clean_data()