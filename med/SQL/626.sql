/* Write your T-SQL query statement below */
SELECT * FROM (
SELECT 
    case 
        when id % 2 = 0 then id - 1
        when id = max_id then id
        else id + 1
    end id, 
    student
    from seat
cross join ( 
SELECT max(id) max_id from seat) f ) sub order by id