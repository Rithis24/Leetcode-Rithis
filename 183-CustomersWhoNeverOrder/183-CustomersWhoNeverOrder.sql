-- Last updated: 8/12/2026, 11:50:34 AM
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId
    FROM Orders
);
