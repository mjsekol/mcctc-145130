-- profile.sql . Lab M04-03 starter
--
-- Questions asked of the staging tables, before a single cleaning rule is
-- written. This file is the Measure step of the performance task.
--
-- Each query is introduced by a comment line holding the word QUERY, a colon,
-- and its title. profile.py splits the file on those lines and runs them in order.
--
-- Nothing here changes any data. Profiling is read only on purpose: the point is
-- to find out what the files say, not to start deciding what they should say.
--
-- The first five are written for you. The nine after them are yours.

-- QUERY: How many rows did each file give us
SELECT 'stg_loans' AS staging_table, COUNT(*) AS rows FROM stg_loans
UNION ALL SELECT 'stg_members', COUNT(*) FROM stg_members
UNION ALL SELECT 'stg_items', COUNT(*) FROM stg_items;

-- QUERY: Rows that are a repeated header, not data
SELECT source_row, loan_id, member_id, item_id
FROM stg_loans
WHERE loan_id = 'loan_id';

-- QUERY: Loan ids that appear more than once
SELECT loan_id, COUNT(*) AS copies, group_concat(source_row, ', ') AS on_lines
FROM stg_loans
WHERE loan_id <> 'loan_id'
GROUP BY loan_id
HAVING COUNT(*) > 1;

-- QUERY: Every shape a member id was typed in
SELECT member_id AS typed, COUNT(*) AS rows
FROM stg_loans
WHERE loan_id <> 'loan_id'
GROUP BY member_id
ORDER BY member_id;

-- QUERY: The same member ids after one normalizing expression
SELECT 'RC-' || substr(replace(replace(upper(trim(member_id)), '-', ''), ' ', ''), 3)
           AS normalized,
       COUNT(*) AS rows,
       COUNT(DISTINCT member_id) AS shapes_it_was_typed_in
FROM stg_loans
WHERE loan_id <> 'loan_id'
GROUP BY normalized
HAVING COUNT(DISTINCT member_id) > 1;


-- Nine questions to write. Keep each title line exactly as it is, write the SQL
-- under it, and end each one with a semicolon.

-- QUERY: What is actually in the returned column
-- TODO
SELECT 'not written yet' AS answer;

-- QUERY: Dates in the checked_out column, by shape
-- TODO
SELECT 'not written yet' AS answer;

-- QUERY: Orphan members, the naive way, joining the raw text
-- TODO
SELECT 'not written yet' AS answer;

-- QUERY: Orphan members, normalizing both sides first
-- TODO
SELECT 'not written yet' AS answer;

-- QUERY: Orphan items, normalizing both sides
-- TODO
SELECT 'not written yet' AS answer;

-- QUERY: Dates that contradict each other
-- TODO
SELECT 'not written yet' AS answer;

-- QUERY: Program names in the member file
-- TODO
SELECT 'not written yet' AS answer;

-- QUERY: How many tags each item carries, still as text
-- TODO
SELECT 'not written yet' AS answer;

-- QUERY: Items nothing borrowed
-- TODO
SELECT 'not written yet' AS answer;

