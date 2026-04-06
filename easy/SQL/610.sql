/* Write your T-SQL query statement below */
SELECT 
    x, 
    y, 
    z
    ,
    CASE 
        WHEN x + y > z AND z >= x AND z >= y THEN 'Yes'
        WHEN x + z > y AND y >= x AND y >= z THEN 'Yes'
        WHEN y + z > x AND x >= z AND x >= y THEN 'Yes'
        ELSE 'No'
    END as triangle
from Triangle