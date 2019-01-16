#URL: https://leetcode.com/problems/customers-who-never-order/description/
#Desc: Suppose that a website contains two tables, the Customers table and the Orders table. Write a SQL query to find all customers who never order anything. Using the above tables as example, return the following:

SELECT c.Name as Customers
    FROM Customers as C
    WHERE c.Id NOT IN
    (SELECT o.CustomerId
        FROM Orders as o);