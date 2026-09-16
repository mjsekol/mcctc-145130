# Ridge Study Planner
## What it is. Invented program, invented team.

A team in a previous class built this. It reads a list of assignments and asks a
locally hosted model, through a service, to suggest an order to do them in, with
one sentence of reason per item. It prints the plan to the terminal.

**Everything on this page is invented.** The program does not exist. It is
described precisely so that claims about it can be checked.

---

## How it is started

```
python planner.py --file assignments.json
```

There is one other flag:

```
python planner.py --file assignments.json --week
```

which prints the same assignments grouped by the day they are due, instead of in a
suggested order.

---

## What it prints

```
RIDGE STUDY PLANNER
6 assignments read from assignments.json

 1. Chemistry lab write-up          due Thu
    Longest of the six and the only one you cannot finish in one sitting.
 2. Spanish vocabulary set          due Wed
    Short, and it is the one you will skip if you leave it until Wednesday.
 3. Government reading response     due Fri
    ...
 6. Algebra problem set 12          due Mon

plan source: model
```

**The last line is the whole of how you find out where the plan came from.** It
says `model` when the model produced the order, and `due-date rule` when the
service could not be used and the program sorted by due date instead.

---

## What it does not have

- **There is no onboarding of any kind.** No first-run walkthrough, no tour, no
  setup screen. It reads the file and prints.
- **There is no mobile version and no web version.** It is a terminal program.
- **There is no way to ask it why, beyond the sentence printed under each item.**
- **It was never tested on a phone or a tablet**, because it does not run on one.

---

## The three tasks used in the study

```
T1  You have six assignments and about two hours tonight. Work out what you
    are going to do first.

T2  The plan has put something in an order you would not have picked. Find out
    what it says about why.

T3  Somebody tells you the model on this machine has been down since lunchtime.
    Find out whether the plan in front of you came from the model or not.
```

**The correct answer to T3 is the `plan source:` line at the bottom of the
output.** In every one of the four sessions, that line said `due-date rule`.
