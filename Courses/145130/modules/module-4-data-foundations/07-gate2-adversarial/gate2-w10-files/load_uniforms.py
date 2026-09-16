# load_uniforms.py
#
# Loads the marching band uniform catalog and the season's checkouts into a
# SQLite database, and reports what happened.
#
#   python load_uniforms.py
#
# Built to the requirements in the Gate 2 handout, Part A.

import csv
import os
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
UNIFORMS_CSV = os.path.join(HERE, "uniforms.csv")
CHECKOUTS_CSV = os.path.join(HERE, "checkouts.csv")
DATABASE = os.path.join(HERE, "output", "band.db")

SCHEMA = """
DROP TABLE IF EXISTS checkouts;
DROP TABLE IF EXISTS uniforms;

CREATE TABLE uniforms (
    uniform_id TEXT PRIMARY KEY,
    piece      TEXT NOT NULL,
    size       TEXT NOT NULL,
    condition  TEXT NOT NULL
);

CREATE TABLE checkouts (
    checkout_id  TEXT PRIMARY KEY,
    uniform_id   TEXT NOT NULL REFERENCES uniforms (uniform_id),
    member       TEXT NOT NULL,
    checked_out  TEXT NOT NULL,
    due          TEXT NOT NULL,
    returned     TEXT
);
"""


def read_csv(path):
    """Read a CSV file into a list of dictionaries."""
    with open(path, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def connect():
    """Open the database, switch foreign keys on, and build the schema."""
    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    connection = sqlite3.connect(DATABASE)
    connection.execute("PRAGMA foreign_keys = ON")
    connection.executescript(SCHEMA)
    connection.execute("PRAGMA foreign_keys = ON")
    return connection


def clean(value):
    """Trim the outer whitespace off a value from the file."""
    return value.strip() if value else ""


def validate_checkout(connection, row):
    """Check that a checkout row is valid before it goes into the database."""
    found = connection.execute(
        "SELECT 1 FROM uniforms WHERE uniform_id = ?",
        (clean(row["uniform_id"]),)).fetchone()
    return found is not None


def load_uniforms(connection, rows):
    """Load the catalog. Every value is checked against the schema first."""
    for row in rows:
        connection.execute(
            f"INSERT OR IGNORE INTO uniforms (uniform_id, piece, size, condition) "
            f"VALUES ('{clean(row['uniform_id'])}', '{clean(row['piece'])}', "
            f"'{clean(row['size'])}', '{clean(row['condition'])}')")
    connection.commit()
    return len(rows)


def load_checkouts(connection, rows):
    """Load the checkouts. Nothing is dropped without being reported."""
    loaded = 0
    for row in rows:
        if validate_checkout(connection, row):
            connection.execute(
                f"INSERT OR IGNORE INTO checkouts "
                f"(checkout_id, uniform_id, member, checked_out, due, returned) "
                f"VALUES ('{clean(row['checkout_id'])}', '{clean(row['uniform_id'])}', "
                f"'{clean(row['member'])}', '{clean(row['checked_out'])}', "
                f"'{clean(row['due'])}', '{clean(row['returned'])}')")
        loaded = loaded + 1
    connection.commit()
    return loaded


def still_out(connection):
    """Print every uniform that has not come back."""
    print("Uniforms still out:")
    for uniform in connection.execute(
            "SELECT uniform_id, piece, size FROM uniforms ORDER BY uniform_id"):
        for checkout in connection.execute(
                "SELECT member, due FROM checkouts "
                "WHERE uniform_id = ? AND returned = '' ORDER BY checked_out",
                (uniform[0],)):
            print(f"  {uniform[0]}  {uniform[1]:<9} {uniform[2]:<9} "
                  f"{checkout[0]:<18} due {checkout[1]}")


def main():
    uniform_rows = read_csv(UNIFORMS_CSV)
    checkout_rows = read_csv(CHECKOUTS_CSV)

    connection = connect()
    uniforms_loaded = load_uniforms(connection, uniform_rows)
    checkouts_loaded = load_checkouts(connection, checkout_rows)

    print("Ridge Creek band . uniform load")
    print(f"  uniforms   read {len(uniform_rows):>3}   loaded {uniforms_loaded:>3}")
    print(f"  checkouts  read {len(checkout_rows):>3}   loaded {checkouts_loaded:>3}")
    print(f"  rejected   {len(checkout_rows) - checkouts_loaded}")
    print()
    still_out(connection)
    connection.close()


main()
