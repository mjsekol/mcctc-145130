-- schema.sql . Lab M04-01 solution
--
-- Three tables out of one flat file.
--
-- players       one row per person. The gamertag is the key, because it is the
--               thing that never changes. The name is typed by a human and is
--               spelled two different ways in the source file.
-- matches       one row per match. (played_on, opponent) is unique, because the
--               team does not play the same school twice on one day.
-- appearances   one row per player per match. This is the junction table, and it
--               is the reason a flat file could not hold this without repeating
--               every match five times.

PRAGMA foreign_keys = ON;

DROP TABLE IF EXISTS appearances;
DROP TABLE IF EXISTS matches;
DROP TABLE IF EXISTS players;

CREATE TABLE players (
    gamertag    TEXT PRIMARY KEY,
    player_name TEXT NOT NULL,
    grade_level INTEGER NOT NULL CHECK (grade_level BETWEEN 9 AND 12)
);

CREATE TABLE matches (
    match_id    INTEGER PRIMARY KEY,
    played_on   TEXT NOT NULL,
    opponent    TEXT NOT NULL,
    game_title  TEXT NOT NULL,
    our_score   INTEGER NOT NULL CHECK (our_score >= 0),
    their_score INTEGER NOT NULL CHECK (their_score >= 0),
    UNIQUE (played_on, opponent)
);

CREATE TABLE appearances (
    match_id INTEGER NOT NULL REFERENCES matches (match_id) ON DELETE CASCADE,
    gamertag TEXT NOT NULL REFERENCES players (gamertag) ON DELETE RESTRICT,
    role     TEXT NOT NULL,
    kills    INTEGER NOT NULL CHECK (kills >= 0),
    deaths   INTEGER NOT NULL CHECK (deaths >= 0),
    PRIMARY KEY (match_id, gamertag)
);
