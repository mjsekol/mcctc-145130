"""chunker.py . cut a Markdown document into retrievable pieces.

Lab M04-05 starter. This file runs. chunk_text returns nothing yet.

WHY CHUNK AT ALL

You cannot retrieve a whole handbook. A model has a context window, and even if
it did not, handing it eight documents to answer one question about the vinyl
cutter buries the sentence that matters. Retrieval works on pieces, so the size
and the boundary of a piece decide what the system can and cannot answer.

THE TWO WAYS TO GET THIS WRONG

Too small, and a chunk stops being an answer. "Five days." is a true sentence
that helps nobody, because the chunk no longer says five days of what.

Too big, and every chunk looks like every other chunk. A whole document embeds
to an average of everything in it, so the vinyl cutter chunk and the resin
printer chunk end up near each other and neither one wins.

THE RULE HERE

Split on Markdown headings first, because a heading is a boundary somebody who
knew the content already chose. Then split any section longer than
`max_characters` at a blank line or a sentence end, never mid word, with
`overlap` characters repeated at the seam so a sentence cut in half still
appears whole in one of the two pieces.

Every chunk carries its document, its heading, and its character offsets in the
original file, so any hit can be traced to the line it came from. That
traceability is the honest reason to prefer retrieval over fine tuning, and it
only exists if you keep the offsets here.
"""

import os
import re

HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
DEFAULT_MAX_CHARACTERS = 900
DEFAULT_OVERLAP = 120
DEFAULT_MIN_CHARACTERS = 80


def split_sections(text):
    """(heading, body, start_offset) for each Markdown heading in the document.

    Text before the first heading is kept under the heading '(top)', because
    dropping it would drop the sentence that says the document is invented.
    """
    lines = text.splitlines(keepends=True)
    sections = []
    heading = "(top)"
    start = 0
    body = []
    position = 0
    for line in lines:
        match = HEADING.match(line.rstrip("\n"))
        if match:
            if "".join(body).strip():
                sections.append((heading, "".join(body), start))
            heading = match.group(2).strip()
            start = position + len(line)
            body = []
        else:
            body.append(line)
        position += len(line)
    if "".join(body).strip():
        sections.append((heading, "".join(body), start))
    return sections


def split_long(body, start_offset, max_characters, overlap):
    """Cut one long section into overlapping windows at a sensible boundary."""
    pieces = []
    position = 0
    length = len(body)
    while position < length:
        end = min(position + max_characters, length)
        if end < length:
            window = body[position:end]
            # Prefer a blank line, then a sentence end, then a space. Never a
            # character in the middle of a word.
            for boundary in ("\n\n", ". ", ".\n", " "):
                cut = window.rfind(boundary)
                if cut > max_characters // 3:
                    end = position + cut + len(boundary)
                    break
        pieces.append((body[position:end], start_offset + position, start_offset + end))
        if end >= length:
            break
        position = max(end - overlap, position + 1)
    return pieces


def chunk_text(doc_id, text, max_characters=DEFAULT_MAX_CHARACTERS,
               overlap=DEFAULT_OVERLAP, min_characters=DEFAULT_MIN_CHARACTERS,
               use_headings=True):
    """TODO part 1, step 4. A list of chunk dictionaries for one document.

    Each chunk is a dictionary with exactly these keys:

        doc_id      the file name
        heading     the Markdown heading this piece came from
        ordinal     0, 1, 2, ... within this document
        char_start  where this piece starts in the original file
        char_end    where it ends
        text        what gets embedded

    What to do:

      1. Get the sections. With use_headings=True that is split_sections(text).
         With use_headings=False, treat the whole document as one section whose
         heading is '(whole document)' and whose start offset is 0.
      2. For each section, call split_long() to cut it into pieces.
      3. Skip a piece that is empty once stripped.
      4. Put the doc_id and the heading INSIDE the text you store. The embedding
         only ever sees the text, so a chunk whose heading is not in it has
         thrown away the strongest clue it had.
      5. A section shorter than min_characters is not an answer on its own.
         Decide what to do with it, do it, and write down what you chose.

    The offsets are not decoration. They are how a hit gets traced back to a line
    in a file, which is the whole reason to prefer retrieval over fine tuning.
    """
    return []


def chunk_folder(folder, pattern=".md", **options):
    """Chunk every matching file in a folder, in sorted order."""
    chunks = []
    for name in sorted(os.listdir(folder)):
        if not name.endswith(pattern):
            continue
        with open(os.path.join(folder, name), encoding="utf-8") as handle:
            chunks.extend(chunk_text(name, handle.read(), **options))
    return chunks
