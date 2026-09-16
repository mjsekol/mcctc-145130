# Acceptance run record
## An invented team's note sweep · captured terminal output

**Everything in this file is invented**, including the team and the stakeholder.
The output shapes are the shapes this module's own programs produce, so every block
below is the kind of thing you have seen on your own screen this week.

**Read this file before the report.** Every claim in the report can be settled
here.

---

## The procedure that was run

```
Platform: Windows 11, Python 3.13.7, no model runtime installed.
Stakeholder: the person who runs the weekly export. Role, not name.

ID    Given                        When                 Then
AC-1  8 notes, service on 5158     run once             exit 0, digest has 8 rows
AC-2  the same 8 notes, nothing    run once again       exit not 0, incident names
      touched since AC-1                                the freshness step
AC-3  8 notes, nothing listening   run once             exit not 0, incident names
      on 5158                                           the wire failure
AC-4  8 notes, service answers     run once             exit not 0, incident names
      200 with result null                              empty_result
AC-5  0 notes in the inbox         run once             exit not 0, incident says
                                                        the drop did not happen
AC-6  8 notes, service on 5158     run --every 3        two sweeps happen with no
                                   --runs 2             further typing
AC-7  after AC-1 to AC-5           open the run log     one row per run, including
                                                        the failed ones
AC-8  after AC-1 to AC-5           search the run log   no note text and no name
                                   for note text        anywhere in it
```

**Stakeholder attendance:** not present. The team ran it alone and sent the results
afterwards. **No reply had been received when this record was written.**

---

## AC-1

```
python note_sweep.py --service http://127.0.0.1:5158 --once
```

```
note sweep, run r0001
  [ok  ] collect    expected at least 1 note file in the inbox, got 8
  [ok  ] classify   expected 8 labelled notes, got 8
  [ok  ] digest     expected 8 rows written to a file, got 8 rows
  status  OK
```

```
exit code: 0
digest rows: 8
```

**Verdict recorded by the team: PASS**

---

## AC-2

```
python note_sweep.py --service http://127.0.0.1:5158 --once
```

Nothing in `inbox/` was touched between AC-1 and this run.

```
note sweep, run r0002
  [ok  ] collect    expected at least 1 note file in the inbox, got 8
  [ok  ] classify   expected 8 labelled notes, got 8
  [ok  ] digest     expected 8 rows written to a file, got 8 rows
  status  OK
```

```
exit code: 0
out/ contains: digest-r0001.md, digest-r0002.md
```

**Verdict recorded by the team: FAIL.** There is no freshness step. The run
produced a second digest from the same eight notes and reported OK.

---

## AC-3

Stub stopped with Ctrl+C.

```
python note_sweep.py --service http://127.0.0.1:5158 --once
```

```
note sweep, run r0003
  [ok  ] collect    expected at least 1 note file in the inbox, got 8
  [FAIL] classify   expected 8 labelled notes, at least 1 from the service,
                    got 8 labelled, 0 from the service
  status  FAILED
  incident written to out\incident-r0003.md
```

```
exit code: 2
out/incident-r0003.md names: connection_refused x8
```

**Verdict recorded by the team: PASS**

---

## AC-4

```
python sweep_service_stub.py --port 5158 --mode empty
python note_sweep.py --service http://127.0.0.1:5158 --once
```

```
note sweep, run r0004
  [ok  ] collect    expected at least 1 note file in the inbox, got 8
  [ok  ] classify   expected 8 labelled notes, got 8
  [ok  ] digest     expected 8 rows written to a file, got 8 rows
  status  OK
```

```
exit code: 0
```

**Verdict recorded by the team: FAIL.** The service answered HTTP 200 with
`result` set to null for every note. Every label came from the keyword rule and
nothing said so.

---

## AC-5

**Verdict recorded by the team: NOT RUN.** No empty inbox folder was prepared
before the session and there was no time to make one.

---

## AC-6

```
python note_sweep.py --service http://127.0.0.1:5158 --every 3 --runs 2
```

```
note sweep scheduler started. Ctrl+C to stop.
  next sweep in 3 seconds
note sweep, run r0005
  status  OK
  next sweep in 3 seconds
note sweep, run r0006
  status  OK
  2 sweeps done, stopping because --runs was set
```

**Verdict recorded by the team: PASS**

---

## AC-7

```
type state\run_log.csv
```

```
run_id,status,notes,labelled,note_text
r0001,OK,8,8,The 3D printer in room 118 stopped in the middle of a print again.
r0002,OK,8,8,The 3D printer in room 118 stopped in the middle of a print again.
r0003,FAILED,8,8,The 3D printer in room 118 stopped in the middle of a print again.
r0004,OK,8,8,The 3D printer in room 118 stopped in the middle of a print again.
r0005,OK,8,8,The 3D printer in room 118 stopped in the middle of a print again.
r0006,OK,8,8,The 3D printer in room 118 stopped in the middle of a print again.
```

**Verdict recorded by the team: PASS.** There is a row for every run, including
r0003 which failed.

---

## AC-8

```
findstr "room 118" state\run_log.csv
```

```
r0001,OK,8,8,The 3D printer in room 118 stopped in the middle of a print again.
r0002,OK,8,8,The 3D printer in room 118 stopped in the middle of a print again.
r0003,FAILED,8,8,The 3D printer in room 118 stopped in the middle of a print again.
r0004,OK,8,8,The 3D printer in room 118 stopped in the middle of a print again.
r0005,OK,8,8,The 3D printer in room 118 stopped in the middle of a print again.
r0006,OK,8,8,The 3D printer in room 118 stopped in the middle of a print again.
```

**Verdict recorded by the team: FAIL.** The run log holds the text of a note on
every row.

---

## The team's own tally, written at the bottom of the sheet

```
PASS: 4    FAIL: 3    NOT RUN: 1
```
