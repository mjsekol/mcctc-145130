# table_reader.py
# Pulls the tables and links out of a web page, using only Python's
# standard library.
#
# Use it like any other module:
#
#     from table_reader import read_tables, read_links
#
#     tables = read_tables(page_text)   # a list of tables
#     rows = tables[0]                  # a table is a list of rows
#     header = rows[0]                  # a row is a list of cell strings
#
#     links = read_links(page_text)     # a list of {"text": ..., "href": ...}
#
# Why this file exists: HTML is not plain text you can split on "<td>".
# Real pages put attributes inside tags, line breaks inside cells, and
# codes like &amp; in place of characters. A parser reads the page the way
# a browser does. The standard library parser, html.parser, is used through
# a class, and classes are Unit 7. You may use this file without
# understanding the class yet, the same way you use json without reading
# its source code. Reading it anyway is good preparation for Unit 7.
#
# Limits, stated plainly: tables inside tables are not supported, and the
# text of each cell has its whitespace collapsed to single spaces.

from html.parser import HTMLParser


class _PageReader(HTMLParser):
    def __init__(self):
        # convert_charrefs=True turns &amp; into & and similar codes into characters.
        super().__init__(convert_charrefs=True)
        self.tables = []
        self.links = []
        self._row = None
        self._cell = None
        self._link = None

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.tables.append([])
        elif tag == "tr" and self.tables:
            self._row = []
        elif tag in ("td", "th") and self._row is not None:
            self._cell = []
        elif tag == "a":
            href = ""
            for name, value in attrs:
                if name == "href" and value is not None:
                    href = value
            self._link = {"text": [], "href": href}

    def handle_endtag(self, tag):
        if tag in ("td", "th") and self._cell is not None:
            self._row.append(" ".join("".join(self._cell).split()))
            self._cell = None
        elif tag == "tr" and self._row is not None:
            self.tables[-1].append(self._row)
            self._row = None
        elif tag == "a" and self._link is not None:
            text = " ".join("".join(self._link["text"]).split())
            self.links.append({"text": text, "href": self._link["href"]})
            self._link = None

    def handle_data(self, data):
        if self._cell is not None:
            self._cell.append(data)
        if self._link is not None:
            self._link["text"].append(data)


def read_tables(page_text):
    """Return every table in the page as a list of rows, each a list of cell strings."""
    reader = _PageReader()
    reader.feed(page_text)
    reader.close()
    return reader.tables


def read_links(page_text):
    """Return every link in the page as a dictionary with "text" and "href"."""
    reader = _PageReader()
    reader.feed(page_text)
    reader.close()
    return reader.links
