-- Last updated: 8/12/2026, 11:47:24 AM
SELECT
    patient_id,
    patient_name,
    conditions
FROM
    Patients
WHERE
    conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';