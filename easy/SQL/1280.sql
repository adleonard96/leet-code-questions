/* Write your T-SQL query statement below */
with exam_counts as (SELECT student_id, count(*) as attended_exams, subject_name from Examinations group by student_id, subject_name)

SELECT 
    s.student_id, 
    s.student_name, 
    sub.subject_name ,
    case
        when attended_exams is null then 0
        else attended_exams
    end attended_exams
from 
    Students s 
cross JOIN 
    Subjects sub 
LEFT JOIN 
    exam_counts e 
        on 
        s.student_id = e.student_id
        AND
        sub.subject_name = e.subject_name
ORDER BY 
    student_id asc, subject_name asc