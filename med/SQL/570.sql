/* Write your T-SQL query statement below */
Select name from employee where id in (
SELECT distinct managerId from (
SELECT count(*) over (partition by managerId) reportee_count, managerId from employee) f where reportee_count >= 5)