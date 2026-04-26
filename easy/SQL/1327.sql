# Write your MySQL query statement below
SELECT product_name, SUM(unit) unit from orders o 
join products p on o.product_id = p.product_id
where order_date  between '2020-02-01' and '2020-02-29' group by o.product_id having unit >= 100 