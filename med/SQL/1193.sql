/* Write your T-SQL query statement below */
with date_trunk as 
    ( 
        select left(cast(trans_date as nvarchar), 7) month, 
        case 
            WHEN country is null THEN 'null'
            ELSE country
        end country, 
        state, 
        amount 
    from transactions),
approved as (select DISTINCT 
            country, 
            month, 
            count(*) over (partition by month, country) approved_count, 
            sum(amount) over (partition by month, country) as approved_total_amount 
        from 
            date_trunk 
        where 
            state = 'approved')

SELECT DISTINCT 
    total.month, 
    case
        when total.country = 'null' then null
        else total.country
    end country, 
    count(*) over (partition by total.month, total.country) 
    trans_count, 
    case 
        when approved_count is null THEN 0
        ELSE approved_count
    END as approved_count, 
    sum(amount) over (partition by total.month, 
    total.country) trans_total_amount, 
    case
        when approved_total_amount is null THEN 0
        ELSE approved_total_amount
    END as approved_total_amount
from 
    date_trunk as total
    LEFT JOIN approved on total.country = approved.country and total.month = approved.month
    