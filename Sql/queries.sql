-- Total sales by product category
SELECT category, SUM(price * quantity) AS total_sales
FROM fact_table
GROUP BY category;

-- Top customers by revenue
SELECT customer_id, SUM(price * quantity) AS total_revenue
FROM fact_table
GROUP BY customer_id
ORDER BY total_revenue DESC
LIMIT 10;

-- Monthly sales trends
SELECT DATE_TRUNC('month', transaction_date) AS month, SUM(price * quantity) AS total_sales
FROM fact_table
GROUP BY month
ORDER BY month;