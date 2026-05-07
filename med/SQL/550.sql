/* Write your T-SQL query statement below */
SELECT round(day_after_count / user_count, 2) fraction FROM
    (SELECT 
        cast(count(*) as float) day_after_count  
    From (
        SELECT 
            *, 
            lead(event_date, 1) over (partition by player_id order by event_date) next, 
            min(event_date) over (partition by player_id) first_login
        from 
            activity) f 
        where event_date = dateadd(day, -1, next) and event_date = first_login) f
    cross join (Select count(*) as user_count from (SELECT DISTINCT player_id from activity) d) d