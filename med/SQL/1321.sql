SELECT visited_on, SUM(amount) over (order by visited_on rows between 6 preceding and current row) amount, round(SUM(amount) over (order by visited_on rows between 6 preceding and current row) / 7.0, 2) average_amount from
(SELECT DISTINCT visited_on, sum(amount) over (partition by visited_on) amount from customer) f 
order by visited_on
offset 6 rows