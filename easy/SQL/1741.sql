/* Write your T-SQL query statement below */
select distinct event_day day, emp_id, sum(out_time - in_time) over (partition by emp_id, event_day ) total_time from employees
