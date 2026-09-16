# box_office.py
#
# The drama club box office report.
#
#   python box_office.py
#   python box_office.py --night 2027-11-13
#
# Built to the requirements in the Gate 2 handout, Part A.

import argparse
import csv
import os
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
TICKETS_CSV = os.path.join(HERE, "tickets.csv")
NIGHTS_CSV = os.path.join(HERE, "nights.csv")
DATABASE = os.path.join(HERE, "output", "boxoffice.db")

SCHEMA = """
DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS nights;

CREATE TABLE nights (
    night    TEXT PRIMARY KEY,
    room     TEXT NOT NULL,
    capacity INTEGER NOT NULL CHECK (capacity > 0)
);

CREATE TABLE tickets (
    ticket_id   TEXT PRIMARY KEY,
    night       TEXT NOT NULL REFERENCES nights (night),
    ticket_type TEXT NOT NULL CHECK (ticket_type IN ('student', 'adult', 'senior', 'comp')),
    price_cents INTEGER NOT NULL CHECK (price_cents >= 0),
    refunded    TEXT
);
"""


def build(connection):
    """Load both CSV files into the database."""
    connection.executescript(SCHEMA)
    connection.execute("PRAGMA foreign_keys = ON")
    with open(NIGHTS_CSV, newline="", encoding="utf-8") as handle:
        connection.executemany(
            "INSERT INTO nights (night, room, capacity) VALUES (?, ?, ?)",
            [(r["night"], r["room"], int(r["capacity"])) for r in csv.DictReader(handle)])
    with open(TICKETS_CSV, newline="", encoding="utf-8") as handle:
        connection.executemany(
            "INSERT INTO tickets (ticket_id, night, ticket_type, price_cents, refunded) "
            "VALUES (?, ?, ?, ?, ?)",
            [(r["ticket_id"], r["night"], r["ticket_type"], int(r["price_cents"]),
              r["refunded"] or None) for r in csv.DictReader(handle)])
    connection.commit()


def money(cents):
    """Format a number of cents as dollars."""
    return f"${cents / 100:,.2f}"


def report_by_night(connection, night_filter):
    """One row per performance night."""
    print("BY NIGHT")
    print(f"  {'night':<12} {'room':<16} {'sold':>5} {'revenue':>10} {'median_price':>13}")
    print(f"  {'-' * 12} {'-' * 16} {'-' * 5} {'-' * 10} {'-' * 13}")

    if night_filter:
        nights = connection.execute(
            f"SELECT night, room, capacity FROM nights "
            f"WHERE night = '{night_filter}' ORDER BY night").fetchall()
    else:
        nights = connection.execute(
            "SELECT night, room, capacity FROM nights ORDER BY night").fetchall()

    total_dollars = 0
    for night, room, capacity in nights:
        row = connection.execute(
            "SELECT COUNT(*), SUM(price_cents), AVG(price_cents) "
            "FROM tickets WHERE night = ?", (night,)).fetchone()
        sold, revenue, median_price = row[0], row[1] or 0, row[2] or 0
        total_dollars += revenue
        print(f"  {night:<12} {room:<16} {sold:>5} {money(revenue):>10} "
              f"{money(median_price):>13}")
    print()
    print(f"  Total revenue: {money(total_dollars)}")
    print()


def report_by_type(connection, night_filter):
    """One row per ticket type."""
    print("BY TICKET TYPE")
    print(f"  {'type':<10} {'count':>6} {'revenue':>10}")
    print(f"  {'-' * 10} {'-' * 6} {'-' * 10}")
    sql = ("SELECT ticket_type, COUNT(*), SUM(price_cents) FROM tickets "
           "{where} GROUP BY ticket_type ORDER BY SUM(price_cents) DESC")
    where = f"WHERE night = '{night_filter}'" if night_filter else ""
    for ticket_type, count, revenue in connection.execute(sql.format(where=where)):
        print(f"  {ticket_type:<10} {count:>6} {money(revenue or 0):>10}")
    print()


def main():
    parser = argparse.ArgumentParser(description="The drama club box office report.")
    parser.add_argument("--night", default=None,
                        help="restrict the report to one performance night")
    arguments = parser.parse_args()

    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)
    if os.path.exists(DATABASE):
        os.remove(DATABASE)
    connection = sqlite3.connect(DATABASE)
    connection.execute("PRAGMA foreign_keys = ON")
    build(connection)

    print("RIDGE CREEK DRAMA CLUB . BOX OFFICE REPORT")
    if arguments.night:
        print(f"restricted to {arguments.night}")
    print()
    report_by_night(connection, arguments.night)
    report_by_type(connection, arguments.night)
    connection.close()


main()
