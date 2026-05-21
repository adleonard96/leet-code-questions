/* Write your T-SQL query statement below */
SELECT round((cast(sum(immediate_delv) as float) / count(*)) * 100 , 2) immediate_percentage  from (
    SELECT *, 
        min(order_date) over (partition by customer_id) first_delv,
        case 
            when order_date = customer_pref_delivery_date then 1
            else 0
        end immediate_delv 
    from delivery) f 
where first_delv = order_date