with base_query as (SELECT 
    request_at,
    case 
        when status = 'completed' then 'false'
        else 'true'
    end canceled   
FROM 
    Trips t join users d on d.users_id = t.driver_id join users c on c.users_id = t.client_id  where c.banned = 'No' and d.banned = 'No' and request_at between '2013-10-01' and '2013-10-03')

/* Write your T-SQL query statement below */
SELECT distinct
    tot.request_at Day, 
    case when f.canceled is null then 0.00 else
    round(f.canceled/ count(*) over (partition by tot.request_at), 2) 
    end  'Cancellation Rate'
from 
    base_query tot
left join (
    select distinct
        base_query.request_at, 
        cast(count(*) over (partition by base_query.request_at) as float) canceled 
    from base_query 
        where canceled = 'true') f on tot.request_at = f.request_at