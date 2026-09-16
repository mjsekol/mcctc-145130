# starter_scraper.py
# SQ-13 The Scraper. A starting point, not a solution.
#
# This file runs right now, without the site running. It does not collect
# anything. It prints the questions you must answer before it should.
#
# Rename it when you start, for example corner_pocket_report.py.

import csv
import json
import time
import urllib.error
import urllib.parse
import urllib.request
import urllib.robotparser

from table_reader import read_links, read_tables

BASE_URL = "http://127.0.0.1:8000"

# TODO: name your program and say what it is for. The shop's terms ask for this.
USER_AGENT = "TODO"

# TODO: set this from the shop's terms of use AND its robots.txt. Use the stricter one.
DELAY_SECONDS = None

# TODO: list every path you have decided NOT to request, and say why in your README.
# robots.txt is one reason. It is not the only one.
NEVER_REQUEST = []

BEFORE_YOU_COLLECT_ANYTHING = [
    "Have you opened robots.txt in a browser and copied its rules into your README?",
    "Have you read the whole terms page and quoted the sentences that allow and forbid things?",
    "Does the shop offer a data feed for any of the data you want? If so, use it for that data.",
    "Is any page you plan to request behind a sign-in, or about customers?",
    "What is the longest wait between requests that either document asks for?",
]


def main():
    print("SQ-13 starter. Nothing is collected until these are answered in your README:")
    for question in BEFORE_YOU_COLLECT_ANYTHING:
        print(f"  - {question}")
    if USER_AGENT == "TODO" or DELAY_SECONDS is None:
        print("USER_AGENT and DELAY_SECONDS are not set yet. Stopping.")
        return
    # TODO: read robots.txt with urllib.robotparser.
    # TODO: collect only what both documents allow, waiting DELAY_SECONDS before every request.
    # TODO: clean the data, write it to a CSV or JSON file, and print a report with a calculated field.


main()
