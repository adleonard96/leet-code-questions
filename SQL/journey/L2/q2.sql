SELECT class from (
SELECT COUNT(student) number_of_student, class from Courses group by class) sub where number_of_student >= 5