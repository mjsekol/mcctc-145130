# build_db.py . Lab M04-01 starter
#
# This file runs right now. It does nothing useful yet.
#
#   python build_db.py
#
# What you are building: one flat CSV goes in, three connected tables come out.

import csv
import os
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "esports_flat.csv")
SCHEMA = os.path.join(HERE, "schema.sql")
DATABASE = os.path.join(HERE, "output", "esports.db")


def read_flat(path):
    """Every row of the flat file, as dictionaries. This one is done for you."""
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def connect(path):
    """Open the database and build the schema. Done for you.

    Read the two PRAGMA lines. SQLite ignores every REFERENCES clause unless
    foreign keys are switched on, the setting belongs to the connection rather
    than to the file, and executescript ends the transaction, which is why it is
    set twice. Step 8 makes you watch what happens without them.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        os.remove(path)
    connection = sqlite3.connect(path)
    connection.execute("PRAGMA foreign_keys = ON")
    with open(SCHEMA, encoding="utf-8") as handle:
        connection.executescript(handle.read())
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def collect_players(rows):
    """TODO step 6: one record per gamertag.

    Return a list of (gamertag, player_name, grade_level) tuples, and a list of
    the name conflicts you found, so the lab can print them.
    """
    return [], []


def collect_matches(rows):
    """TODO step 7: one record per match.

    Return a dictionary keyed by (played_on, opponent) whose value is
    (match_id, played_on, opponent, game_title, our_score, their_score).
    You assign the match_id here. Nothing in the file has one.
    """
    return {}


def collect_appearances(rows, matches):
    """TODO step 7: one record per (match, player).

    Return a list of (match_id, gamertag, role, kills, deaths) tuples, plus a
    count of the exact duplicate rows you collapsed.
    """
    return [], 0


def main():
    rows = read_flat(SOURCE)
    players, conflicts = collect_players(rows)
    matches = collect_matches(rows)
    appearances, duplicates = collect_appearances(rows, matches)

    connection = connect(DATABASE)
    # TODO step 7: insert each list with executemany, in an order the foreign
    # keys allow. Work out that order before you write the lines.
    connection.commit()

    print(f"flat rows read      {len(rows)}")
    print(f"players             {len(players)}")
    print(f"matches             {len(matches)}")
    print(f"appearances         {len(appearances)}")
    print(f"duplicate rows      {duplicates}")
    for tag, kept, other in conflicts:
        print(f"name conflict       {tag}: kept '{kept}', also saw '{other}'")

    # TODO step 9: the kills per player query, from the junction table.
    connection.close()


if __name__ == "__main__":
    main()
