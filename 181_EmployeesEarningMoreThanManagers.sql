#URL:https://leetcode.com/problems/employees-earning-more-than-their-managers/description/
#Desc: The Employee table holds all employees including their managers. Every employee has an Id, and there is also a column for the manager Id.
# Given the Employee table, write a SQL query that finds out employees who earn more than their managers. For the above table, Joe is the only employee who earns more than his manager.

SELECT e1.Name as Employee
FROM Employee as e1
LEFT JOIN Employee as e2
ON e1.ManagerId = e2.Id
WHERE e1.Salary > e2.Salary;