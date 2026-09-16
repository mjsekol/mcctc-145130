"""pocketgrid: a very small plain-text table formatter.

Copyright (c) 2024 Pocketgrid Contributors

Licensed under the MIT License. See the LICENSE file in this directory for the
full text.

INVENTED COMPONENT. Written for the MCCTC 145130 Module 3 licensing fixture.
Pocketgrid is not a real project.
"""


def format_table(headers, rows):
    """Return a plain-text table. Columns are as wide as their widest cell."""
    widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    line = "  ".join(str(h).ljust(widths[i]) for i, h in enumerate(headers))
    rule = "  ".join("-" * w for w in widths)
    body = [
        "  ".join(str(c).ljust(widths[i]) for i, c in enumerate(row)) for row in rows
    ]
    return "\n".join([line, rule] + body)
