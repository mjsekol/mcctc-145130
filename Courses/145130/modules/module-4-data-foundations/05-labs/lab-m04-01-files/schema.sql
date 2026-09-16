-- schema.sql . Lab M04-01 starter
--
-- One table is written for you, as the worked example. Two are yours.
-- Every table needs a primary key. Every relationship needs a REFERENCES clause.
-- Write a comment above each table saying why it is shaped that way.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS appearances;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;

-- players: one row per person.
-- The gamertag is the key because it is the value that never changes. The name
-- is typed by a person, and in this file it is typed two different ways for one
-- of the players.
CREATE TABLE players (
    gamertag    TEXT PRIMARY KEY,
    player_name TEXT NOT NULL,
    grade_level INTEGER NOT NULL CHECK (grade_level BETWEEN 9 AND 12)
);

-- TODO step 4: matches. One row per match.
-- Decide the key. Decide what combination of columns must be unique, and say why
-- in a comment. Add a CHECK that a score cannot be negative.
-- CREATE TABLE matches (
-- );

-- TODO step 5: appearances. One row per player per match.
-- This is the junction table. Its primary key is two columns together.
-- Both of those columns are also foreign keys.
-- CREATE TABLE appearances (
-- );
