# build_db.py . Lab M04-02, given to you complete
#
# One flat CSV in, three tables out.
#
#   python build_db.py
#
# Lab M04-01 built this. Here it is finished, so everybody starts level.
# The whole of M04-01 is one idea: the flat file repeats the match on every player row,
# and the repetition is where wrong data comes from. Split the repeated facts out
# into their own table, give each table a key, and connect them.

import csv
import os
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "esports_flat.csv")
SCHEMA = os.path.join(HERE, "schema.sql")
DATABASE = os.path.join(HERE, "output", "esports.db")


def read_flat(path):
    """Every row of the flat file, as dictionaries."""
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def connect(path):
    """Open the database with foreign keys ON.

    SQLite ignores every REFERENCES clause unless you switch this on, and it is
    a setting on the connection rather than on the file. Step 8 of the lab makes
    you watch that happen.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if os.path.exists(path):
        os.remove(path)
    connection = sqlite3.connect(path)
    connection.execute("PRAGMA foreign_keys = ON")
    with open(SCHEMA, encoding="utf-8") as handle:
        connection.executescript(handle.read())
    connection.execute("PRAGMA foreign_keys = ON")   # executescript ended the transaction
    return connection


def collect_players(rows):
    """One record per gamertag, first spelling of the name wins.

    The same gamertag appears with two spellings of the same person's name. The
    key is the gamertag, so the two rows are one player. Which spelling to keep
    is a decision, and it is written in the lab's decision line.
    """
    players = {}
    conflicts = []
    for row in rows:
        tag = row["gamertag"].strip()
        name = row["player_name"].strip()
        grade = int(row["grade_level"])
        if tag not in players:
            players[tag] = (tag, name, grade)
        elif players[tag][1] != name:
            conflicts.append((tag, players[tag][1], name))
    return list(players.values()), conflicts


def collect_matches(rows):
    """One record per (played_on, opponent), with a match_id assigned here."""
    matches = {}
    for row in rows:
        key = (row["played_on"].strip(), row["opponent"].strip())
        if key not in matches:
            matches[key] = (len(matches) + 1, key[0], key[1],
                            row["game_title"].strip(),
                            int(row["our_score"]), int(row["their_score"]))
    return matches


def collect_appearances(rows, matches):
    """One record per (match, player). Exact duplicate rows collapse."""
    appearances = {}
    duplicates = 0
    for row in rows:
        key = (row["played_on"].strip(), row["opponent"].strip())
        match_id = matches[key][0]
        tag = row["gamertag"].strip()
        if (match_id, tag) in appearances:
            duplicates += 1
            continue
        appearances[(match_id, tag)] = (match_id, tag, row["role"].strip(),
                                        int(row["kills"]), int(row["deaths"]))
    return list(appearances.values()), duplicates


def main():
    rows = read_flat(SOURCE)
    players, conflicts = collect_players(rows)
    matches = collect_matches(rows)
    appearances, duplicates = collect_appearances(rows, matches)

    connection = connect(DATABASE)
    # executemany is one call into the database instead of one per row. At 28
    # rows nobody notices. At 280,000 the difference is minutes.
    connection.executemany("INSERT INTO players VALUES (?, ?, ?)", players)
    connection.executemany("INSERT INTO matches VALUES (?, ?, ?, ?, ?, ?)",
                           sorted(matches.values()))
    connection.executemany("INSERT INTO appearances VALUES (?, ?, ?, ?, ?)", appearances)
    connection.commit()

    print(f"flat rows read      {len(rows)}")
    print(f"players             {len(players)}")
    print(f"matches             {len(matches)}")
    print(f"appearances         {len(appearances)}")
    print(f"duplicate rows      {duplicates}")
    for tag, kept, other in conflicts:
        print(f"name conflict       {tag}: kept '{kept}', also saw '{other}'")

    print()
    print("Kills per player, from the junction table:")
    query = """
        SELECT p.gamertag, p.player_name, COUNT(*) AS matches_played,
               SUM(a.kills) AS kills, SUM(a.deaths) AS deaths
        FROM players p
        JOIN appearances a ON a.gamertag = p.gamertag
        GROUP BY p.gamertag, p.player_name
        ORDER BY kills DESC
    """
    for tag, name, played, kills, deaths in connection.execute(query):
        print(f"  {tag:<13} {name:<16} {played} matches  {kills:>3} kills  {deaths:>3} deaths")
    connection.close()


if __name__ == "__main__":
    main()
