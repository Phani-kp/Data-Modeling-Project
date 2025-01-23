import psycopg2
import pandas as pd

def load_data_to_db():
    conn = psycopg2.connect(
        dbname="bigdata_db", user="user", password="password", host="localhost", port="5432"
    )
    cursor = conn.cursor()

    # Load fact table
    fact_table = pd.read_parquet("data/processed/modeled_data/fact_table.parquet")
    for _, row in fact_table.iterrows():
        cursor.execute(
            """
            INSERT INTO fact_table (transaction_id, customer_id, product_id, quantity, transaction_date)
            VALUES (%s, %s, %s, %s, %s)
            """,
            (row.transaction_id, row.customer_id, row.product_id, row.quantity, row.transaction_date)
        )

    conn.commit()
    conn.close()

if __name__ == "__main__":
    load_data_to_db()