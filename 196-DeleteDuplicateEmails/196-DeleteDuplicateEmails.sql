-- Last updated: 8/12/2026, 11:50:19 AM
DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
AND p1.id > p2.id;