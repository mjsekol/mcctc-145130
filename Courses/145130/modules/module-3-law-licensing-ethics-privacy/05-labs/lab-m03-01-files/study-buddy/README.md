# Study Buddy

Study Buddy turns a page of class notes into flashcards you can drill before a test.
Point it at a text file. It reads the file, finds the term-and-definition lines, and
writes a deck. If a locally hosted model is running, it can also write a hint for each
card in plainer words.

Built by the Study Buddy team for the fall showcase.

---

## READ THIS FIRST, BEFORE YOU AUDIT ANYTHING

**This whole project is invented for this course. It is a composite.** The team does not
exist. Every third-party component in `vendor/`, `assets/`, `model/`, and `data/` is
invented for this exercise, and the names do not refer to any real project, package,
font, model, or dataset. Do not search for them and do not cite them as real.

**What is real is the shape.** Every licensing problem planted in this tree is a problem
that shows up in student and professional projects constantly: a component whose license
file never got copied, an image that came from a web search, a snippet pasted out of a
blog post, a sound with a use restriction nobody read, a model whose license is not an
open source license at all.

The license **identifiers** used here (MIT, Apache License 2.0, GPL-3.0-or-later,
CC BY 4.0, CC BY-NC 4.0, CC BY-SA 4.0) are real license identifiers. Where the full text
of a license is short and standard, it is included in this tree so you can read it. Where
it is long, the file points you at the license steward's own published text, which is the
only version that governs. Read the text. Do not read a summary and stop.

---

## How to run it

```
python study_buddy.py notes/chemistry.txt
```

There is one sample notes file in `notes/`. Study Buddy writes `deck.json` next to it.

To ask a locally hosted model for hints, always passing the port:

```
python study_buddy.py notes/chemistry.txt --hints --port 11634
```

If no model is running, Study Buddy says so and writes the deck without hints. It does
not crash and it does not pretend the hints are there.

**No API key.** Study Buddy talks to a locally hosted, Ollama-compatible endpoint on this
machine. It never talks to a commercial service.

**Always pass `--port`.** This module uses **11634**. A real Ollama listens on 11434 and so do
several stubs in this course, and a run against the wrong server looks exactly like a working
run, with nothing on screen to tell you.

---

## What is in this project

| Path | What it is |
|---|---|
| `study_buddy.py` | The program. Reads notes, writes a deck, optionally asks a local model for hints. |
| `make_cards.py` | The parser that turns note lines into cards. |
| `LICENSE` | The license the team chose for its own code. |
| `notes/chemistry.txt` | Sample input. Written by the team. |
| `vendor/pocketgrid/` | Table formatting helper the team copied in. |
| `vendor/lanternparse/` | Text splitting helper the team copied in. |
| `vendor/sortwell/` | Sorting helper the team copied in. |
| `snippets/shuffle_from_blog.py` | A shuffle routine the team found in a blog post. |
| `assets/fonts/` | The display font for the printable card sheet. |
| `assets/icons/` | The icon set used on the card sheet. |
| `assets/sounds/` | The chime that plays when a drill session ends. |
| `assets/images/` | The hero image on the showcase poster. |
| `model/` | The locally hosted model the team used for hints. |
| `data/flashcard_seed/` | The seed dataset the team used to test the parser. |

## Credits

Icons by the Lantern Icon Project. Font is NotoLike. Thanks to everyone who helped.

## Plans

The team wants to put Study Buddy on the showcase table and sell printed card decks for
two dollars each to raise money for the trip.
