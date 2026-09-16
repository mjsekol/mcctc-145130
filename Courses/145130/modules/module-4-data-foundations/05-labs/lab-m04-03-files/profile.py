# profile.py . Lab M04-03 solution
#
# Runs every query in profile.sql against the staging database and prints the
# answers as titled tables.
#
#   python profile.py
#   python profile.py --sql profile.sql --db output\staging.db
#
# The queries live in a .sql file rather than in this program on purpose. A
# question about the data is something a person who does not write Python should
# be able to read, add to, and argue with.

import argparse
import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DB = os.path.join(HERE, "output", "staging.db")
DEFAULT_SQL = os.path.join(HERE, "profile.sql")
MARKER = "-- QUERY:"


def split_queries(text):
    """(title, sql) for every block introduced by a '-- QUERY:' line."""
    queries = []
    title = None
    body = []
    for line in text.splitlines():
        if line.startswith(MARKER):
            if title is not None and "".join(body).strip():
                queries.append((title, "\n".join(body)))
            title = line[len(MARKER):].strip()
            body = []
        elif title is not None:
            body.append(line)
    if title is not None and "".join(body).strip():
        queries.append((title, "\n".join(body)))
    return queries


def table(headers, rows):
    if not rows:
        return "  (no rows, which is itself an answer)"
    body = [[("" if value is None else str(value)) for value in row] for row in rows]
    widths = [max(len(headers[i]), max(len(r[i]) for r in body)) for i in range(len(headers))]
    lines = ["  " + "  ".join(headers[i].ljust(widths[i]) for i in range(len(headers)))]
    lines.append("  " + "  ".join("-" * widths[i] for i in range(len(headers))))
    for r in body:
        lines.append("  " + "  ".join(r[i].ljust(widths[i]) for i in range(len(headers))))
    return "\n".join(lines)


def run(db_path=DEFAULT_DB, sql_path=DEFAULT_SQL):
    with open(sql_path, encoding="utf-8") as handle:
        queries = split_queries(handle.read())
    connection = sqlite3.connect(db_path)
    for number, (title, sql) in enumerate(queries, start=1):
        print(f"\n{number}. {title}")
        cursor = connection.execute(sql)
        headers = [description[0] for description in cursor.description]
        print(table(headers, cursor.fetchall()))
    connection.close()
    return len(queries)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Profile the staging database.")
    parser.add_argument("--db", default=DEFAULT_DB)
    parser.add_argument("--sql", default=DEFAULT_SQL)
    arguments = parser.parse_args(argv)
    if not os.path.exists(arguments.db):
        print(f"No staging database at {arguments.db}. Run: python stage.py")
        return 1
    count = run(arguments.db, arguments.sql)
    print(f"\n{count} questions asked. No data was changed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
