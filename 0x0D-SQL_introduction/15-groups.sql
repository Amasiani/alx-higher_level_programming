-- Lists number of records with the same score in the table second_table.
-- Ordered by count descending order.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
