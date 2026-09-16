# Additional Resources · Week 14
## 145130 Applications of AI · Module 5 · Week 14
### Topics: four failure kinds on one HTTP call, timeouts and retries, who gives up first, troubleshooting with a named method

Every link below is marked **Confident** or **[VERIFY]**. A **[VERIFY]** link has not been confirmed
live. Click it before you rely on it.

**This is the competition week and there is no instruction segment.** Some of your teammates are out of
the building. That changes what this page is for: these resources are written so you can work through
them alone, at your own pace, without asking anybody anything. Start with the three lecture notes in
section 8. They are the lesson.

**No commercial AI developer API appears here.** Those services require their users to be 18 or older.
Everything in this module runs against a local model or against the stub that ships with the stack.

| # | Resource | For | Level | Time |
|---|---|---|---|---|
| 1 | MDN, an overview of HTTP and the status code list | Mon | On-level | 35 min |
| 2 | Official docs: `HttpClient` and `HttpClient.Timeout` | Mon, Tue | On-level | 25 min |
| 3 | Official docs: `TaskCanceledException` | Mon | On-level | 15 min |
| 4 | Official docs: `HttpRequestException`, `SocketException`, `SocketError` | Mon | On-level | 20 min |
| 5 | Official docs: `System.Text.Json.JsonSerializer` | Mon | On-level | 20 min |
| 6 | MDN: the 429 status and the `Retry-After` header | Tue | Extension | 15 min |
| 7 | RFC 9110, HTTP Semantics, the status code sections | Tue | Extension | 30 min |
| 8 | This week's three lecture notes and their self-checks | Any | Review | 20 min each |
| 9 | Interactive: the six scenarios, the probe, and the stub's ten behaviours | Wed | On-level | 45 min |
| 10 | The run book, every failure and what it looks like when it works | Any | On-level | 30 min |
| 11 | The two files that own failure: `the Four Failures note` and `contract_demo_service.py` | Mon, Tue | On-level | 40 min |
| 12 | The reference troubleshooting log | Wed | On-level | 15 min |
| 13 | Industry connection: retries, timeouts, and cascading failure | Tue | Extension | 40 min |
| 14 | A free video under 20 minutes | Any | Remediation | under 20 min |
| 15 | SQ-10 API First Contact and SQ-05 Bug Hunt | Fri | Extension | 1-2 blocks |

---

## 1. Primary reading

**MDN Web Docs, an overview of HTTP, and the HTTP response status codes list** ·
`https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview` and
`https://developer.mozilla.org/en-US/docs/Web/HTTP/Status` · **Confident.**

**Why this one.** It is free, it needs no account, and it is the reference the rest of the industry
actually opens. This week you need two things from it and you can skip the rest.

**First, the shape of a request and a response.** A method, a path, headers, a status line, a body.
Your C# client sends one and reads one. The service you are calling sends one and reads one. When you
can name the five parts, a failure stops being "it did not work" and becomes "the status line said 404
and the body was two words long".

**Second, the status classes.** 2xx, 4xx, 5xx, and what each class says about whose fault it is. This
is the distinction Monday's lesson turns into two different messages: a 400 is your request being
wrong, and a 500 is the other program being wrong, and telling a person the wrong one sends them
looking in the wrong place for the rest of the period.

**Read it with one question:** *is a 404 a failure of the network, of the server, or of your request?*
Then read Wednesday's fault E in the lecture notes, where a 404 on the model path means something that
is not a model server is listening on that port.

**Time.** 35 minutes. **Level.** On-level.

---

## 2. `HttpClient` and its timeout

`https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient` · **Confident.**
`https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httpclient.timeout` · **Confident.**

**Why these.** Tuesday's whole lesson is one number on one property, and this is the page that defines
it. Read what `Timeout` covers and what it does not.

**Assign a question:** *What does the documentation say happens when the timeout elapses?* The answer
is the reason Monday's C# catches `TaskCanceledException` rather than a timeout exception, and it
surprises everybody the first time.

**Second question, and this one is worth points on the WebXam-style items:** *what does the
documentation say about creating a new `HttpClient` for every request?* The stack creates one and keeps
it. There is a real reason, and it is about sockets, not about style.

**Time.** 25 minutes. **Level.** On-level.

---

## 3. The exception that is not named Timeout

`https://learn.microsoft.com/en-us/dotnet/api/system.threading.tasks.taskcanceledexception` ·
**Confident.**

**Why this one.** `HttpClient` reports its own timeout by cancelling the task, so the exception you
catch is a cancellation, not a timeout. A cancellation the caller asked for, by pressing Ctrl+C or by
cancelling a token, arrives as the same type.

**The thing to take away.** Two different events, one exception type. You tell them apart by checking
whether the caller's token was cancelled before you blame a timeout, which is what the `when` clause in
the reference client is for. Without that check, a person who pressed Ctrl+C is told the model timed
out, and they go and restart a model that was fine.

**Time.** 15 minutes. **Level.** On-level.

---

## 4. Nothing is listening, and how you know

`https://learn.microsoft.com/en-us/dotnet/api/system.net.http.httprequestexception` · **Confident.**
`https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.socketexception` · **Confident.**
`https://learn.microsoft.com/en-us/dotnet/api/system.net.sockets.socketerror` · **Confident.**

**Why these three together.** A refused connection arrives as an `HttpRequestException` with a
`SocketException` inside it, and the value that says "nothing is listening" is
`SocketError.ConnectionRefused`. Three pages, one fact, and that fact is the difference between the
message "the service is not running, start it with this command" and the message "something went
wrong".

**Assign a question:** *Scan the `SocketError` list. Name two other values that could reach your client,
and say whether each one deserves a different message than ConnectionRefused.* There is no single right
answer and the argument is the point.

**Python's side of the same idea:** `https://docs.python.org/3/library/socket.html` · **Confident.** The
service's health check opens a TCP connection to the model endpoint, sees whether it connects, and
closes it. Find `create_connection` and its timeout argument. A health check that costs an inference is
a health check nobody runs.

**Time.** 20 minutes. **Level.** On-level.

---

## 5. Deserialising a reply you did not write

`https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializer` · **Confident.**
`https://learn.microsoft.com/en-us/dotnet/api/system.text.json.jsonserializeroptions` · **Confident.**

**Why these.** This is the quiet one. `System.Text.Json` will deserialise
`{"status": "ok", "data": {...}}` into your envelope class without throwing anything, and set every
field it did not find to that field's default. `Ok` becomes false, `Source` becomes null, and your
program prints something confident and empty.

**Assign a question:** *What does the serializer do with a JSON property that has no matching member on
the target type, and what does it do with a member that has no matching JSON property?* Both answers
are "nothing", and "nothing" is why you need a `Problem()` check that looks for the fields that must be
there.

**Worth ten more minutes:** find the option that controls case-insensitive property name matching. A
service that returns `elapsed_ms` and a C# property called `ElapsedMs` do not match by accident.

**A 200 status is not proof that the body is your envelope.** Write that down.

**Time.** 20 minutes. **Level.** On-level.

---

## 6. When the server asks you to slow down

`https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429` · **Confident.**
`https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Retry-After` · **Confident.**

**Why these.** One model server may be serving the whole room, because there is not a graphics card per
seat. Thirty clients on one server is how you meet a 429 for real, and 429 is the one failure where the
server tells you how long to wait.

**The thing most people get wrong:** a 429 is retryable and a 400 is not, and both are 4xx. The class
of the status code does not decide whether you retry. What decides is whether trying again could give
a different answer.

**Assign a question:** *`Retry-After` can carry two different kinds of value. Name both, and say which
one is harder to handle correctly.*

**Time.** 15 minutes. **Level.** Extension.

---

## 7. How HTTP is actually defined

**RFC 9110, HTTP Semantics** · `https://www.rfc-editor.org/rfc/rfc9110` · **Confident.**

**Why this one.** It is long, and you are not reading all of it. Go to the status code sections and
read the definitions of 400, 404, 429, 500, and 503. Five short paragraphs.

**What you get for the twenty minutes.** The standard says what each status means, and the words it
uses are more careful than the words people use in conversation. 503 means the server cannot handle the
request right now and may be able to later. 500 means the server hit a condition that stopped it. Those
are different promises to the caller, and the second one is not retryable in the way the first one is.

**The honest caveat.** Real servers do not always follow this, and the model runner on your lab machine
is a real server. A 500 that always means the same thing on your machine is still a 500 you should not
retry blindly. Read the standard, then read your own service's console, and believe the console.

**Time.** 30 minutes. **Level.** Extension.

---

## 8. This week's lecture notes, which are the lesson

There is no instruction segment this week, so these three files carry it. Each one is written to be
worked alone, and each ends with three self-check questions and worked answers.

| Day | Notes |
|---|---|
| Monday | [Four failures, four messages](../03-lecture-notes/MCCTC_145130_Notes_FourFailuresFourMessages.md) |
| Tuesday | [Who gives up first](../03-lecture-notes/MCCTC_145130_Notes_WhoGivesUpFirst.md) |
| Wednesday | [Troubleshooting an integration with a named method](../03-lecture-notes/MCCTC_145130_Notes_TroubleshootingAnIntegration.md) |

**Work Tuesday's example 1 on paper before you read example 2.** Three settings, three numbers each.
If you read the answers first you will believe you would have got them, and one of the three catches
almost everybody.

**The sentence from this week that goes on your monitor:**

> Your application has to wait longer than the service's own worst case, or the labelled fallback the
> service was about to hand you never arrives.

**Time.** 20 minutes each. **Level.** Review.

---

## 9. Interactive practice

Three things to run, in this order. All three are in this repository and all three work with no model
installed.

**The stub model server** ·
[stub_model_server.py](../09-project/project-files/stub_model_server.py) · **Confident.** Ten
behaviours you can select, including HTTP 500, a refusal, prose instead of JSON, and a deliberate
delay. This is how you practise failure handling without waiting for a real failure. Pass a port on
every command, and read the line it prints when it starts.

**The six scenarios** · [scenario.py](../05-labs/lab-m05-03-files/scenario.py) · **Confident.**
Scenario 0 is the healthy baseline, and the reason it exists is that "spot the differences" has nothing
to compare against without one. Scenarios 2 and 4 produce the same symptom from two different causes,
on purpose.

**The contract probe** · [contract_probe.py](../05-labs/lab-m05-03-files/contract_probe.py) ·
**Confident.** Your own program probably does not print `error.kind`. The probe always does, and
`error.kind` is the field that separates two faults that look identical from the outside.

**The lab that drives all three** ·
[Lab M05-03, The Broken Integration](../05-labs/MCCTC_145130_Lab_M05-03_TheBrokenIntegration.md).

**And if you want to measure rather than guess:** [bench.py](../05-labs/lab-m05-03-files/bench.py) runs
the same request repeatedly and gives you a number, which is what a processing requirement needs behind
it.

**Time.** 45 minutes. **Level.** On-level.

---

## 10. The run book

[Lab M05-01](../05-labs/MCCTC_145130_Lab_M05-01_TraceTheContract.md) · **Confident.**

**Why this one.** It shows you how to start the stack, how to break it on purpose, and what each
failure looks like when the system is handling it correctly. Every block in it was captured from a real
run.

**Read it for the thing nobody teaches.** Knowing what correct failure handling looks like on screen is
a skill, and it is the one that tells you whether the fallback you are looking at is the system working
or the system broken. A labelled fallback with a reason under it is the system working.

**Time.** 30 minutes. **Level.** On-level.

---

## 11. Read the two files that own failure

You have been told what the client does. Now read it. Both files are commented to explain why, not
what.

**The C# side** ·
[Notes_FourFailuresFourMessages.md](../03-lecture-notes/MCCTC_145130_Notes_FourFailuresFourMessages.md) ·
**Confident.** One `HttpClient`, four failure kinds, and a sentence of advice attached to each one.
Find the `when` clause on the `TaskCanceledException` catch, and find the code that prints the first
120 characters of a body it could not understand.

**The Python side** ·
[contract_demo_service.py](../05-labs/lab-m05-01-files/contract_demo_service.py) · **Confident.** The
only file in the service that talks to the model. Timeout, retries, and the set of failure kinds that
are worth retrying. Find that set and check it against Tuesday's rule: retry what could change, do not
retry what cannot.

**The tests** ·
[test_parse_plan.py](../05-labs/lab-m05-02-files/test_parse_plan.py) ·
**Confident.** Tests that make a fake service fail on purpose, which is the pattern you need for your
own build. You cannot demonstrate that you handle a timeout by waiting for one to happen.

**Assign yourself a question:** *find the line that decides a connection was refused rather than
something else going wrong on the way, and say what would break if that line were removed.*

**Time.** 40 minutes. **Level.** On-level.

---

## 12. The reference troubleshooting log

[troubleshooting-log.md](../09-project/reference-implementation/docs/troubleshooting-log.md) ·
**Confident.**

**Why this one.** Competencies 2.11.1, 2.11.2, 2.11.5, and 2.11.8 are graded on your written log, and
the WebXam has four items on this outcome. This is what an entry that is worth reading looks like.

**Notice the part people leave out:** a theory that turned out to be wrong, and how it died. That is the
part that saves the next reader an hour, and it is the first thing that disappears when you write the
log after the problem is fixed.

**Open your own log before you start fixing anything.** Write the symptom while you are still looking at
it. The entry is then nearly finished when the bug is.

**Time.** 15 minutes. **Level.** On-level.

---

## 13. Industry connection: retries, timeouts, and the failure that spreads

**The Google SRE Book, the chapters on addressing cascading failures and on handling overload** ·
`https://sre.google/sre-book/addressing-cascading-failures/` · **[VERIFY]** before you assign it. The
book is free to read online with no account.

**Why this one.** Tuesday's lesson is a two-layer version of a problem that large systems have at
twenty layers. The chapter covers the same three ideas you worked this week, at production scale:
timeouts chosen against the layer below rather than by feel, retries that multiply load instead of
fixing it, and a degraded answer being better than no answer.

**The idea to bring back.** Retrying makes the thing you are retrying busier. In a room with thirty
clients and one model server, raising your retries is a decision about everybody's period, not only
yours.

**A second search, and it is the more current one: [VERIFY].** Look for a public post-incident write-up
where a retry storm or a timeout mismatch made an outage worse. Companies publish these on their
engineering blogs and status pages, they are free, and they are more specific than any textbook. Read
one and write three sentences in your decision log about what your own stack would do in the same shape
of failure.

**Time.** 40 minutes. **Level.** Extension.

---

## 14. A free video

**[VERIFY].** No specific video is named, because a title and a channel that are wrong waste more of
your time than no link.

**What to search for.** A video under 20 minutes on **HTTP status codes explained**, or on
**HttpClient timeout and cancellation in .NET**. Three tests before you commit to it:

1. It shows a request and a response, not only slides
2. It distinguishes 4xx from 5xx by whose fault it is, and says so out loud
3. If it is about .NET, it mentions that the timeout surfaces as a cancellation

**If you are behind on the C# rather than on the HTTP**, the .NET documentation pages in sections 2
through 5 have runnable examples on them, and reading a short example you can paste and run beats
watching somebody else type.

**Time.** Under 20 minutes. **Level.** Remediation.

---

## 15. Side quests and extensions

Two bundles fit this week, and both are in this repository.

**SQ-10 API First Contact** ·
[the bundle](../../../../Misc/side-quests/SQ-10-API-First-Contact/README.md) · **Confident.** Two
blocks, difficulty ★★. Consume a service, read the reply, print something a person wants, then break it
on purpose and make it fail gracefully. It ships its own practice service that runs on your own
computer, so it needs no internet and no account, and it needs no key.

**SQ-05 Bug Hunt** · [the bundle](../../../../Misc/side-quests/SQ-05-Bug-Hunt/README.md) ·
**Confident.** One block, difficulty ★★. Seven defects in a program somebody else wrote, and you may
fix but not rewrite. That constraint is the point, and it is the same skill Wednesday's lab asks for:
change one thing, verify, and leave the rest working.

### An extension that needs no bundle

**Make your own program tell you the answer.** Six lines, taken from Tuesday's example 3: read the
service's timeout and retry count from `/health`, multiply them, compare the result with your own
timeout, and print a warning when yours is smaller. The failure that used to cost twenty-one seconds of
silence now costs one command.

**Then break it deliberately and capture the output.** Set your client timeout below the service's
worst case, run it, and save what you saw. That capture is evidence for your troubleshooting log and it
is one of the four failures your demonstration has to show.

**Time.** One to two blocks for a quest, 30 minutes for the extension. **Level.** Extension.

---

## For the student who is behind

1. Monday's lecture notes, the table of four failure kinds, copied out by hand
2. The MDN status code page, the five codes named in section 7 and nothing else
3. [scenario.py](../05-labs/lab-m05-03-files/scenario.py) scenario 0, so you have seen the system work
   before you see it fail
4. Tuesday's self-check question 1, which is arithmetic and takes two minutes

## For the student who is ahead

- RFC 9110, and an argument in your decision log about whether 500 should be retryable in your stack
- The cascading failure reading in section 13, plus a public write-up you found yourself
- [bench.py](../05-labs/lab-m05-03-files/bench.py), and a measured number behind every processing
  requirement in your design
- SQ-10 API First Contact
