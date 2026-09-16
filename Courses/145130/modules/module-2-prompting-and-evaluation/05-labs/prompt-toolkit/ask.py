# ask.py  ·  145130 Module 2 prompt toolkit
#
# Send one prompt to a locally hosted model and record exactly what came back.
#
# WHY THIS EXISTS
#   You cannot compare five prompts from memory. You will remember the reply
#   you liked and forget the three that were nearly the same. This tool writes
#   every run to a file so the comparison is made from evidence instead of
#   from an impression.
#
# WHAT IT NEVER DOES
#   It never sends anything to a commercial service. The endpoint defaults to
#   your own machine. It never puts a name, an ID, a grade, or any other
#   personal detail in a file: what goes in the prompt file is what gets
#   recorded, so keep people out of your prompt files.
#
# Usage:
#   python ask.py --prompt-file prompts/v1.txt --label v1
#   python ask.py --prompt-file prompts/v1.txt --label v1 --runs-dir runs
#   python ask.py --prompt-file prompts/v1.txt --label v1 --endpoint http://127.0.0.1:11500
#   python ask.py --prompt "one line prompt" --label quick
#
# Exit codes, so a script can tell the failures apart:
#   0  the model answered and the reply is usable
#   2  nothing is listening at the endpoint
#   3  the server answered with an HTTP error
#   4  the server answered with something that is not valid JSON
#   5  the reply parsed but is not usable (no response field, empty, not done)
#   6  the server did not answer inside the timeout

import argparse
import json
import pathlib
import sys
import time
import urllib.error
import urllib.request

DEFAULT_ENDPOINT = "http://127.0.0.1:11434"
DEFAULT_MODEL = "stub-caricature"
DEFAULT_TIMEOUT_SECONDS = 20.0
GENERATE_PATH = "/api/generate"
MAX_RATE_LIMIT_RETRIES = 3
DEFAULT_RETRY_AFTER = 5

EXIT_OK = 0
EXIT_UNREACHABLE = 2
EXIT_HTTP_ERROR = 3
EXIT_MALFORMED = 4
EXIT_UNUSABLE = 5
EXIT_TIMEOUT = 6


class AskError(Exception):
    """A failure with an exit code attached, so main() can report it cleanly."""

    def __init__(self, code, message, detail=""):
        super().__init__(message)
        self.code = code
        self.message = message
        self.detail = detail


def send(prompt, endpoint, model, timeout_seconds):
    """Send one prompt. Return (reply_text, elapsed_seconds, raw_reply).

    Every failure this can hit is caught separately, because "it did not work"
    is not a useful thing to write in a decision log. Which way it did not work
    is.
    """
    body = json.dumps({"model": model, "prompt": prompt, "stream": False}).encode("utf-8")
    request = urllib.request.Request(
        endpoint.rstrip("/") + GENERATE_PATH,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )

    attempts = 0
    while True:
        attempts += 1
        started = time.monotonic()
        try:
            with urllib.request.urlopen(request, timeout=timeout_seconds) as response:
                raw = response.read().decode("utf-8")
            elapsed = time.monotonic() - started
            break
        except urllib.error.HTTPError as error:
            elapsed = time.monotonic() - started
            if error.code == 429 and attempts <= MAX_RATE_LIMIT_RETRIES:
                wait = to_int(error.headers.get("Retry-After"), DEFAULT_RETRY_AFTER)
                print(f"  rate limited, waiting {wait}s and trying again "
                      f"(attempt {attempts} of {MAX_RATE_LIMIT_RETRIES})")
                time.sleep(wait)
                continue
            raise AskError(EXIT_HTTP_ERROR,
                           f"the server answered HTTP {error.code}",
                           error.reason or "")
        except TimeoutError:
            raise AskError(EXIT_TIMEOUT,
                           f"no answer inside {timeout_seconds:.0f} seconds",
                           "a local model on a slow machine can genuinely need longer")
        except urllib.error.URLError as error:
            # A timeout can arrive wrapped in a URLError on some versions.
            if isinstance(error.reason, TimeoutError):
                raise AskError(EXIT_TIMEOUT, f"no answer inside {timeout_seconds:.0f} seconds", "")
            raise AskError(EXIT_UNREACHABLE,
                           f"nothing is listening at {endpoint}",
                           "start the model server, or the stub, and try again")

    try:
        reply = json.loads(raw)
    except ValueError:
        raise AskError(EXIT_MALFORMED,
                       "the server answered with something that is not valid JSON",
                       raw[:120])
    if not isinstance(reply, dict):
        raise AskError(EXIT_MALFORMED, "the reply is valid JSON but not an object", raw[:120])

    if "response" not in reply:
        raise AskError(EXIT_UNUSABLE, "the reply has no 'response' field",
                       "keys present: " + ", ".join(sorted(reply)))
    if reply.get("done") is not True:
        raise AskError(EXIT_UNUSABLE, "the reply is not marked done",
                       "a partial reply is not a short reply")
    text = reply["response"]
    if not isinstance(text, str) or not text.strip():
        raise AskError(EXIT_UNUSABLE, "the reply is empty",
                       "an empty reply is a failure, not a short answer")

    return text, elapsed, reply


def to_int(value, fallback):
    try:
        return max(0, int(value))
    except (TypeError, ValueError):
        return fallback


def record(runs_dir, label, prompt, text, elapsed, reply, endpoint, model):
    """Write one run to runs/<label>.json and append a line to runs/run_log.md.

    No clock time is stored on purpose. A file with a date in it stops being
    reusable next year, and the number you actually compare is elapsed seconds.
    """
    runs_dir.mkdir(parents=True, exist_ok=True)
    run = {
        "label": label,
        "endpoint": endpoint,
        "model": model,
        "prompt": prompt,
        "response": text,
        "elapsed_seconds": round(elapsed, 3),
        "prompt_words": len(prompt.split()),
        "response_words": len(text.split()),
        "server_prompt_eval_count": reply.get("prompt_eval_count"),
        "server_eval_count": reply.get("eval_count"),
    }
    path = runs_dir / f"{label}.json"
    path.write_text(json.dumps(run, indent=2), encoding="utf-8")

    log = runs_dir / "run_log.md"
    if not log.exists():
        log.write_text("# Run log\n\n| Label | Prompt words | Reply words | Seconds |\n"
                       "|---|---|---|---|\n", encoding="utf-8")
    with log.open("a", encoding="utf-8") as handle:
        handle.write(f"| {label} | {run['prompt_words']} | {run['response_words']} | "
                     f"{run['elapsed_seconds']:.2f} |\n")
    return path


def main(argv=None):
    parser = argparse.ArgumentParser(description="Send one prompt to a local model and record the run.")
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--prompt-file", help="a text file holding the whole prompt")
    source.add_argument("--prompt", help="the prompt on the command line, for quick checks")
    parser.add_argument("--label", required=True, help="the name this run is filed under")
    parser.add_argument("--runs-dir", default="runs")
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--timeout", type=float, default=DEFAULT_TIMEOUT_SECONDS)
    parser.add_argument("--show", action="store_true", help="print the whole reply")
    arguments = parser.parse_args(argv)

    if arguments.prompt_file:
        path = pathlib.Path(arguments.prompt_file)
        if not path.exists():
            print(f"FAILED: there is no file at {path}")
            return EXIT_UNREACHABLE
        prompt = path.read_text(encoding="utf-8")
    else:
        prompt = arguments.prompt

    if not prompt.strip():
        print("FAILED: the prompt is empty. An empty prompt is not a control run.")
        return EXIT_UNUSABLE

    print(f"[{arguments.label}] {len(prompt.split())} prompt words to {arguments.endpoint}")
    try:
        text, elapsed, reply = send(prompt, arguments.endpoint, arguments.model, arguments.timeout)
    except AskError as error:
        print(f"FAILED ({error.message})")
        if error.detail:
            print(f"  {error.detail}")
        return error.code

    runs_dir = pathlib.Path(arguments.runs_dir)
    path = record(runs_dir, arguments.label, prompt, text, elapsed, reply,
                  arguments.endpoint, arguments.model)
    print(f"  {len(text.split())} reply words in {elapsed:.2f}s, recorded in {path}")
    if arguments.show:
        print("-" * 60)
        print(text)
        print("-" * 60)
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
