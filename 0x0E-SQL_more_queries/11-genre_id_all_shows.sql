-- Lists all shows contained in the database hbtn_0d_tvshows.
-- Displays NULL for shows without genres.
-- Results are ordered by tv_shows.title and tv_show_genres.genre_id.
-- ascending order.
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
