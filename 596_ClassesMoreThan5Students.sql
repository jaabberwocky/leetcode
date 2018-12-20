#URL: https://leetcode.com/problems/classes-more-than-5-students/description/
#Desc:  There is a table courses with columns: student and class

#Please list out all classes which have more than or equal to 5 students.

#For example, the table: 

SELECT class 
FROM courses 
GROUP BY class 
HAVING COUNT(DISTINCT student) >= 5;