SET search_path TO banking_dw;


EXPLAIN analyze
SELECT 
    c.customer_type_name,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.amount) AS total_volume
FROM dim_customer c
JOIN dim_account a ON c.customer_id = a.customer_id
JOIN fact_transactions t ON a.account_id = t.account_origin_id
GROUP BY c.customer_type_name;


