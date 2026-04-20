/* Write your T-SQL query statement below */
SELECT distinct director_id, actor_id from (
SELECT COUNT(*) over (partition by actor_id, director_id) coop, director_id, actor_id from ActorDirector) f where coop >= 3