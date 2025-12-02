# Write your MySQL query statement below
SELECT 
    e.name Employee
from 
    employee e 
join 
    employee m 
        on e.managerid = m.id
where
    e.salary > m.salary