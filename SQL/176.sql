/* Write your T-SQL query statement below */
DECLARE @dist_salaries int;
Select @dist_salaries = COUNT(*) FROM
(Select distinct salary from employee) f

if @dist_salaries < 2 
Begin 
    SELECT null as SecondHighestSalary
END
ELSE 
begin
    select top 1 salary as SecondHighestSalary from (
    SELECT DISTINCT top 2 salary from employee order by salary desc) f order by salary asc
end 
