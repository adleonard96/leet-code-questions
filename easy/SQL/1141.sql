/* Write your T-SQL query statement below */
WITH distinct_activity as (SELECT DISTINCT user_id, activity_date from Activity where activity_date between DATEADD(day, -29, '2019-07-27') and '2019-07-27'  )

SELECT activity_date day, count(*) active_users  FROM distinct_activity group by activity_date 