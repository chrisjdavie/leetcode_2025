-- Improved based on other submissions - I forgot how `MAX` works, which isn't great news for interviewing tomorrow...

-- Write your PostgreSQL query statement below
SELECT
    CASE
        WHEN id % 2 = 1 AND id = (SELECT MAX(id) FROM seat) THEN id
        WHEN id % 2 = 1 THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
    END AS id,
    student
FROM seat
ORDER BY id;
