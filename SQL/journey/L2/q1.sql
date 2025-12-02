# Write your MySQL query statement below
SELECT  customer_number FROM (
SELECT count(order_number) num_of_orders, customer_number from orders group by customer_number ) f order by num_of_orders desc LIMIT 1