# seam_report.py  .  Lab M01-02, the seam between your program and a model
#
# A seam is the place where a new system is bolted onto the systems already
# there. Yours is one HTTP call to a model server. This program stands at that
# seam and makes the model fail on purpose, one failure at a time, so you can
# write down what the person at the keyboard actually sees.
#
# Nothing sits between you and the model here. There is no service catching
# failures for you, which means the failure policy is yours to write. That is
# the lab.
#
# The plumbing below is finished. THREE THINGS ARE NOT, and they are the lab:
#
#   step 4  MODES_TO_TEST     which failures you are going to force
#   step 5  kind_of()         name what happened, from what you can observe
#   step 6  sentence_for()    the sentence a person should read for each kind
#   step 7  should_retry()    the rule for when trying again could help
#
#   python seam_report.py
#
# Needs the stub running:  python stub_model_server.py --port 11634 --delay 6
# The address comes from RIDGE_MODEL_URL, or 127.0.0.1:11634.

import json
import os
import time
import urllib.error
import urllib.request

# Module 1 port. 11434 is reserved for a real model and this module never
# uses it. See local-model-kit/README.md.
MODEL_URL = os.environ.get("RIDGE_MODEL_URL", "http://127.0.0.1:11634").rstrip("/")
MODEL_NAME = os.environ.get("RIDGE_MODEL", "llama3.2")
REQUEST_TIMEOUT_SECONDS = 5
REPORT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "seam_report.md")

# One help request, used for every mode, so the only thing changing between
# rows is the failure. Invented sample, not a real person.
TICKET = ("My laptop keeps dropping the wifi in the back corner of the lab. "
          "It reconnects after about a minute.")

# Every mode the stub can be put into. Read the stub's own comment block for
# what each one does before you choose.
ALL_MODES = ["success", "success_prose", "unusable", "slow", "error",
             "rate_limited", "malformed", "not_done", "missing_response",
             "empty_response"]

# The names you may use in kind_of. Do not invent others: a fixed list is what
# lets a later program branch on the answer.
KINDS = ["ok", "http_error", "rate_limited", "malformed_json", "not_done",
         "no_response_field", "empty_response", "timeout", "refused"]

DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))


# TODO step 4. Choose at least five modes. One of them must be slow, and you
# have to decide what --delay the stub runs with so the period does not end
# while you wait. Write down the reason for your choice in the report.
MODES_TO_TEST = ["success"]


def kind_of(observation):
    """Name what happened, using only what a caller can actually observe.

    observation has: status (int or None), raw (str or None), transport (str
    or None). transport is set when no HTTP reply arrived at all.

    TODO step 5. Return one of KINDS. Work from the outside in: did anything
    arrive, was the status 200, was the body JSON, did it say done, was there
    response text.
    """
    return "ok"


def sentence_for(kind):
    """Return the one sentence a person at the keyboard should read.

    TODO step 6. Every sentence names exactly one thing that person can do.
    Two different problems with two different fixes may not share a sentence.
    Two problems with the same fix may.
    """
    return "something happened"


def should_retry(kind):
    """Return True when sending the same request again could come out differently.

    TODO step 7. This is a rule, not a list. Write the rule in your report in
    one sentence, then make this function match it.
    """
    return False


def set_mode(mode):
    """Switch the stub into a mode while it is running."""
    post(MODEL_URL + "/stub/mode", {"mode": mode})


def calls_so_far():
    """How many times the stub has been asked to generate. Proves a retry."""
    with DIRECT.open(MODEL_URL + "/stub/stats", timeout=10) as response:
        return json.loads(response.read().decode("utf-8"))["generate_calls"]


def post(url, body):
    request = urllib.request.Request(
        url, data=json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    with DIRECT.open(request, timeout=10) as response:
        return response.read().decode("utf-8")


def send_once():
    """Send one request. Return what a caller can observe, and nothing more."""
    payload = {"model": MODEL_NAME, "prompt": TICKET, "stream": False}
    request = urllib.request.Request(
        MODEL_URL + "/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"}, method="POST")
    started = time.perf_counter()
    try:
        with DIRECT.open(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            raw = response.read().decode("utf-8")
            status = response.status
        transport = None
    except urllib.error.HTTPError as error:
        status, raw, transport = error.code, error.read().decode("utf-8"), None
        error.close()
    except TimeoutError:
        status, raw, transport = None, None, "timeout"
    except urllib.error.URLError as error:
        reason = error.reason
        status, raw = None, None
        transport = "timeout" if isinstance(reason, TimeoutError) else "refused"
    elapsed_ms = round((time.perf_counter() - started) * 1000, 1)
    return {"status": status, "raw": raw, "transport": transport,
            "elapsed_ms": elapsed_ms}


def attempt(max_attempts=2):
    """Send, and send again when your own rule says a retry could help."""
    for attempt_number in range(1, max_attempts + 1):
        observation = send_once()
        kind = kind_of(observation)
        if not should_retry(kind) or attempt_number == max_attempts:
            return observation, kind, attempt_number
        time.sleep(1)


def main():
    rows = []
    for mode in MODES_TO_TEST:
        set_mode(mode)
        before = calls_so_far()
        observation, kind, attempts = attempt()
        after = calls_so_far()
        rows.append({
            "mode": mode,
            "http": observation["status"] if observation["status"] else "none",
            "kind": kind,
            "retried": "yes" if attempts > 1 else "no",
            "model_calls": after - before,
            "elapsed_ms": observation["elapsed_ms"],
            "sentence": sentence_for(kind),
        })

    header = ("| stub mode | HTTP | kind | retried | model calls | elapsed ms "
              "| what the person reads |")
    lines = [header, "|---|---|---|---|---|---|---|"]
    for row in rows:
        lines.append(f"| {row['mode']} | {row['http']} | {row['kind']} | "
                     f"{row['retried']} | {row['model_calls']} | "
                     f"{row['elapsed_ms']} | {row['sentence']} |")
    table = "\n".join(lines)
    print(table)

    with open(REPORT_FILE, "w", encoding="utf-8") as handle:
        handle.write("# Seam report\n\nOne help request, sent once per stub "
                     "mode. Only the failure changes.\n\n" + table + "\n")
    print(f"\nWrote {os.path.basename(REPORT_FILE)}.")
    set_mode("success")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
