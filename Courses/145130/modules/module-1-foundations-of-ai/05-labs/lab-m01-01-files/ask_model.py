# ask_model.py  .  Lab M01-01, the side you do not write
#
# This file is finished. You are not asked to change it. It is here so you can
# read how one program asks a model server for an answer, and so the
# comparison in compare.py has something to compare against.
#
# It posts one help request to the model endpoint and gets back one field of
# TEXT. Everything after that is this program making sense of text, which is
# the part people underestimate.
#
#   python ask_model.py
#
# Start the stub first:  python stub_model_server.py --port 11634
# The address comes from RIDGE_MODEL_URL, or 127.0.0.1:11634.
#
# THE PROMPT MATTERS AND IT IS NOT MAGIC
#
# build_prompt below writes an instruction, names the task on its own line,
# and wraps the ticket text in markers so the model can tell the instruction
# apart from the data. Our stand-in server looks for that task line to decide
# which shape to answer with. A real model reads the whole thing. Module 2 is
# three weeks on writing this well.
#
# WHAT THIS PROGRAM RECORDS, AND WHY
#
# Every answer carries a `how` field: json, prose, or unparsed. Nothing gives
# you that for free. If your program does not record how it got a value, then
# three weeks later nobody can tell a label the model produced from a label
# your code guessed at.

import json
import os
import re
import urllib.error
import urllib.request

MODEL_URL = os.environ.get("RIDGE_MODEL_URL", "http://127.0.0.1:11634").rstrip("/")
MODEL_NAME = os.environ.get("RIDGE_MODEL", "llama3.2")
REQUEST_TIMEOUT_SECONDS = 30

LABELS = ["hardware", "software", "network", "account", "other"]

FENCE = re.compile(r"```[a-zA-Z0-9_-]*\n(.*?)```", re.DOTALL)
LABEL_LINE = re.compile(r"^\s*label\s*:\s*(.+?)\s*$", re.I | re.M)

DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))


class ModelProblem(Exception):
    """The model server could not be reached, or did not answer usefully."""


def build_prompt(text):
    """Build the whole input the model sees. The ticket is data, not instruction."""
    return (
        "You sort help requests for a school makerspace.\n"
        f"Answer with JSON only: {{\"label\": one of {LABELS}}}.\n"
        "Task: classify\n"
        "<<<TEXT\n"
        f"{text}\n"
        "TEXT\n"
    )


def ask(text):
    """Send one request. Return the model's raw answer text."""
    payload = {"model": MODEL_NAME, "prompt": build_prompt(text), "stream": False}
    request = urllib.request.Request(
        MODEL_URL + "/api/generate",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST")
    try:
        with DIRECT.open(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8")[:120]
        error.close()
        raise ModelProblem(f"the server answered HTTP {error.code}: {detail}")
    except urllib.error.URLError as error:
        raise ModelProblem(
            f"nothing answered at {MODEL_URL}. Start it with: "
            f"python stub_model_server.py --port 11634  ({error.reason})")
    except TimeoutError:
        raise ModelProblem(f"{MODEL_URL} did not answer within "
                           f"{REQUEST_TIMEOUT_SECONDS} seconds")

    try:
        reply = json.loads(body)
    except json.JSONDecodeError:
        raise ModelProblem(f"the reply was not JSON. First 120 characters: {body[:120]}")
    if not isinstance(reply, dict) or reply.get("done") is not True:
        raise ModelProblem("the reply did not say done: true, so the answer is unfinished")
    answer = reply.get("response")
    if not isinstance(answer, str) or answer.strip() == "":
        raise ModelProblem("the reply had no response text in it")
    return answer


def read_label(answer):
    """Pull a label out of the model's text. Return (label, how).

    Three routes, tried in order, and the one that worked is recorded:
      json     the answer contained a JSON object with a label
      prose    no JSON, but a line started with Label:
      unparsed nothing usable, and we refuse to guess
    """
    fenced = FENCE.search(answer)
    candidate = fenced.group(1) if fenced else answer
    try:
        data = json.loads(candidate.strip())
        if isinstance(data, dict) and isinstance(data.get("label"), str):
            return data["label"].strip().lower(), "json"
    except json.JSONDecodeError:
        pass

    line = LABEL_LINE.search(answer)
    if line:
        return line.group(1).strip().lower(), "prose"

    return None, "unparsed"


def classify_one(text):
    """Ask the model to label one help request. Never invents a label."""
    answer = ask(text)
    label, how = read_label(answer)
    if label is not None and label not in LABELS:
        # A label outside the list is not a label. A program that writes a
        # made-up category into a database is worse than one that refuses.
        return {"label": None, "how": "off_list", "raw": answer.strip()[:160],
                "rejected": label}
    return {"label": label, "how": how, "raw": answer.strip()[:160], "rejected": None}


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "tickets.json"), encoding="utf-8") as handle:
        tickets = json.load(handle)["tickets"]

    print(f"model endpoint {MODEL_URL}, model {MODEL_NAME}\n")
    for ticket in tickets:
        try:
            answer = classify_one(ticket["text"])
        except ModelProblem as problem:
            print(f"  {ticket['id']}  {problem}")
            return 1
        shown = answer["label"] if answer["label"] else "no label"
        print(f"  {ticket['id']}  {shown:<9} read from {answer['how']}")
        if answer["rejected"]:
            print(f"            the model said '{answer['rejected']}', which is not on the list")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
