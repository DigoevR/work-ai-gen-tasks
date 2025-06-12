SELECT AVG(amount) AS avg_order_value_last3months
FROM orders
WHERE order_date >= '2024-01-01' AND order_date <= '2024-03-31'; 