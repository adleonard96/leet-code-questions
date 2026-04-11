with row_cte as (select id, temperature, recordDate, row_number() over (order by recordDate asc) rowNum from weather)

SELECT curr.id from row_cte curr join row_cte prev on  curr.rowNum = prev.rowNum + 1 
where curr.temperature > prev.temperature and datediff(day, prev.recordDate, curr.recordDate) = 1