-- /* Write your T-SQL query statement below */
SELECT id, 'Root' as type from Tree where p_id is null
UNION
select id, 'Inner' as type from Tree where id in (select distinct p_id from Tree) and id not in (select id from Tree where p_id is null)
UNION 
select id, 'Leaf' as type from Tree where id not in (select distinct p_id from tree where p_id is not null) and id not in (select id from Tree where p_id is null)