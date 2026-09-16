"""vectorstore.py . a vector store in SQLite, written with the standard library.

Lab M04-05 starter. Three functions are yours: cosine, add, and search.

A vector database is not magic and it is not a different kind of computer. It is
a table of vectors plus a way to find the nearest ones. The part a real vector
database adds is an index that finds approximate neighbours without comparing
every row, which matters at a million rows and does not matter at forty. Below
forty thousand chunks on a laptop, a full scan in a loop is fast enough, and
writing it yourself is the only way to see that there is nothing hidden in it.

WHAT THIS STORE REFUSES TO DO

  - It does not assume a vector length. The length of the first vector added
    becomes the length of the index, it is written into `index_meta`, and a
    vector of any other length is refused with both numbers in the message.
  - It does not silently compare vectors of different lengths. Two models produce
    numbers that mean nothing to each other, and cosine similarity between them
    is a number with no meaning that looks exactly like a number with meaning.
  - It does not store a chunk without its source. Every chunk carries its
    document, its heading, and its character offsets, because the reason to use
    retrieval instead of fine tuning is that you can point at where the answer
    came from.

WHAT COSINE SIMILARITY IS

The cosine of the angle between two vectors. 1.0 means the same direction, 0.0
means at right angles, -1.0 means opposite. It ignores length, which is what you
want, because a longer chunk should not score higher for being longer.
"""

import json
import math
import os
import sqlite3

SCHEMA = """
PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS index_meta (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS chunks (
    chunk_id   INTEGER PRIMARY KEY,
    doc_id     TEXT NOT NULL,
    heading    TEXT NOT NULL,
    ordinal    INTEGER NOT NULL,
    char_start INTEGER NOT NULL,
    char_end   INTEGER NOT NULL,
    text       TEXT NOT NULL,
    UNIQUE (doc_id, ordinal)
);

CREATE TABLE IF NOT EXISTS vectors (
    chunk_id INTEGER PRIMARY KEY REFERENCES chunks (chunk_id) ON DELETE CASCADE,
    dim      INTEGER NOT NULL,
    vector   TEXT NOT NULL
);
"""


class DimensionMismatch(ValueError):
    """Raised when a vector does not match the length this index was built with."""


def cosine(a, b):
    """TODO part 2, step 6. Cosine similarity between two equal length vectors.

    The dot product of a and b, divided by the product of their lengths.
    The length of a vector is the square root of the sum of its squares.

    Two rules this function has to follow:
      1. If the two vectors are different lengths, raise DimensionMismatch with
         BOTH lengths in the message. They came from different models and the
         answer would be meaningless.
      2. If either vector has zero length, return 0.0 rather than dividing by
         zero.
    """
    raise NotImplementedError("part 2, step 6")


class VectorStore:
    """Chunks and their vectors, in one SQLite file."""

    def __init__(self, path):
        self.path = path
        if path != ":memory:":
            os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        self.connection = sqlite3.connect(path)
        self.connection.execute("PRAGMA foreign_keys = ON")
        self.connection.executescript(SCHEMA)
        self.connection.execute("PRAGMA foreign_keys = ON")

    # -- metadata ----------------------------------------------------------

    def set_meta(self, key, value):
        self.connection.execute(
            "INSERT INTO index_meta (key, value) VALUES (?, ?) "
            "ON CONFLICT (key) DO UPDATE SET value = excluded.value", (key, str(value)))

    def get_meta(self, key, default=None):
        row = self.connection.execute(
            "SELECT value FROM index_meta WHERE key = ?", (key,)).fetchone()
        return default if row is None else row[0]

    @property
    def dimensions(self):
        """The vector length this index was built with, or None if it is empty."""
        value = self.get_meta("dimensions")
        return None if value is None else int(value)

    # -- writing -----------------------------------------------------------

    def add(self, chunk, vector):
        """TODO part 2, step 7. Store one chunk and its vector.

        `chunk` is a dictionary with doc_id, heading, ordinal, char_start,
        char_end, and text. Return the new chunk_id.

        The rule that matters: this index must learn its vector length from the
        FIRST vector it is given and then refuse any vector of another length,
        with both numbers in the message. Nothing in this file may contain the
        number 32. The stub returns 32 numbers and a real model returns
        hundreds, and code that learned 32 passes every test here and fails on
        the first machine with a model on it.

        Store the vector with json.dumps. SQLite has no list type.
        """
        raise NotImplementedError("part 2, step 7")


    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()

    # -- reading -----------------------------------------------------------

    def count(self):
        return self.connection.execute("SELECT COUNT(*) FROM chunks").fetchone()[0]

    def documents(self):
        return [row[0] for row in self.connection.execute(
            "SELECT DISTINCT doc_id FROM chunks ORDER BY doc_id")]

    def search(self, query_vector, k=4, min_score=None):
        """TODO part 2, step 8. The k nearest chunks, best first.

        Return a list of dictionaries, each with chunk_id, doc_id, heading,
        ordinal, char_start, char_end, text, and score.

        Read every chunk and its vector, score each one with cosine(), sort, and
        return the best k. A full scan. At 56 chunks that is the right answer,
        and saying so is more useful than pretending an index is required.

        Two rules:
          1. An empty index returns an empty list rather than raising.
          2. A query vector of the wrong length raises DimensionMismatch, with
             both numbers in the message.

        Sort on the score AND on something stable, so that two chunks with the
        same score always come back in the same order. A search that returns a
        different order on two runs is a search nobody can check.
        """
        raise NotImplementedError("part 2, step 8")
