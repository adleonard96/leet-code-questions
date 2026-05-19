/* Write your T-SQL query statement below */
SELECT id, visit_date, people from (
SELECT 
    id, 
    visit_date, 
    people, 
    lead(people, 1, 0) over (order by visit_date) day2, 
    lead(people, 2, 0) over (order by visit_date) day3,
    lag(people, 1, 0) over (order by visit_date) nday2, 
    lag(people, 2, 0) over (order by visit_date) nday3
from 
    stadium) f where 
        (people >= 100 and day2 >= 100 and day3 >= 100)
        or 
        (people >= 100 and nday2 >= 100 and day2 >= 100)
        or
        (people >= 100 and nday2 >= 100 and nday3 >= 100)