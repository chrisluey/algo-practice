# Write your MySQL query statement below
SELECT c.name AS "Customers" FROM customers c WHERE c.id NOT IN (SELECT DISTINCT o.customerid FROM  orders o)