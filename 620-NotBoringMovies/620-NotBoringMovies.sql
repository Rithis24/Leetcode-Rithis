-- Last updated: 8/12/2026, 11:49:06 AM
SELECT *
FROM Cinema
WHERE id % 2 = 1
  AND description <> 'boring'
ORDER BY rating DESC;
