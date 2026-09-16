# report.py . Lab M04-04 starter
#
# This file runs right now. Two of the six queries are written.
#
# The report the coach reads, and the one player record form.
#
#   python report.py
#   python report.py form vexcalibur
#
# Every number is calculated in SQL. The database already knows how to group,
# count, average, and divide, and a calculation written in SQL sits next to the
# data it is about, where somebody who does not write Python can read it and
# argue with it.
#
# Three things in here are worth reading before you copy them:
#
#   NULLIF(x, 0)   turns a zero into NULL so a division gives NULL instead of a
#                  number. A kill to death ratio with zero deaths is not
#                  infinity, it is "we cannot say yet".
#   printf('%.2f') formats at the edge, not in the middle. Round for display,
#                  never while you are still calculating. And watch it:
#                  printf('%.2f', NULL) prints 0.00 in SQLite, so a NULL you
#                  were careful to produce becomes a number that looks real.
#                  That is why the ratios below are wrapped in a CASE.
#   COUNT(a.match_id) rather than COUNT(*)
#                  the LEFT JOIN guard. A player who has never played still
#                  produces one row with every appearance column NULL, and
#                  COUNT(*) counts that row. Step 7 makes you watch it happen.

import argparse
import csv
import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB = os.path.join(HERE, "output", "esports.db")

PER_PLAYER = """
-- TODO step 3. One row per player, with these columns and these names:
--   gamertag, player_name, grade_level, matches_played, kills, deaths,
--   kd_ratio, kills_per_match
-- LEFT JOIN from players, so a player who has never played still appears.
-- kd_ratio and kills_per_match are calculated fields. Read the notes at the top
-- of this file about NULLIF and printf before you write them.
SELECT 'not written yet' AS answer
"""

PER_GAME = """
-- TODO step 4. One row per game title: matches, wins, losses, win rate as a
-- percent, average score for, average score against. Wins and losses come from
-- SUM over a CASE, not from running two queries and subtracting.
SELECT 'not written yet' AS answer
"""

PER_MATCH = """
-- TODO step 5. One row per match, with the team's total kills and the gamertag
-- of that match's top scorer. The top scorer needs a subquery in the SELECT.
SELECT 'not written yet' AS answer
"""

NEVER_PLAYED = """
SELECT p.gamertag, p.player_name, p.grade_level
FROM players p
WHERE NOT EXISTS (SELECT 1 FROM appearances a WHERE a.gamertag = p.gamertag)
ORDER BY p.gamertag
"""

ROLE_SPREAD = """
-- TODO step 6. One row per role: how many times it was played, how many
-- different players played it, and the average kills in it.
SELECT 'not written yet' AS answer
"""

PLAYER_FORM = """
SELECT p.gamertag, p.player_name, p.grade_level
FROM players p WHERE p.gamertag = :gamertag
"""

PLAYER_HISTORY = """
SELECT m.played_on, m.opponent, m.game_title AS game,
       m.our_score || '-' || m.their_score AS score,
       a.role, a.kills, a.deaths,
       CASE WHEN a.deaths > 0 THEN printf('%.2f', 1.0 * a.kills / a.deaths)
            ELSE 'n/a' END AS kd
FROM appearances a
JOIN matches m ON m.match_id = a.match_id
WHERE a.gamertag = :gamertag
ORDER BY m.played_on
"""


def open_database(path):
    connection = sqlite3.connect(path)
    connection.execute("PRAGMA foreign_keys = ON")
    connection.row_factory = sqlite3.Row
    return connection


def table(rows, headers):
    if not rows:
        return "  (no rows)"
    body = [[("" if value is None else str(value)) for value in row] for row in rows]
    widths = [max(len(headers[i]), max(len(r[i]) for r in body))
              for i in range(len(headers))]
    lines = ["  " + "  ".join(headers[i].ljust(widths[i]) for i in range(len(headers)))]
    lines.append("  " + "  ".join("-" * widths[i] for i in range(len(headers))))
    for r in body:
        lines.append("  " + "  ".join(r[i].ljust(widths[i]) for i in range(len(headers))))
    return "\n".join(lines)


def section(connection, title, sql, note=None):
    """Run one query and print it as a table.

    The column headings come from the query itself, through cursor.description,
    rather than from a list kept next to it. Two lists that have to stay in step
    is one list too many, and it means the name you give a calculated field with
    AS is the name the coach reads.
    """
    cursor = connection.execute(sql)
    headers = [description[0] for description in cursor.description]
    rows = [tuple(row) for row in cursor]
    out = [title]
    if note:
        out.append("   " + note)
    out.append(table(rows, headers))
    out.append("")
    return "\n".join(out)


def build_report(connection):
    out = ["RIDGE CREEK ESPORTS . SEASON REPORT", ""]
    out.append(section(connection, "1. BY PLAYER", PER_PLAYER,
                       "kd_ratio reads n/a when a player has no deaths yet."
                       " It is not a zero."))
    out.append(section(connection, "2. BY GAME", PER_GAME))
    out.append(section(connection, "3. BY MATCH", PER_MATCH))
    out.append(section(connection, "4. ON THE ROSTER, NEVER PLAYED", NEVER_PLAYED,
                       "If this list is empty, section 1 is safe. If it is not,"
                       " read section 1's matches_played column again."))
    out.append(section(connection, "5. BY ROLE", ROLE_SPREAD))
    return "\n".join(out)


def build_form(connection, gamertag):
    player = connection.execute(PLAYER_FORM, {"gamertag": gamertag}).fetchone()
    if player is None:
        return f"No player {gamertag} on the roster."
    cursor = connection.execute(PLAYER_HISTORY, {"gamertag": gamertag})
    headers = [description[0] for description in cursor.description]
    history = [tuple(row) for row in cursor]
    lines = ["RIDGE CREEK ESPORTS . PLAYER RECORD", ""]
    lines.append(f"  Gamertag   {player['gamertag']}")
    lines.append(f"  Name       {player['player_name']}")
    lines.append(f"  Grade      {player['grade_level']}")
    lines.append(f"  Matches    {len(history)}")
    lines.append("")
    lines.append("  Match history")
    lines.append(table(history, headers))
    return "\n".join(lines)


def write_player_csv(connection, path):
    """The same query, as a file the coach can open in a spreadsheet.

    A report a person reads and a file a program reads are two products of one
    query. Producing both from one query is how they stay in agreement.
    """
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    cursor = connection.execute(PER_PLAYER)
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.writer(handle)
        writer.writerow([description[0] for description in cursor.description])
        writer.writerows([list(row) for row in cursor])
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description="The esports season report.")
    parser.add_argument("mode", nargs="?", default="report", choices=["report", "form"])
    parser.add_argument("gamertag", nargs="?")
    parser.add_argument("--db", default=DEFAULT_DB)
    arguments = parser.parse_args(argv)

    if not os.path.exists(arguments.db):
        print(f"No database at {arguments.db}. Run: python build_db.py")
        return 1
    connection = open_database(arguments.db)
    if arguments.mode == "form":
        if not arguments.gamertag:
            print("Pass a gamertag, for example: python report.py form vexcalibur")
            return 2
        print(build_form(connection, arguments.gamertag))
        connection.close()
        return 0

    text = build_report(connection)
    print(text)
    report_path = os.path.join(HERE, "output", "season_report.txt")
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    csv_path = write_player_csv(connection, os.path.join(HERE, "output", "by_player.csv"))
    print(f"Written: {report_path}")
    print(f"Written: {csv_path}")
    connection.close()
    return 0


if __name__ == "__main__":
    sys.exit(main())
