-- https://www.codewars.com/kata/5811501c2d35672d4f000146/train/sql

-- Create your SELECT statement here

-- get all sales with price over $90
-- check whether any departments are in the first table

WITH special_sales as (
  SELECT department_id
  FROM sales
  WHERE price > 90.00
)

SELECT d.id, d.name
FROM departments as d
WHERE d.id IN (SELECT DISTINCT department_id FROM special_sales)