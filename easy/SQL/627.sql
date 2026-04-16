/* Write your T-SQL query statement below */
UPDATE Salary set sex = CASE
    WHEN sex = 'f' then 'm'
    else 'f'
END