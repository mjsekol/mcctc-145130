# SQ-13 · The Scraper
## Corner Pocket Cards · 145060 Programming · Unlocks Unit 5, Week 11

**Time:** two blocks. **Difficulty:** ★★★
**Competencies:** 5.5.7 (read inputs, including a web source), 5.3.11 (access data
repositories), 1.7.13 (protect intellectual property).

---

## The situation

Corner Pocket Cards is a local card shop with a website: new arrivals, a price guide, an
events calendar, customer accounts, and wish lists. **It is invented, and its website runs on
your own computer.** Nobody in this quest scrapes a real site.

Your job: extract structured data from the shop's site, clean it, and produce a report with at
least one calculated field. Something a player who shops there would actually use.

## The constraints are the quest

These come from the Side Quest Catalog, and they are not optional:

- **Read `robots.txt` first and obey it.** Put what it said in your README.
- **Read the site's terms of use. Quote the relevant sentences.**
- **Rate limit yourself** to at most one request every two seconds, **or slower if the site asks
  for slower.**
- **Never scrape anything behind a login.**
- **Never collect personal information about anybody.**
- **If the site offers an API or data feed, use it instead, and say so.**

**This site was built so that following one rule is not enough.** Some of what `robots.txt`
allows, the terms forbid. Some of what is on the pages is offered a better way. Read everything
before you write the first request.

**A student who decides mid-quest that part of this site should not be scraped, and writes up
why, has completed that part of the quest.** That judgment is the skill.

---

## Files

| File | What it is |
|---|---|
| `serve_site.py` | Runs the shop's website at `http://127.0.0.1:8000/` |
| `site/` | The website's pages, `robots.txt`, and data feed. Do not edit it. |
| `table_reader.py` | The same helper as Lab U5-05: `read_tables` and `read_links` |
| `starter_scraper.py` | A starting point that runs and collects nothing until you configure it |

---

## How to run the site

**Terminal 1**, from this folder:

```
python serve_site.py
```

```
Corner Pocket Cards running at http://127.0.0.1:8000/
Press Ctrl+C to stop.
```

Leave it running. Every request prints a line with the time since the one before, and the
User-Agent that sent it. **The server refuses requests less than one second apart with
`429 Too Many Requests`.** The shop's own terms ask for more than that.

**Terminal 2**, from your quest folder, runs your program. Copy `table_reader.py` next to your
program.

**Press Ctrl+C in Terminal 1 when you finish.**

---

## How to work

**Checkpoint 1: read like a person.** Open the site in a browser. Visit every link on the home
page. Open `/robots.txt`. Read `/terms.html` all the way through. Then, **before writing any code**,
write a table in your README with one row for each section of the site: new arrivals, price guide,
events, account, wish lists. For each, answer: does `robots.txt` allow it, do the terms allow it, is
there a better way to get it, and will you collect it.

**Checkpoint 2: configure the starter.** Set a User-Agent that names your program. Set the delay from
the stricter of the two documents. List every path you will never request.

**Checkpoint 3: collect only what you decided to collect.** Use `can_fetch` before every page and your
never-request list, and wait before every request. Keep Terminal 1 visible.

**Checkpoint 4: clean and report.** Clean what you collected into consistent values. Write it to a CSV or
JSON file. Print a report with at least one calculated field, such as the value of the stock in each game,
or how full each event is.

---

## What to submit

A repository containing:

1. **Your program**, runnable against `serve_site.py`.
2. **Your clean dataset**, as a CSV or JSON file.
3. **`README.md`**, with these sections:
   - **What it does**, and how to run it.
   - **Why this was allowed.** The `robots.txt` rules, the terms sentences you relied on, and your table
     from checkpoint 1. **This section is required by the catalog.**
   - **What I did not collect, and why.** Every section you left alone, with the reason.
   - **The report**, pasted from a real run.
   - **The server log** from Terminal 1 for that run, pasted.
4. **Commits** across both blocks.

## Done when

- [ ] A clean dataset and a report with at least one calculated field
- [ ] A `Why this was allowed` section that cites `robots.txt` and quotes the terms
- [ ] Terminal 1's log shows only requests your README says are allowed, each one at least as far apart
      as the stricter document asks
- [ ] Nothing behind a sign-in, and nothing about customers, was requested
- [ ] Anything the shop offers as a data feed was taken from the feed
- [ ] You can explain every decision in the checkpoint 1 table

---

## Hints, if you are stuck

**"robots.txt allows the page, so I can take it."** Read the terms again, section by section. Two documents,
two different questions.

**"My scraper gets 429 on the first page."** Look at Terminal 1. How long after `robots.txt` did your first
page request arrive? Wait before that request too.

**"The events are right there in a table."** Read the events page's first paragraph, and the terms' events
section.

**"can_fetch says nothing is allowed."** Did you call `read()` first?

**"I want to compare the price guide to the new arrivals to find deals."** That is a genuinely good idea for a
shopper, and it is exactly what this shop's terms forbid a program from doing. Writing that up is worth more than
building it.

---

## Grading

Scored under **BPA / Credential / Capstone**. 40 points.

| Dimension | Points | Standard |
|---|---|---|
| Judgment | 14 | The checkpoint 1 table is right for every section of the site, and the program's requests match it exactly. |
| Why this was allowed | 10 | Cites `robots.txt`, quotes the terms, and explains anything left out. |
| Working program | 10 | Collects the allowed data politely, cleans it, and produces a report with a calculated field. |
| Explanation | 6 | You can talk through any decision on request. |

**A request to a page your own table says you should not collect scores zero for Judgment**, however good the
report is. A student who collects nothing, and whose table and write-up are right, can still earn the Judgment and
Why this was allowed points.
