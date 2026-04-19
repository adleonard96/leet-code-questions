/* Write your T-SQL query statement below */
SELECT DISTINCT 
    name, 
    case 
        when travelled_distance is null then 0
        else travelled_distance
    end travelled_distance from (
    SELECT 
        name, 
        sum(distance) over (partition by user_id) travelled_distance 
    FROM 
        users left join rides on rides.user_id = users.id) f 
order by 
    travelled_distance desc