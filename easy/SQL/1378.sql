/* Write your T-SQL query statement below */
SELECT unique_id, name From Employees e left join EmployeeUNI eu on e.id = eu.id 