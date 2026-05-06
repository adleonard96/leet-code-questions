-- /* Write your T-SQL query statement below */
select * from (
SELECT top 1 name results from (
SELECT count(*) total, user_id from movieRating group by user_id) f join Users on users.user_id = f.user_id order by total desc, name asc) f
UNION ALL
select * from (
SELECT top 1 title results from (
SELECT avg(cast(rating as float))  average, movie_id from MovieRating where created_at between '2020-02-01' and '2020-02-29' group by movie_id) 
f join movies on movies.movie_id = f.movie_id 
order by average desc, title asc) f