/* Write your T-SQL query statement below */
with product_count as (select count(*) as count from product)

SELECT customer_id from (
    SELECT count(*) count, customer_id from (
        SELECT DISTINCT customer_id, product_key from customer) f group by customer_id
        ) g
    JOIN product_count pc on g.count = pc.count 
