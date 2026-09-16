# Requirements · Supply Sweep

**This is the document the program in this folder was supposedly built from.**
Read it before you read a line of code. Every defect in this exercise is a
disagreement between this file and that one.

---

## The situation

The school store keeps a small stock of things people run out of in the middle
of a build: filament, gloves, safety glasses, tape, lanyards, resin, SD cards.
The inventory tool exports a weekly file of what is on hand and what people
wrote when they asked for more.

Somebody has to read that file, decide what to reorder, and give the store
manager a list. That is twenty minutes a week that is the same twenty minutes
every week, which is what makes it worth automating.

---

## The requirements

| # | Requirement | Why it is there |
|---|---|---|
| R1 | The sweep runs on a schedule, without anybody starting it. | If somebody has to remember, it is not an automation. |
| R2 | An item is reordered when its on-hand count is **at or below** its threshold. | The threshold is the line the store manager set. Sitting on the line is the last moment to order, not the moment after. |
| R3 | Each reordered item's note is sorted into a category. The model service does that when it can. When it cannot, a keyword rule stands in. | Categories are how the store manager batches orders by vendor. |
| R4 | The service is checked for health **once per run**, not once per item. | A health check costs a round trip. Twenty items should not cost twenty of them. |
| R5 | The run log records **counts only**. No note text and no submitted-by name reaches any file this program writes. | The notes are free text people wrote about their own classes and their own problems. Program rule: no personal data enters a file, a log, or a model. |
| R6 | The run log is appended on **every** run, including the runs that did not work. | A log that only records good runs is a log that says this automation has never failed. |
| R7 | When a step does not get what it expected, the export owner is told, by something that reaches them when nobody is watching the terminal. | The sweep runs before anybody is in the building. |
| R8 | Every command passes an explicit `--service`. There is no default. | A program that reaches the wrong server does not fail. It answers. |

---

## The export format

`requests.json`, written by the inventory tool.

```json
{
  "requests": [
    {
      "id": "SR-101",
      "item": "PLA filament, white, 1kg",
      "on_hand": 2,
      "threshold": 5,
      "note": "free text somebody typed",
      "submitted_by": "a name"
    }
  ]
}
```

**Everything in the bundled `requests.json` is invented.** The names are made up
so that R5 has something to be about.

---

## What the store manager gets

A file listing every item at or below threshold, with its on-hand count, its
threshold, and its category.

---

## How to run it

```
python sweep_service_stub.py --port 5159
python supply_sweep.py --service http://127.0.0.1:5159 --once
python supply_sweep.py --service http://127.0.0.1:5159 --every 5 --runs 2
```

The stub answers the same two endpoints the Module 5 service answers. It also
answers `GET /stub/stats`, which reports how many times it was called. That
endpoint is in this bundle for a reason.

```
python sweep_service_stub.py --port 5159 --mode error500
python sweep_service_stub.py --port 5159 --mode empty
```
