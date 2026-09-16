"""Turn note lines into flashcards.

Invented project. Part of the MCCTC 145130 Module 3 licensing audit fixture.
"""
from vendor.lanternparse.lanternparse import split_once
from vendor.sortwell.sortwell import sort_by_key


def build_cards(lines):
    """Build one card per 'Term: definition' line. Blank and comment lines are skipped."""
    cards = []
    for line in lines:
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        term, definition = split_once(text, ":")
        if definition is None:
            continue
        cards.append({"term": term.strip(), "definition": definition.strip()})
    return sort_by_key(cards, "term")
