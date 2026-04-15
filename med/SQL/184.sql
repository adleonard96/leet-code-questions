/* Write your T-SQL query statement below */
SELECT 
    d.name Department, 
    ranked.name Employee, 
    Salary 
from ( 
    SELECT 
        *, 
        dense_rank() over (partition by departmentId order by salary desc) salary_rank 
    FROM 
        Employee e ) ranked join Department d on ranked.departmentId = d.id
where
    salary_rank = 1