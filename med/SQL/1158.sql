/* Write your T-SQL query statement below */
SELECT DISTINCT 
    user_id buyer_id, 
    join_date, 
    case 
        when orders_in_2019 is null then 0
        else orders_in_2019 
    end orders_in_2019 from users left join (SELECT *, count(*) over (partition by buyer_id) orders_in_2019 FROM orders where order_date between '2019-01-01' and '2019-12-31') orders on users.user_id = orders.buyer_id 
