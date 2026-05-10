/* Write your T-SQL query statement below */
SELECT DISTINCT machine_id, round(avg(next_timestamp - timestamp) over (partition by machine_id), 3) processing_time  from (
SELECT 
    machine_id, 
    process_id, 
    activity_type, 
    timestamp, 
    lead(timestamp, 1) over (order by machine_id, process_id, timestamp) next_timestamp 
from 
    activity) f where activity_type = 'start'