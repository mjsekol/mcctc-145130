# backdoor.py . Lab M04-02
#
# A second program that writes straight to the database, without going anywhere
# near the kiosk. Fifteen lines. Somebody writes one of these in every real
# system, usually on a Friday, usually to fix something quickly.
#
#   python backdoor.py
#
# Every rule the kiosk enforces is a rule this program never runs.

import os
import sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(HERE, "output", "esports.db")

connection = sqlite3.connect(DATABASE)
connection.execute("PRAGMA foreign_keys = ON")     # step 5 asks you to comment this out

connection.execute(
    "INSERT INTO appearances (match_id, gamertag, role, kills, deaths) "
    "VALUES (?, ?, ?, ?, ?)", (99, "ghost_player", "goalkeeper", 40, 0))
connection.commit()

print("Wrote one appearance row: match 99, ghost_player, goalkeeper, 40 kills.")
print("appearances now:",
      connection.execute("SELECT COUNT(*) FROM appearances").fetchone()[0])
connection.close()
