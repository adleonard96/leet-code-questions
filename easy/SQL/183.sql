/* Write your T-SQL query statement below */

SELECT name as Customers from customers left  join orders on customers.id = orders.customerId
 where orders.id is null