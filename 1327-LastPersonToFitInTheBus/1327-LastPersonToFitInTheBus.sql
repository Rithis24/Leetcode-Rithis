-- Last updated: 8/12/2026, 11:48:03 AM
# Write your MySQL query statement below
SELECT person_name
FROM (
    SELECT
        person_name,
        SUM(weight) OVER (ORDER BY turn) AS total_weight
    FROM Queue
) AS q
WHERE total_weight <= 1000
ORDER BY total_weight DESC
LIMIT 1;