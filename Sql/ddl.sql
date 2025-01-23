CREATE TABLE fact_table (
    transaction_id INT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    quantity INT,
    transaction_date DATE
);