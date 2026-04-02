/* Write your T-SQL query statement below */
SELECT player_id, event_date as first_login from (
SELECT *, row_number() over (partition by player_id ORDER BY event_date asc) row_num FROM Activity) temp where row_num = 1 