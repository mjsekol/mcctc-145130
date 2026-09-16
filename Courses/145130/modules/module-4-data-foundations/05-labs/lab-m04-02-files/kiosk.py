# kiosk.py . Lab M04-02
#
# The front end. A small program the team manager runs after a match to record
# the result and the lineup.
#
#   python kiosk.py list
#   python kiosk.py add --date 2027-03-03 --opponent "Maple Ridge" --game "Rocket League" ^
#                       --ours 4 --theirs 3 ^
#                       --lineup vexcalibur:striker:5:2,static_mango:midfield:3:3,nightowl99:keeper:1:1
#   python kiosk.py fix-grade --player kettlecorn --grade 12
#   python kiosk.py remove-match --match 7
#   python kiosk.py remove-player --player crabrangoon
#
# Read this file before you run it. Everything it checks, it checks in Python.
# Part of this lab is deciding which of those checks belongs down in the database
# instead, and proving what happens when it is not there.

import argparse
import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(HERE, "output", "esports.db")

# The roles the kiosk knows about. This list lives in the front end.
ROLES = ["striker", "midfield", "keeper",
         "duelist", "controller", "sentinel", "initiator"]


def connect(path):
    connection = sqlite3.connect(path)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def parse_lineup(text):
    """tag:role:kills:deaths,tag:role:kills:deaths -> a list of tuples."""
    lineup = []
    for entry in text.split(","):
        parts = entry.split(":")
        if len(parts) != 4:
            raise ValueError(f"'{entry}' is not tag:role:kills:deaths")
        tag, role, kills, deaths = parts
        if not kills.isdigit() or not deaths.isdigit():
            raise ValueError(f"'{entry}' has a kill or death count that is not a number")
        lineup.append((tag.strip(), role.strip(), int(kills), int(deaths)))
    return lineup


def check(connection, played_on, opponent, ours, theirs, lineup):
    """Everything the front end checks. Returns a list of problems."""
    problems = []
    if ours < 0 or theirs < 0:
        problems.append("a score cannot be negative")
    if len(lineup) == 0:
        problems.append("a match needs at least one player")
    known = {row[0] for row in connection.execute("SELECT gamertag FROM players")}
    for tag, role, kills, deaths in lineup:
        if tag not in known:
            problems.append(f"{tag} is not on the team roster")
        if role not in ROLES:
            problems.append(f"{role} is not a role the kiosk knows")
        if kills < 0 or deaths < 0:
            problems.append(f"{tag} has a negative count")
    return problems


def add(connection, played_on, opponent, game, ours, theirs, lineup):
    problems = check(connection, played_on, opponent, ours, theirs, lineup)
    if problems:
        print("The kiosk refused this match:")
        for problem in problems:
            print(f"  - {problem}")
        return 1

    cursor = connection.execute(
        "INSERT INTO matches (played_on, opponent, game_title, our_score, their_score) "
        "VALUES (?, ?, ?, ?, ?)", (played_on, opponent, game, ours, theirs))
    match_id = cursor.lastrowid
    # Save the match straight away so the match_id is safe.
    connection.commit()

    for tag, role, kills, deaths in lineup:
        connection.execute(
            "INSERT INTO appearances (match_id, gamertag, role, kills, deaths) "
            "VALUES (?, ?, ?, ?, ?)", (match_id, tag, role, kills, deaths))
    connection.commit()
    print(f"Recorded match {match_id}: {opponent} on {played_on}, "
          f"{ours}-{theirs}, {len(lineup)} players.")
    return 0


def fix_grade(connection, player, grade):
    cursor = connection.execute(
        "UPDATE players SET grade_level = ? WHERE gamertag = ?", (grade, player))
    connection.commit()
    print(f"{cursor.rowcount} row(s) changed.")
    return 0


def remove_match(connection, match_id):
    cursor = connection.execute("DELETE FROM matches WHERE match_id = ?", (match_id,))
    connection.commit()
    print(f"{cursor.rowcount} match row(s) deleted.")
    return 0


def remove_player(connection, player):
    cursor = connection.execute("DELETE FROM players WHERE gamertag = ?", (player,))
    connection.commit()
    print(f"{cursor.rowcount} player row(s) deleted.")
    return 0


def listing(connection):
    print("matches")
    for row in connection.execute(
            "SELECT m.match_id, m.played_on, m.opponent, m.game_title, "
            "       m.our_score, m.their_score, COUNT(a.gamertag) AS players "
            "FROM matches m LEFT JOIN appearances a ON a.match_id = m.match_id "
            "GROUP BY m.match_id ORDER BY m.match_id"):
        print(f"  {row[0]:>2}  {row[1]}  {row[2]:<14} {row[3]:<14} "
              f"{row[4]}-{row[5]}   {row[6]} players")
    counts = connection.execute(
        "SELECT (SELECT COUNT(*) FROM players), (SELECT COUNT(*) FROM matches), "
        "       (SELECT COUNT(*) FROM appearances)").fetchone()
    print(f"players {counts[0]}   matches {counts[1]}   appearances {counts[2]}")
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="The esports kiosk front end.")
    parser.add_argument("command",
                        choices=["list", "add", "fix-grade", "remove-match", "remove-player"])
    parser.add_argument("--date")
    parser.add_argument("--opponent")
    parser.add_argument("--game")
    parser.add_argument("--ours", type=int)
    parser.add_argument("--theirs", type=int)
    parser.add_argument("--lineup")
    parser.add_argument("--player")
    parser.add_argument("--grade", type=int)
    parser.add_argument("--match", type=int)
    parser.add_argument("--db", default=DATABASE)
    arguments = parser.parse_args(argv)

    if not os.path.exists(arguments.db):
        print(f"No database at {arguments.db}. Run: python build_db.py")
        return 1
    connection = connect(arguments.db)
    try:
        if arguments.command == "list":
            return listing(connection)
        if arguments.command == "add":
            lineup = parse_lineup(arguments.lineup or "")
            return add(connection, arguments.date, arguments.opponent, arguments.game,
                       arguments.ours, arguments.theirs, lineup)
        if arguments.command == "fix-grade":
            return fix_grade(connection, arguments.player, arguments.grade)
        if arguments.command == "remove-match":
            return remove_match(connection, arguments.match)
        if arguments.command == "remove-player":
            return remove_player(connection, arguments.player)
    except ValueError as error:
        print(f"The kiosk could not read that: {error}")
        return 2
    except sqlite3.IntegrityError as error:
        print(f"The database refused it: {error}")
        return 3
    finally:
        connection.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
