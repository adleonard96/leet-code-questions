/* Write your T-SQL query statement below */
SELECT name, sum(amount) balance from users u join transactions t on t.account = u.account group by name having sum(amount) > 10000 