CREATE FUNCTION getNthHighestSalary(@N INT) RETURNS INT AS
BEGIN
    RETURN (
        /* Write your T-SQL query statement below. */
        SELECT DISTINCT salary from (
        SELECT DENSE_rank() over (order by salary desc) sal_rank, salary from Employee) f where sal_rank = @N
    );
END