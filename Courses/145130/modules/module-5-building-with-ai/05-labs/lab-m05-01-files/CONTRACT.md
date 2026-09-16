# The contract · contract-demo-service

This file is the contract for the demo service in this folder. Read it before
you write anything that calls a service, and read it with a terminal open.

**The service it describes is a teaching prop.** It has one task, one result
field, one validation rule, and a parser that handles one of the four shapes a
model really answers in. It is here so you can trace a finished contract before
you write your own, not so you can copy it.

**What you should copy is the shape of this document**, because your own
specification has to do the same job: tell somebody who has never seen your code
exactly what to send, exactly what comes back, and exactly what every failure is
called.

---

## 1. The service

| Item | Value |
|---|---|
| Name | `contract-demo-service`, version 1.0 |
| Base URL | `http://127.0.0.1:5157`, or whatever `DEMO_SERVICE_HOST` and `DEMO_SERVICE_PORT` say |
| Transport | HTTP, JSON in and JSON out, UTF-8 |
| Authentication | none, and none is ever added, because the model is local |
| Endpoints | `GET /health`, `POST /generate` |
| Tasks | `headline` |
| State kept | none |

### GET /health

Why it exists: you need to know whether the service is up, and **separately**
whether it can see a model, before you start blaming your own code. Those are two
different problems with two different fixes.

`/health` never asks the model to generate anything. It opens a TCP connection to
the model endpoint, sees whether it connects, and closes it. A health check that
costs an inference is a health check nobody runs.

It answers HTTP 200 whenever the service itself is running.

```json
{
  "service": "contract-demo-service",
  "version": "1.0",
  "status": "ok",
  "model_endpoint": "http://127.0.0.1:11535",
  "model": "stub",
  "model_reachable": true,
  "checked_by": "tcp_connect",
  "timeout_seconds": 20.0,
  "retries": 1,
  "tasks": ["headline"]
}
```

**`model_reachable` false means the service is running and every answer you get
back will be a fallback.** It also does not tell you that the thing listening is
a model. It tells you something is listening. You will meet the difference in
Week 14.

**`timeout_seconds` and `retries` are there for you to read.** The service's worst
case is the timeout multiplied by one more than the retries. Your own program's
timeout has to be larger than that number, and Week 14 Tuesday is about why.

---

## 2. The request

`POST /generate` takes one JSON object with two fields.

```json
{"task": "headline", "prompt": "The 3D printer in room 118 jammed near the nozzle."}
```

| Field | Type | Rules |
|---|---|---|
| `task` | string | must be `headline`. Case and outer spaces are ignored. |
| `prompt` | string | 1 to 4000 characters after control characters and outer whitespace are removed |

The whole body is capped at 16384 bytes and anything larger is refused before it
is read. Length is checked on the raw text, before any work is done with it,
because work done on input you have not checked is work you may have to undo.

---

## 3. The response envelope

Every response from `/generate` has these six fields, in this order, for every
outcome. **That is the point of a service.** Your program writes one deserialiser
and it always works.

```json
{
  "ok": true,
  "task": "headline",
  "result": {"headline": "Stub headline: The 3D printer in room 118 jammed near the nozzle."},
  "source": "model",
  "elapsed_ms": 32,
  "error": null
}
```

| Field | Type | Meaning |
|---|---|---|
| `ok` | bool | true when `result` holds a usable answer for the task |
| `task` | string | the task that ran, echoed back |
| `result` | object or null | the task's result shape. Null only when `ok` is false. |
| `source` | string | `model`, `fallback`, or `none` |
| `elapsed_ms` | int | how long the service spent on this request, including any retry |
| `error` | object or null | `{"kind": "...", "message": "..."}` |

### Read `source` first

**`ok` and `error` are not opposites.** This is the single thing about this
contract that people get wrong, and getting it wrong produces a program that
presents a sentence written by a keyword rule as though a model wrote it.

| `source` | `ok` | `error` | What happened |
|---|---|---|---|
| `model` | true | null | the model answered and the answer fit the task |
| `fallback` | true | **set** | the model did not give a usable answer, so the service built one without it |
| `none` | false | set | the service refused the request, and never called the model |

**HTTP status:** 200 whenever `ok` is true. 400 for a refused request, 413 for a
body over the cap, 404 and 405 for a wrong path or method. Every one of those
still carries the envelope, so a caller never has to parse an error page.

---

## 4. The result shape

### headline

```json
{"headline": "Stub headline: The 3D printer in room 118 jammed near the nozzle."}
```

| Field | Type | Rules |
|---|---|---|
| `headline` | string | 15 to 120 characters, not empty |

**Only one field, on purpose.** Your own result shape will have more, and every
field you add is another row in your specification and another rule in your
validator.

An answer shorter than 15 characters, or an answer the service could not find a
headline in at all, is treated as a failed answer and you get the fallback
instead. That is a deliberate choice: a headline of two characters renders on a
screen and tells nobody anything.

---

## 5. Error kinds

Every kind is a fixed string. **Branch on `kind` in code. Show `message` to a
person.** That split is why they are two fields.

### Kinds that mean the model let you down. `source` is `fallback`, `ok` is still true.

| Kind | Cause | Retried |
|---|---|---|
| `connection_refused` | nothing is listening at the model endpoint | yes |
| `unreachable` | the address does not resolve, or the route failed | yes |
| `timeout` | no answer within `timeout_seconds` | yes |
| `rate_limited` | the model server answered 429 | yes |
| `model_http_error` | any other non-200 status from the model server | no |
| `malformed_json` | the body was not valid JSON, or was not an object | no |
| `missing_field` | no `response` string, or `done` was not true | no |
| `empty_response` | the answer was empty once cleaned | no |
| `response_too_long` | over 8000 characters, so the model ignored the instructions | no |
| `task_validation_failed` | the answer arrived and did not fit the task's rules | no |

**The retried column is the design decision.** Trying again helps when the
problem might be temporary. Trying again on a broken reply gets you the same
broken reply and costs somebody another twenty seconds of a period.

### Kinds that mean your request was wrong. `source` is `none`, `ok` is false.

| Kind | HTTP | Cause |
|---|---|---|
| `bad_request` | 400 | the body was not a JSON object, or a field was missing or the wrong type |
| `unknown_task` | 400 | the task name is not one the service knows |
| `prompt_too_long` | 400 | over 4000 characters |
| `prompt_empty` | 400 | nothing left after control characters and whitespace were removed |
| `body_too_large` | 413 | over 16384 bytes |
| `not_found` | 404 | wrong path |
| `method_not_allowed` | 405 | right path, wrong method |

**On all of these, `elapsed_ms` is 0.** The service checked the request and
returned before calling the model, so there was nothing to time and nothing was
spent.

---

## 6. What a caller owes the person

If you write a program against this service, you owe the person using it **four
distinct messages**, because these are four different problems with four
different fixes.

1. **The service is not running.** Tell them the command that starts it.
2. **The service did not answer in time.** Say how long you waited.
3. **The service answered with a status and no usable envelope.**
4. **The service answered with something that is not the envelope at all.** The
   usual cause is pointing at the wrong port, such as the model endpoint. Print
   the first 120 characters of what you received.

Separately, **`source: "fallback"` is not one of those four.** It is a successful
call. Show the answer, and say plainly that it did not come from the model.

---

## 7. Settings

All optional. Environment variables, never values typed into the code.

| Variable | Read by | Default | Meaning |
|---|---|---|---|
| `DEMO_MODEL_URL` | the service | `http://127.0.0.1:11535` | where the model listens |
| `DEMO_MODEL` | the service | `stub` | which model to ask for |
| `DEMO_MODEL_TIMEOUT` | the service | `20` | seconds to wait for one model answer |
| `DEMO_MODEL_RETRIES` | the service | `1`, capped at 3 | retries after the first try |
| `DEMO_SERVICE_HOST` | the service | `127.0.0.1` | where the service listens |
| `DEMO_SERVICE_PORT` | the service | `5157` | the service port |
| `DEMO_SERVICE_URL` | a client | `http://127.0.0.1:5157` | where a client looks for the service |

**Use `127.0.0.1`, not `localhost`.** On the Windows machine this was built on, a
refused connection to `localhost` took about twice as long as the same refusal to
`127.0.0.1`, because Windows tries IPv6 first. When the model is not running,
that difference is most of the response time.

---

## 8. What this contract deliberately leaves out

Your own specification will need these. This one does not have them, and saying
so is part of being honest about what a prop is.

- **More than one task.** Adding a second task means a second result shape, a
  second parser, and a second set of rules.
- **A result shape with more than one field.** Every field is another row here
  and another rule in the validator.
- **A parser worth the name.** The service behind this contract handles fenced
  JSON and nothing else. You will watch it throw away three perfectly good
  answers in this lab.
- **Anything about what the model is good at.** A contract says what crosses a
  boundary. It says nothing about quality, and quality is not something a
  specification can promise.
