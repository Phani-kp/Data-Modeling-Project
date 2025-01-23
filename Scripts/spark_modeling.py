from pyspark.sql import SparkSession

def process_data():
    spark = SparkSession.builder.appName("DataModeling").getOrCreate()

    # Load data
    customers = spark.read.csv("data/processed/customers_cleaned.csv", header=True, inferSchema=True)
    products = spark.read.csv("data/processed/products_cleaned.csv", header=True, inferSchema=True)
    transactions = spark.read.csv("data/processed/transactions_cleaned.csv", header=True, inferSchema=True)

    # Create fact and dimension tables
    fact_table = transactions.join(customers, "customer_id").join(products, "product_id")
    fact_table.write.parquet("data/processed/modeled_data/fact_table.parquet")

if __name__ == "__main__":
    process_data()