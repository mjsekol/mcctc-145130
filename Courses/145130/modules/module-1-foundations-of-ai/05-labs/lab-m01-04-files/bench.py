# bench.py  .  Lab M01-04 and the Module 1 performance task
#
# Measures what one language model costs on one machine, three numbers at a
# time. This file is finished. The arithmetic it depends on lives in
# measure.py, and that is the part you write.
#
#   python bench.py --label station-06 --repeats 3
#   python bench.py --label station-06 --endpoint http://127.0.0.1:11634
#
# WHAT IT MEASURES, AND WHAT EACH NUMBER IS FOR
#
#   total_latency_ms   send to last byte. The number a user feels when the
#                      answer appears all at once.
#   ttft_ms            send to the first piece of text. The number a user
#                      feels when the answer types itself out. Only
#                      measurable when the server streams.
#   tokens_per_second  tokens divided by the seconds spent generating, which
#                      is total latency MINUS time to first token. Dividing
#                      by total latency instead reports a rate the model
#                      never ran at.
#
# WHAT IT IS TIMING, AND WHAT IT IS NOT
#
# This program times the model server and nothing else. It sends a prompt and
# waits, and it does no parsing of its own beyond reading the reply's fields.
# That is deliberate: a benchmark that also parsed, retried, or validated
# could not tell you whether a slow answer was the model or your own code.
# Measure one thing at a time, and say which thing it was.
#
# WHAT IT REFUSES TO DO
#
# It never invents a number. When the server will not stream, time to first
# token is recorded as null and tokens per second is recorded as null, and
# the report says the server does not stream. A benchmark that fills a gap
# with a plausible guess is worse than one with a gap in it.

import argparse
import json
import os
import pathlib
import sys
import time
import urllib.error
import urllib.request

import measure

# Module 1 model stub port. 11434 is reserved for a real model and this
# module never defaults to it. See local-model-kit/README.md.
DEFAULT_ENDPOINT = os.environ.get("RIDGE_MODEL_URL", "http://127.0.0.1:11634")
DEFAULT_MODEL = os.environ.get("RIDGE_MODEL", "llama3.2")
PROMPTS_DIRECTORY = pathlib.Path(__file__).with_name("prompts")
RUNS_DIRECTORY = pathlib.Path(__file__).with_name("runs")
REQUEST_TIMEOUT_SECONDS = 120

# An assumption, printed in every report so nobody mistakes it for a
# measurement. Used only when the server gives no token counter and does not
# stream. Replace it with a real tokenizer count on lab hardware before you
# compare two different models with it.
CHARACTERS_PER_TOKEN_ASSUMED = 4.0

NO_STREAM_NOTE = ("this server does not stream, so time to first token and "
                  "tokens per second are not measurable here")
ASKED_NOT_TO_STREAM = ("streaming was switched off with --no-stream, so time to "
                       "first token and tokens per second were not measured")

DIRECT = urllib.request.build_opener(urllib.request.ProxyHandler({}))


class EndpointProblem(Exception):
    """The model endpoint could not be reached or refused the request."""


def load_prompts():
    files = sorted(PROMPTS_DIRECTORY.glob("*.txt"))
    if not files:
        raise EndpointProblem(f"no prompt files in {PROMPTS_DIRECTORY}")
    return [(f.stem, f.read_text(encoding="utf-8").strip()) for f in files]


def build_request(endpoint, model, prompt, stream):
    payload = json.dumps({"model": model, "prompt": prompt, "stream": stream})
    return urllib.request.Request(
        endpoint.rstrip("/") + "/api/generate",
        data=payload.encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST")


def count_tokens(text, reply_object):
    """Return (token_count, how_we_know). Never guess silently."""
    if isinstance(reply_object, dict) and isinstance(reply_object.get("eval_count"), int):
        return reply_object["eval_count"], "server_counter"
    return max(1, round(len(text) / CHARACTERS_PER_TOKEN_ASSUMED)), "character_estimate"


def one_streamed_call(endpoint, model, prompt):
    """Send one request with streaming on. Raises EndpointProblem on refusal."""
    request = build_request(endpoint, model, prompt, True)
    started = time.perf_counter()
    first_text_at = None
    chunks = 0
    pieces = []
    final = None
    try:
        with DIRECT.open(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            for line in response:
                line = line.strip()
                if not line:
                    continue
                try:
                    part = json.loads(line.decode("utf-8"))
                except json.JSONDecodeError:
                    continue
                piece = part.get("response", "")
                if piece:
                    if first_text_at is None:
                        first_text_at = time.perf_counter()
                    chunks += 1
                    pieces.append(piece)
                if part.get("done"):
                    final = part
    except urllib.error.HTTPError as error:
        body = error.read()[:120].decode("utf-8", "replace")
        error.close()
        raise EndpointProblem(
            f"the server refused a streaming request with HTTP {error.code}: {body}")
    except urllib.error.URLError as error:
        raise EndpointProblem(f"nothing answered at {endpoint}: {error.reason}") from error
    ended = time.perf_counter()

    text = "".join(pieces)
    token_count, how = count_tokens(text, final)
    if how == "character_estimate" and chunks > 1:
        token_count, how = chunks, "stream_chunks"
    return {
        "total_ms": round((ended - started) * 1000, 1),
        "ttft_ms": round((first_text_at - started) * 1000, 1) if first_text_at else None,
        "tokens": token_count,
        "token_source": how,
        "characters": len(text),
        "streamed": True,
    }


def one_plain_call(endpoint, model, prompt):
    """Send one request with streaming off. Time to first token is unknowable."""
    request = build_request(endpoint, model, prompt, False)
    started = time.perf_counter()
    try:
        with DIRECT.open(request, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        detail = error.read()[:120].decode("utf-8", "replace")
        error.close()
        raise EndpointProblem(f"the server answered HTTP {error.code}: {detail}")
    except urllib.error.URLError as error:
        raise EndpointProblem(f"nothing answered at {endpoint}: {error.reason}") from error
    ended = time.perf_counter()

    try:
        reply = json.loads(body)
    except json.JSONDecodeError:
        raise EndpointProblem(f"the reply was not JSON. First 120 characters: {body[:120]}")
    text = reply.get("response", "") if isinstance(reply, dict) else ""
    token_count, how = count_tokens(text, reply)
    return {
        "total_ms": round((ended - started) * 1000, 1),
        "ttft_ms": None,
        "tokens": token_count,
        "token_source": how,
        "characters": len(text),
        "streamed": False,
    }


def run_prompt(endpoint, model, prompt, repeats, want_stream, streaming_known_bad):
    """Run one prompt `repeats` times and return the samples and a note."""
    samples = []
    note = ""
    for _ in range(repeats):
        if want_stream and not streaming_known_bad:
            try:
                samples.append(one_streamed_call(endpoint, model, prompt))
                continue
            except EndpointProblem as problem:
                if "refused a streaming request" not in str(problem):
                    raise
                streaming_known_bad = True
                note = NO_STREAM_NOTE
        samples.append(one_plain_call(endpoint, model, prompt))
    return samples, note, streaming_known_bad


def summarise(samples):
    """Turn the repeats for one prompt into the numbers that go in the report."""
    totals = [s["total_ms"] for s in samples]
    ttfts = [s["ttft_ms"] for s in samples if s["ttft_ms"] is not None]
    median_total = measure.median(totals)
    median_ttft = measure.median(ttfts) if ttfts else None
    median_tokens = measure.median([float(s["tokens"]) for s in samples])
    generation = measure.generation_ms(median_total, median_ttft)
    return {
        "repeats": len(samples),
        "median_total_ms": median_total,
        "slowest_total_ms": max(totals) if totals else None,
        "fastest_total_ms": min(totals) if totals else None,
        "median_ttft_ms": median_ttft,
        "median_tokens": median_tokens,
        "generation_ms": generation,
        "tokens_per_second": measure.tokens_per_second(median_tokens or 0, generation),
        "token_source": samples[0]["token_source"] if samples else "",
        "streamed": samples[0]["streamed"] if samples else False,
    }


def main():
    parser = argparse.ArgumentParser(description="Measure one model on one machine.")
    parser.add_argument("--label", required=True,
                        help="a name for this machine, such as station-06")
    parser.add_argument("--endpoint", default=DEFAULT_ENDPOINT)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--repeats", type=int, default=3)
    parser.add_argument("--warmups", type=int, default=1,
                        help="requests sent and thrown away before timing starts")
    parser.add_argument("--no-stream", action="store_true",
                        help="do not even try to stream")
    parser.add_argument("--hardware", default="not recorded",
                        help="one line about this machine, typed by you")
    arguments = parser.parse_args()

    prompts = load_prompts()
    print(f"bench . {arguments.label} . {arguments.model} at {arguments.endpoint}")
    print(f"{len(prompts)} prompts, {arguments.repeats} timed repeats each, "
          f"{arguments.warmups} warm-up thrown away\n")

    streaming_known_bad = arguments.no_stream
    note = ASKED_NOT_TO_STREAM if arguments.no_stream else ""
    warmup_records = []
    try:
        for _ in range(arguments.warmups):
            name, text = prompts[0]
            started = time.perf_counter()
            if streaming_known_bad:
                one_plain_call(arguments.endpoint, arguments.model, text)
            else:
                try:
                    one_streamed_call(arguments.endpoint, arguments.model, text)
                except EndpointProblem as problem:
                    if "refused a streaming request" not in str(problem):
                        raise
                    streaming_known_bad = True
                    note = NO_STREAM_NOTE
                    one_plain_call(arguments.endpoint, arguments.model, text)
            warmup_records.append(round((time.perf_counter() - started) * 1000, 1))
    except EndpointProblem as problem:
        print(f"  {problem}")
        print("  Start a model server, or start the stub with: python stub_model_server.py")
        return 1

    if warmup_records:
        print(f"warm-up requests, not counted: "
              f"{', '.join(f'{ms} ms' for ms in warmup_records)}")
        print("The first request is usually the slowest. That is the model being "
              "loaded, not the model running.\n")

    results = {}
    try:
        for name, text in prompts:
            samples, prompt_note, streaming_known_bad = run_prompt(
                arguments.endpoint, arguments.model, text,
                arguments.repeats, not arguments.no_stream, streaming_known_bad)
            note = note or prompt_note
            results[name] = {"prompt_characters": len(text),
                             "samples": samples,
                             "summary": summarise(samples)}
    except EndpointProblem as problem:
        print(f"  {problem}")
        return 1

    if note:
        print(f"note: {note}\n")

    print("  prompt            median total   median ttft   tokens   tokens/sec   source")
    print("  " + "-" * 76)
    for name, block in results.items():
        summary = block["summary"]
        ttft = f"{summary['median_ttft_ms']} ms" if summary["median_ttft_ms"] is not None else "n/a"
        rate = summary["tokens_per_second"] if summary["tokens_per_second"] is not None else "n/a"
        print(f"  {name:<17} {summary['median_total_ms']:>9} ms {ttft:>13} "
              f"{summary['median_tokens']:>8} {str(rate):>12}   {summary['token_source']}")

    spread = [round(block["summary"]["slowest_total_ms"]
                    - block["summary"]["fastest_total_ms"], 1)
              for block in results.values()]
    print(f"\n  widest gap between the fastest and slowest repeat of one prompt: "
          f"{max(spread)} ms")
    print("  If that gap is large next to the medians, your repeats are not "
          "measuring the same thing.")

    record = {
        "label": arguments.label,
        "model": arguments.model,
        "endpoint": arguments.endpoint,
        "hardware_note": arguments.hardware,
        "method": {
            "prompt_set": [name for name, _ in prompts],
            "repeats": arguments.repeats,
            "warmups": arguments.warmups,
            "streamed": not streaming_known_bad,
            "characters_per_token_assumed": CHARACTERS_PER_TOKEN_ASSUMED,
            "note": note,
        },
        "warmup_ms": warmup_records,
        "results": results,
    }
    RUNS_DIRECTORY.mkdir(exist_ok=True)
    out = RUNS_DIRECTORY / f"{arguments.label}.json"
    out.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"\n  Wrote {out.as_posix()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
