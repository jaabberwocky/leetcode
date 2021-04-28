-- https://www.codewars.com/kata/55f73be6e12baaa5900000d4/train/sql

-- you will be given a table, goals, with columns la_liga_goals, copa_del_rey_goals, and champions_league_goals. Return a table with a column, res.

select (la_liga_goals + copa_del_rey_goals + champions_league_goals) as res from goals