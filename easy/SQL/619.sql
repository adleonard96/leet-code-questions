# Write your MySQL query statement below
SELECT MAX(num) num from ( 
SELECT count(num) count, num from MyNumbers group by num having count = 1) f