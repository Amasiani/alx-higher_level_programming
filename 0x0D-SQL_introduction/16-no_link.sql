-- Lists all records of the table second_table having a name value.
-- Ordered by score descending order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
