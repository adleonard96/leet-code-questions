/* Write your T-SQL query statement below */
SELECT DISTINCT
    d.id, 
    Jan_Revenue, 
    Feb_Revenue, 
    Mar_Revenue, 
    Apr_Revenue, 
    May_Revenue, 
    Jun_Revenue, 
    Jul_Revenue, 
    Aug_Revenue, 
    Sep_Revenue, 
    Oct_Revenue,
    Nov_Revenue,
    Dec_Revenue
from department d
LEFT JOIN (SELECT id, sum(revenue) AS 'Jan_Revenue' from department Jan where month = 'Jan' group by id) Jan on d.id = jan.id
LEFT JOIN (SELECT id, sum(revenue) AS 'Feb_Revenue' from department Feb where month = 'Feb' group by id) Feb on d.id = feb.id
LEFT JOIN (SELECT id, sum(revenue) AS 'Mar_Revenue' from department Mar where month = 'Mar' group by id) Mar on d.id = mar.id
LEFT JOIN (SELECT id, sum(revenue) AS 'Apr_Revenue' from department Apr where month = 'Apr' group by id) Apr on d.id = apr.id
LEFT JOIN (SELECT id, sum(revenue) AS 'May_Revenue' from department May where month = 'May' group by id) May on d.id = may.id
LEFT JOIN (SELECT id, sum(revenue) AS 'Jun_Revenue' from department Jun where month = 'Jun' group by id) Jun on d.id = jun.id
LEFT JOIN (SELECT id, sum(revenue) AS 'Jul_Revenue' from department Jul where month = 'Jul' group by id) Jul on d.id = jul.id
LEFT JOIN (SELECT id, sum(revenue) AS 'Aug_Revenue' from department Aug where month = 'Aug' group by id) Aug on d.id = aug.id
LEFT JOIN (SELECT id, sum(revenue) AS 'Sep_Revenue' from department Sep where month = 'Sep' group by id) Sep on d.id = sep.id
LEFT JOIN (SELECT id, sum(revenue) AS 'Oct_Revenue' from department Oct where month = 'Oct' group by id) Oct on d.id = oct.id
LEFT JOIN (SELECT id, sum(revenue) AS 'Nov_Revenue' from department Nov where month = 'Nov' group by id) Nov on d.id = nov.id
LEFT JOIN (SELECT id, sum(revenue) AS 'Dec_Revenue' from department Dec where month = 'Dec' group by id) Dec on d.id = dec.id