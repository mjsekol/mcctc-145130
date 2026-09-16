# stage.py . Lab M04-03 starter
#
# This file runs right now. One of the three importers works.
#
# Three source files, three import techniques, one staging database.
#
#   python stage.py
#   python stage.py --data <folder> --db output\staging.db
#
# WHY STAGING TABLES ARE ALL TEXT
#
# A staging table is a photograph of the file. It is not the schema you are going
# to keep. Every column is TEXT and nothing is converted, because the moment you
# convert you have thrown something away and you can no longer ask what the file
# actually said. `int('11')` and `int(' 11 ')` are both 11, and one of them tells
# you a volunteer typed a space.
#
# Every row carries the line number it came from, so any problem you find can be
# handed back to a person with a place to look.

import argparse
import csv
import json
import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DATA = os.path.join(HERE, "..", "fixtures", "ridge-makerspace")
# If you copied this folder somewhere else, pass --data with the path to the
# ridge-makerspace fixture folder. Do not copy the raw files around.
DEFAULT_DB = os.path.join(HERE, "output", "staging.db")

SCHEMA = """
DROP TABLE IF EXISTS stg_loans;
DROP TABLE IF EXISTS stg_members;
DROP TABLE IF EXISTS stg_items;

CREATE TABLE stg_loans (
    source_row  INTEGER NOT NULL,
    loan_id     TEXT, member_id TEXT, item_id TEXT,
    checked_out TEXT, due TEXT, returned TEXT, notes TEXT
);

CREATE TABLE stg_members (
    source_row  INTEGER NOT NULL,
    member_id   TEXT, full_name TEXT, grade_level TEXT, program TEXT, joined TEXT
);

CREATE TABLE stg_items (
    source_position INTEGER NOT NULL,
    item_id TEXT, name TEXT, category TEXT, loan_days TEXT,
    cost TEXT, funded_by TEXT, purchase_year TEXT,
    replacement_value TEXT, condition TEXT, tags TEXT
);
"""

LOAN_COLUMNS = ["loan_id", "member_id", "item_id", "checked_out", "due", "returned", "notes"]


def stage_loans_with_executemany(connection, path):
    """Technique 1: read with the csv module, insert with executemany.

    encoding='utf-8-sig' strips the byte order mark a spreadsheet writes. With
    plain utf-8 the first column comes back named '\\ufeffloan_id' and every
    row['loan_id'] raises KeyError on a line that looks correct.
    """
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as handle:
        reader = csv.reader(handle)
        header = [name.strip() for name in next(reader)]
        if header != LOAN_COLUMNS:
            raise ValueError(f"unexpected columns in {path}: {header}")
        for fields in reader:
            if len(fields) != len(LOAN_COLUMNS):
                continue
            rows.append([reader.line_num] + fields)
    connection.executemany(
        "INSERT INTO stg_loans (source_row, loan_id, member_id, item_id, "
        "checked_out, due, returned, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", rows)
    return len(rows)


def stage_members_with_sql_script(connection, path, script_folder):
    """TODO step 4: technique 2, a generated SQL script.

    Read the pipe delimited member file, skip the comment lines, and build one
    INSERT statement per member as TEXT. Write the whole thing to
    load_members.sql in script_folder, then run it with
    connection.executescript(script).

    Escape every value. A single quote inside a value ends the string early and
    breaks the script, and in a system that matters it is worse than that.

    Return the number of statements you generated.
    """
    return 0


def stage_items_from_json(connection, path):
    """TODO step 5: technique 3, the nested JSON catalog.

    Read the file with json.load. Each item has a tags ARRAY and a purchase
    OBJECT. Flatten each item into one staging row.

    Keep the tags joined with ';' for now. Splitting them into their own table is
    a schema decision, and staging is a photograph rather than a decision.

    Return the number of rows you inserted.
    """
    return 0


def stage(db_path=DEFAULT_DB, data_dir=DEFAULT_DATA, verbose=True):
    os.makedirs(os.path.dirname(os.path.abspath(db_path)), exist_ok=True)
    if os.path.exists(db_path):
        os.remove(db_path)
    connection = sqlite3.connect(db_path)
    connection.executescript(SCHEMA)

    loans = stage_loans_with_executemany(
        connection, os.path.join(data_dir, "raw", "loans_spring.csv"))
    members = stage_members_with_sql_script(
        connection, os.path.join(data_dir, "raw", "members_legacy.txt"),
        os.path.dirname(os.path.abspath(db_path)))
    items = stage_items_from_json(
        connection, os.path.join(data_dir, "raw", "catalog.json"))
    connection.commit()

    if verbose:
        print("staged, nothing converted, nothing dropped")
        print(f"  stg_loans    {loans:>3} rows   (csv module, executemany)")
        print(f"  stg_members  {members:>3} rows   (generated SQL script, executescript)")
        print(f"  stg_items    {items:>3} rows   (json module, executemany)")
    connection.close()
    return {"loans": loans, "members": members, "items": items}


def main(argv=None):
    parser = argparse.ArgumentParser(description="Stage the three raw makerspace files.")
    parser.add_argument("--data", default=DEFAULT_DATA)
    parser.add_argument("--db", default=DEFAULT_DB)
    arguments = parser.parse_args(argv)
    try:
        stage(arguments.db, arguments.data)
    except FileNotFoundError as error:
        print(f"A source file is missing: {error.filename}")
        return 1
    except ValueError as error:
        print(f"A source file does not look the way this program expects: {error}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
