-- Write your PostgreSQL query statement below
SELECT
    CASE
        WHEN id % 2 = 1 AND id IN (SELECT id FROM seat ORDER BY id DESC LIMIT 1) THEN id
        WHEN id % 2 = 1 THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
    END AS id,
    student
FROM seat
ORDER BY id;
