# Write your MySQL query statement below
SELECT e.name AS "Employee" FROM Employee e JOIN employee m ON e.managerid = m.id WHERE e.salary > m.salary