-- Last updated: 8/12/2026, 11:50:37 AM
# Write your MySQL query statement below
SELECT
    email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;