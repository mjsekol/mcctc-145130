"""sortwell: stable sorting helpers for lists of dictionaries.

Copyright (C) 2024 Sortwell Authors

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see the GNU project's published copy of the license.

INVENTED COMPONENT. Written for the MCCTC 145130 Module 3 licensing fixture.
Sortwell is not a real project.
"""


def sort_by_key(records, key):
    """Return records sorted by one key, case-insensitively, leaving the input alone."""
    return sorted(records, key=lambda record: str(record.get(key, "")).lower())
