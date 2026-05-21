/* Write your T-SQL query statement below */
SELECT product_id, new_price price FROM (
SELECT *, max(change_date) over (partition by product_id) max_date from products 
where change_date <= '2019-08-16') f where change_date = max_date 
UNION 
SELECT product_id,  10 price from  products where product_id not in (select product_id from products where change_date <= '2019-08-16')