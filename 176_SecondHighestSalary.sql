# URL: https://leetcode.com/problems/second-highest-salary/description/
# Desc: Write a SQL query to get the second highest salary from the Employee table.

SELECT MAX(Salary) as SecondHighestSalary
    FROM Employee
WHERE Salary < (SELECT MAX(Salary) FROM Employee);