/* Write your T-SQL query statement below */
SELECT distinct
    query_name, 
    round(sum(cast(rating as float) / position) over (partition by query_name)/ cast(count(*) over (partition by query_name) as float), 2) quality,
    round((cast(sum(
    case when rating < 3 then 1
    else 0
    end) over (partition by query_name) as float) / count(*) over (partition by query_name)) * 100, 2) poor_query_percentage
from queries  