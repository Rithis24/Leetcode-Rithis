-- Last updated: 8/12/2026, 11:47:44 AM
SELECT
    eu.unique_id,
    e.name
FROM
    Employees AS e
LEFT JOIN
    EmployeeUNI AS eu ON e.id = eu.id;