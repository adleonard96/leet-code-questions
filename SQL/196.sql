/* Write your T-SQL query statement below */
DELETE FROM 
    person 
where id in (
    SELECT id FROM (
        SELECT 
            min(id) over (Partition by email) minId, 
            id 
        from person ) f where id <> minId)
