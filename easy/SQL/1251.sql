# Write your MySQL query statement below
SELECT DISTINCT product_id, round(sum(purchase_price) over (partition by product_id) / sum(units) over (partition by product_id), 2) average_price  from (
SELECT
    p.product_id,
    case 
        when purchase_date between start_date and end_date then price * units
        else null
    end purchase_price,
    price,
    units
from 
    prices p
    left join unitsSold us
    on p.product_id = us.product_id) f where purchase_price is not null
UNION
SELECT DISTINCT prices.product_id, 0 as average_price from prices left join unitsSold on unitsSold.product_id = prices.product_id where purchase_date is null