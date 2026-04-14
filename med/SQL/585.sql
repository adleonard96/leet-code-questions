# Write your MySQL query statement below
SELECT round(sum(tiv_2016), 2) tiv_2016 FROM (
SELECT *, count(*) over (partition by lat, lon) location_count, count(*) over (partition by tiv_2015) tiv_count from Insurance) f where location_count = 1 and tiv_count > 1