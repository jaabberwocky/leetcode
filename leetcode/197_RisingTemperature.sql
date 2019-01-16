#URL: https://leetcode.com/problems/rising-temperature/description/
#Desc: Given a Weather table, write a SQL query to find all dates' Ids with higher temperature compared to its previous (yesterday's) dates.

SELECT t1.Id
    FROM Weather as t1, Weather as t2
    WHERE t1.Temperature > t2.Temperature
    AND TO_DAYS(t1.RecordDate) = TO_DAYS(t2.RecordDate) + 1;