-- Last updated: 8/12/2026, 11:47:18 AM
SELECT
    u.name,
    SUM(t.amount) AS balance
FROM
    Users u
JOIN
    Transactions t ON u.account = t.account
GROUP BY
    u.account, u.name
HAVING
    balance > 10000;