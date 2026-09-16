# The Bellfield Note Sorter
## What it does. Invented program, invented school.

A team built this for a front office that gets short written notes about problems
in the building. It reads a folder of notes and prints a digest to the terminal.

**Everything on this page is invented.** Bellfield is not a real school and the
program does not exist. It is described precisely so that you can check claims
about it.

---

## How it is started

```
python sorter.py
```

prints, and does nothing else:

```
usage: sorter.py --folder FOLDER
```

```
python sorter.py --folder notes
```

prints the digest.

**There are no other flags.** There is no configuration file and no menu.

---

## What the digest looks like

```
================================================
BELLFIELD NOTE SORTER
14 notes read from notes/
================================================

SUMMARY
Most of this week's notes are about equipment, with a few about the
network and a small number about people not being able to sign in.

equipment (4)
  - the 3D printer in room 118 jammed again
  - the second monitor on station 11 is intermittent
  - the laminator is out of pouches
  - somebody left the band saw guard off

software (2)
  - the design software crashes opening from the shared drive
  - the install on station 6 rolls itself back

network (4)
  - wifi drops in the back corner of the lab
  - the printer in the office will not stay connected
  - uploads keep failing part way
  - the cart tablets cannot see the shared drive

access (1)
  - locked out after a password change

other (3)
  - thank you for fixing the hallway cart
  - the room 118 door sticks
  - can we get a second recycling bin
```

---

## What it does not do

- **There is no search.** Nothing takes a word and finds the notes containing it.
- **There is no date or time anywhere in the output.** Notes appear in the order
  the files were read.
- **Nothing can be changed after the fact.** A note in the wrong category stays
  there.
- **The categories are fixed:** equipment, software, network, access, other. There
  is no list anywhere explaining what each one means.

---

## The three tasks used in the study

```
T1  You are covering the front desk on Monday and there is a pile of
    notes from last week. You want to know how many of them are about
    the network before you start answering any of them. Show me how you
    would find that out.

T2  Somebody stops you in the hall and says the thing they reported last
    week never got dealt with. It was something about not being able to
    sign in. You want to find what they wrote. Show me how you would
    look.

T3  It is Monday morning, there are fourteen notes, and you have twenty
    minutes before your first meeting. Decide which three you would deal
    with first, using whatever the program gives you.
```

**The correct answer to T1 is 4.** It is in the category header.

**The correct answer to T2 is the single note under `access`.**
