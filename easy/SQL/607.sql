/* Write your T-SQL query statement below */
SELECT 
    name 
from 
    salesPerson 
WHERE 
    name not in (
SELECT 
    sp.name
FROM 
    SalesPerson sp 
    join orders o on o.sales_id = sp.sales_id 
    join company c on o.com_id = c.com_id
WHERE 
    c.name = 'RED')