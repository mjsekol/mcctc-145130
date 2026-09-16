# Gate 2: Adversarial Review · Week 10
## 145130 Applications of AI · Module 4 · Week 10, Friday

**40 minutes**, in Build 1 after the Gate 1 rep. Individual. You may and should run the
code. **You may not ask a model whether it is correct**, because a model is what is being
reviewed.

The program is `gate2-w10-files/load_uniforms.py`. Copy the folder and run it.

---

## What you are looking at

Somebody handed an AI assistant the requirements in Part A and got this program back. It
runs. It is formatted well, every function has a docstring, and the docstrings sound sure of
themselves.

**Five defects, one in each category:**

| Dimension | What to look for |
|---|---|
| **Correctness** | It does not do what it says it does |
| **Security** | It trusts input it did not check, or hands data to something that will run it |
| **Readability** | A name or a comment that misleads the next reader |
| **Performance** | Work done more times than it needs to be |
| **Requirements Fit** | Something Part A asked for that is missing |

**Four of the five leave no error message at all.** The program finishes, prints a report,
and the report is wrong. That is the shape of every defect this module has shown you.

---

## PART A: The requirements

> Write `load_uniforms.py`, which loads the marching band's uniform catalog and this season's
> checkouts into a SQLite database.
>
> 1. Read `uniforms.csv` and `checkouts.csv`.
> 2. Build a schema with a `uniforms` table and a `checkouts` table, with a foreign key from
>    a checkout to the uniform it is for, **enforced**.
> 3. Load both files.
> 4. **Refuse any checkout that points at a uniform id that is not in the catalog, and refuse
>    any duplicate checkout id.**
> 5. **Print every refused row with its line number in the source file and the reason it was
>    refused**, so the uniform manager can go and ask the person who wrote it.
> 6. Print how many rows were read and how many were loaded, for each file.
> 7. Print every uniform that has not come back, with who has it and when it was due.

*(The band, the uniforms, the members, and the dates are invented for this course.)*

---

## PART B: What the AI produced

The code is in `gate2-w10-files/`. Run it:

```
python load_uniforms.py
```

A real run:

```
Ridge Creek band . uniform load
  uniforms   read  12   loaded  12
  checkouts  read  20   loaded  20
  rejected   0

Uniforms still out:
  U-101  jacket    S         Maya Ostrowski     due 2027-11-15
  U-102  jacket    M         Rosa Delacroix     due 2027-11-15
  U-104  jacket    L         Ines Bergstrom     due 2027-11-15
  U-104  jacket    L         Owen Falk          due 2027-11-15
  U-105  jacket    XL        Aiden Nakashima    due 2027-11-15
  U-202  trousers  M         Rosa Delacroix     due 2027-11-15
  U-204  trousers  L         Ines Bergstrom     due 2027-11-15
  U-302  shako     one size  Rosa Delacroix     due 2027-11-15
  U-302  shako     one size  Tanvi Srinivasan   due 2027-11-15
```

**Read that report against requirement 4 before you read any code.** Then open
`checkouts.csv` and read it against the report.

---

## What to submit

For each defect: **file and line**, **dimension**, **what goes wrong for a real person**, and
**the fix**. Then one final entry: **what I was unsure about**, naming something specific.
That entry is scored and a blank costs more than a wrong guess.

### How to spend 40 minutes

- **First 6:** run it. Count the rows in `checkouts.csv` by hand. Ask the database how many
  rows are actually in the `checkouts` table, and compare all three numbers.
- **Next 8:** read Part A one requirement at a time, and for each one find the line of code
  that meets it. One requirement has no line.
- **Next 10:** read every line that builds a string which is then handed to the database.
  For each one, ask what happens if a value from the file contains the character that ends
  that string. **Try it.**
- **Next 8:** read every docstring against the code under it. Ask whether the sentence is
  true.
- **Rest:** look for work being repeated. Count how many times the program asks the database
  something when it could have asked once.

**One useful command:**

```
python -c "import sqlite3; print(sqlite3.connect('output/band.db').execute('SELECT COUNT(*) FROM checkouts').fetchone())"
```

---

## Scoring

Five defects, one point each, plus one for the unsure-about entry. Your instructor states the
security weighting before you start.

**Three of five is a normal score. Four is strong.**

**One of the five is genuinely arguable**, and the key scores your reasoning rather than your
verdict. If you decide something is not a defect, say why, and say what would change your
mind. That is worth the same as finding it.
