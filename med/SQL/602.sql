/* Write your T-SQL query statement below */
SELECT top 1 * FROM (
SELECT id, COUNT(*) num  FROM (
SELECT requester_id id from requestaccepted
UNION ALL
SELECT accepter_id id from requestaccepted) f group by id) f order by num desc