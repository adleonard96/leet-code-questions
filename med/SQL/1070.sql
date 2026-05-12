/* Write your T-SQL query statement below */
select product_id, first_year, quantity, price from (
SELECT product_id,year, min(year) over (partition by product_id) first_year, quantity, price from sales) f where year = first_year