SELECT DISTINCT 
    email 
FROM (
    SELECT 
        row_number() over (partition by email order by email) row, 
        email 
    FROM 
        person
    ) f 
WHERE 
    row > 1 