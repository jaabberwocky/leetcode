#URL: https://leetcode.com/problems/combine-two-tables/description/
#Desc: Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:

SELECT p.FirstName, p.LastName, a.City, a.State 
	FROM Person as p 
	LEFT JOIN Address as a 
		ON p.PersonId = a.PersonId;
