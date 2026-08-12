-- Last updated: 8/12/2026, 11:47:47 AM
(
    SELECT U.name AS results
    FROM Users U
    JOIN MovieRating MR ON U.user_id = MR.user_id
    GROUP BY U.user_id, U.name
    ORDER BY COUNT(MR.movie_id) DESC, U.name ASC
    LIMIT 1
)
UNION ALL
(
    SELECT M.title AS results
    FROM Movies M
    JOIN MovieRating MR ON M.movie_id = MR.movie_id
    WHERE MR.created_at BETWEEN '2020-02-01' AND '2020-02-29'
    GROUP BY M.movie_id, M.title
    ORDER BY AVG(MR.rating) DESC, M.title ASC
    LIMIT 1
);