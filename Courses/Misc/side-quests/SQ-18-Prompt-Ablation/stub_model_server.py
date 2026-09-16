# stub_model_server.py  ·  145130 Module 2 prompt toolkit
#
# A stand-in for a locally hosted language model. It answers
# POST /api/generate the way an Ollama-compatible server does, with no model
# behind it, so every lab in this module runs on a machine that has nothing
# installed.
#
# WHAT THIS IS NOT
#   This is not a language model. It is a caricature of one. It reacts to the
#   same five prompt elements a real model reacts to (role, task, context,
#   format, constraints) and it fabricates sources when you ask for sources
#   without giving it any. It does that deterministically, from templates, so
#   the same prompt always produces the same reply.
#
#   Everything you learn here about WHICH prompt element changed the output is
#   real. Nothing you learn here about HOW GOOD a real model's wording is, is
#   real. Run the same prompts against the lab's local model when it is
#   available and compare.
#
# EVERY SOURCE THIS SERVER PRODUCES IS INVENTED. None of the journals,
# authors, volumes, or page numbers are real. They are built from templates on
# purpose, because a fabricated citation you can study is safer than one you
# went looking for.
#
# Usage:
#   python stub_model_server.py                          success mode, port 11434
#   python stub_model_server.py --mode slow --delay 30   answers too late
#   python stub_model_server.py --mode rate_limited      429 with Retry-After
#   python stub_model_server.py --port 11500 --mode error
#
# Modes:
#   success           a reply that responds to the prompt's elements
#   slow              waits --delay seconds, then replies like success
#   error             HTTP 500
#   malformed         status 200, but the body is broken JSON
#   rate_limited      HTTP 429 with a Retry-After header
#   not_done          valid JSON with done: false
#   missing_response  valid JSON with no "response" field
#   empty_response    valid JSON whose response is only spaces
#
# Extra endpoints a real server does not have:
#   GET  /stub/stats   {"generate_calls": 3, "mode": "success"}
#   GET  /stub/parse   ?prompt=...  shows which elements the stub detected
#   POST /stub/mode    send {"mode": "error"} to switch modes while running

import argparse
import json
import re
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

DEFAULT_HOST = "127.0.0.1"   # loopback only: nobody else on the network can reach it
DEFAULT_PORT = 11434
DEFAULT_DELAY_SECONDS = 30.0
RETRY_AFTER_SECONDS = 4

SUCCESS = "success"
SLOW = "slow"
ERROR = "error"
MALFORMED = "malformed"
RATE_LIMITED = "rate_limited"
NOT_DONE = "not_done"
MISSING_RESPONSE = "missing_response"
EMPTY_RESPONSE = "empty_response"
MODES = [SUCCESS, SLOW, ERROR, MALFORMED, RATE_LIMITED,
         NOT_DONE, MISSING_RESPONSE, EMPTY_RESPONSE]

GENERATE_PATH = "/api/generate"
TAGS_PATH = "/api/tags"
STATS_PATH = "/stub/stats"
PARSE_PATH = "/stub/parse"
MODE_PATH = "/stub/mode"

STUB_MODEL_NAME = "stub-caricature"


# ---------------------------------------------------------------------------
# Reading the prompt
#
# A real model does not "detect elements." It predicts text, and text that
# follows a role line and a format instruction ends up different from text
# that does not. The stub fakes that outcome with regular expressions so the
# difference is observable with no model installed.
# ---------------------------------------------------------------------------

ROLE_PATTERN = re.compile(
    r"\byou are (?:an?|the)\s+(.{3,60}?)(?=\s+(?:and|who|with|that)\b|[.,;\n]|$)", re.I)
NO_INTRO_PATTERN = re.compile(r"\b(?:do not|don't|no)\s+(?:add|include|write|give me)?\s*"
                              r"(?:an?\s+)?(?:introduction|intro|preamble|"
                              r"closing paragraph|conclusion)", re.I)
AUDIENCE_PATTERN = re.compile(r"\bfor (?:a|an|the)\s+((?:[a-z-]+\s+){0,3}"
                              r"(?:freshman|ninth grader|senior|parent|teacher|"
                              r"principal|beginner|expert|engineer|reader))", re.I)
WORD_CAP_PATTERN = re.compile(r"\b(?:under|at most|no more than|fewer than|max(?:imum)? of)\s+(\d{1,4})\s+words", re.I)
STEP_COUNT_PATTERN = re.compile(r"\b(?:exactly|give me|write|list)\s+(\d{1,2})\s+(?:steps|numbered steps|items|bullets)", re.I)
JSON_PATTERN = re.compile(r"\bjson\b", re.I)
NUMBERED_PATTERN = re.compile(r"\bnumbered (?:list|steps)\b", re.I)
BULLET_PATTERN = re.compile(r"\bbullet(?:s| points| list)\b", re.I)
# "as a table" is a format instruction. "hash table" is a topic. The verb in
# front is what tells them apart, and without it the stub formats a study plan
# about hash tables as a table, which is a real bug this file used to have.
TABLE_PATTERN = re.compile(
    r"\b(?:markdown table|(?:as|in|into|using|return|give me|write|format(?:ted)? as|"
    r"present(?:ed)? as|put it in)\s+(?:an?\s+)?(?:markdown\s+)?table)\b", re.I)
EXAMPLE_PATTERN = re.compile(r"^\s*(?:example|for example|here is an example)\b", re.I | re.M)
CITE_PATTERN = re.compile(r"\b(?:cite|citation|citations|sources?|references?|bibliograph)", re.I)
GROUNDING_PATTERN = re.compile(r"\b(?:only use|use only|using only|based only on|answer only from|"
                               r"only from the (?:notes|sources|text|passage|list)|"
                               r"from the (?:notes|sources|text|passage|list) below|"
                               r"do not use anything else|restricted to the sources)\b", re.I)
# "Return JSON" and "return ONLY JSON" are different instructions, and the
# difference is the whole Thursday lesson. Without the second one, a model
# usually wraps the JSON in a friendly sentence and the parser breaks.
JSON_ONLY_PATTERN = re.compile(r"\b(?:only json|json only|no other text|nothing else|"
                               r"no prose|no explanation|output only the json|"
                               r"return only the json)\b", re.I)
SOURCE_LINE_PATTERN = re.compile(r"^\s*SOURCE:\s*(.+)$", re.M)
REFUSE_PATTERN = re.compile(r"\b(?:say|write|reply with) ['\"]?(?:I do not know|not in the sources|no source)['\"]?", re.I)
KEYS_PATTERN = re.compile(r"\bkeys?\s*[:\-]?\s*([a-z_]+(?:\s*,\s*[a-z_]+)+)", re.I)
BEGINNER_AUDIENCE = re.compile(r"\b(?:freshman|ninth grader|beginner|parent)\b", re.I)


def parse_prompt(prompt):
    """Return which of the five prompt elements the stub can see in this prompt.

    This is how the stub decides what to say. It is also worth reading on its
    own, because the list below is what a prompt is made of.
    """
    role = ROLE_PATTERN.search(prompt)
    audience = AUDIENCE_PATTERN.search(prompt)
    word_cap = WORD_CAP_PATTERN.search(prompt)
    step_count = STEP_COUNT_PATTERN.search(prompt)
    keys = KEYS_PATTERN.search(prompt)

    if JSON_PATTERN.search(prompt):
        fmt = "json"
    elif TABLE_PATTERN.search(prompt):
        fmt = "table"
    elif BULLET_PATTERN.search(prompt):
        fmt = "bullets"
    elif NUMBERED_PATTERN.search(prompt) or step_count:
        fmt = "numbered"
    else:
        fmt = "prose"

    return {
        "role": role.group(1).strip().rstrip(".") if role else None,
        "audience": audience.group(1).strip() if audience else None,
        "format": fmt,
        "json_only": bool(JSON_ONLY_PATTERN.search(prompt)),
        "json_keys": [k.strip() for k in keys.group(1).split(",")] if keys else [],
        "word_cap": int(word_cap.group(1)) if word_cap else None,
        "step_count": int(step_count.group(1)) if step_count else None,
        "has_example": bool(EXAMPLE_PATTERN.search(prompt)),
        "no_intro": bool(NO_INTRO_PATTERN.search(prompt)),
        "wants_sources": bool(CITE_PATTERN.search(prompt)),
        "grounded": bool(GROUNDING_PATTERN.search(prompt)),
        "provided_sources": [s.strip() for s in SOURCE_LINE_PATTERN.findall(prompt)],
        "allows_refusal": bool(REFUSE_PATTERN.search(prompt)),
        "topic": pick_topic(prompt),
        "prompt_words": len(prompt.split()),
    }


# ---------------------------------------------------------------------------
# Content packs
#
# Each pack is a list of short factual-sounding sentences about an invented
# school situation. The stub picks a pack from words in the prompt. Packs
# exist so that changing the format instruction changes the SHAPE of the reply
# without changing the subject, which is what makes an ablation readable.
# ---------------------------------------------------------------------------

TOPIC_PACKS = {
    "checkout": {
        "match": re.compile(r"\b(checkout|equipment|camera|tripod|locker|sign out|borrow)\b", re.I),
        "subject": "the Friday equipment checkout",
        "points": [
            "Open the checkout sheet before anyone lines up",
            "Match the serial number on the case to the number on the sheet",
            "Write the borrower's grade level, not their schedule",
            "Photograph any damage before the item leaves the room",
            "Set the return slot to the next school day, first period",
            "Put anything with a missing part on the repair shelf instead",
        ],
    },
    "study": {
        "match": re.compile(r"\b(study|studying|revise|revision|exam|quiz|test prep|homework)\b", re.I),
        "subject": "a study plan for a unit exam",
        "points": [
            "Write down what the exam actually covers before planning anything",
            "Split the material into blocks you can finish in twenty minutes",
            "Do the hardest block first, while you still have attention left",
            "Test yourself from a blank page instead of rereading notes",
            "Leave the last day for the two topics you keep getting wrong",
            "Sleep is part of the plan and not the thing you cut",
        ],
    },
    "research": {
        "match": re.compile(r"\b(research|history|evidence|study found|survey|report on|brief on)\b", re.I),
        "subject": "a short research brief",
        "points": [
            "The question has been studied in more than one field",
            "Findings disagree once you look at how each study measured the outcome",
            "Sample sizes in the smaller studies are too small to settle anything",
            "The most cited work in this area is older than most of its readers",
            "Later work narrowed the claim rather than overturning it",
        ],
    },
    "default": {
        "match": None,
        "subject": "the task you described",
        "points": [
            "Start by writing down what finished looks like",
            "Name the one thing that would make this fail",
            "Decide who reads the result before you decide its shape",
            "Check the part you are least sure about first",
            "Write down what you decided and why",
        ],
    },
}


def pick_topic(prompt):
    for name, pack in TOPIC_PACKS.items():
        if pack["match"] and pack["match"].search(prompt):
            return name
    return "default"


# Invented sources. Every one of these is fabricated from a template.
# They exist so a class can study a fabricated citation without going looking
# for one in the wild.
FAKE_AUTHORS = ["Ramirez, D.", "Okafor, T.", "Lindqvist, M.", "Barrow, J.", "Petrov, A."]
FAKE_VENUES = [
    "Quarterly Notes on School Technology",
    "Midland Review of Applied Learning",
    "Proceedings of the Workshop on Classroom Systems",
    "Bulletin of Secondary Instruction Research",
]
FAKE_TITLES = [
    "Measuring Attention in Scheduled Work Blocks",
    "A Field Study of Checkout Procedures in Secondary Schools",
    "Retrieval Practice and Short Revision Windows",
    "Structured Output and Downstream Parsing Failures",
]


def invented_sources(count, seed_text):
    """Build fabricated citations that look like real ones. None of them exist.

    The seed keeps the output deterministic, so a key can state exactly what a
    given prompt produces.
    """
    seed = sum(ord(c) for c in seed_text) % 97
    out = []
    for i in range(count):
        author = FAKE_AUTHORS[(seed + i * 3) % len(FAKE_AUTHORS)]
        venue = FAKE_VENUES[(seed + i * 5) % len(FAKE_VENUES)]
        title = FAKE_TITLES[(seed + i * 7) % len(FAKE_TITLES)]
        year = 2011 + ((seed + i * 11) % 13)
        volume = 4 + ((seed + i) % 21)
        first_page = 17 + ((seed + i * 13) % 180)
        out.append(f"{author} ({year}). {title}. {venue}, {volume}, "
                   f"{first_page}-{first_page + 14}.")
    return out


HEDGES = [
    "It is worth noting that outcomes vary by situation.",
    "Many educators agree that consistency matters more than any single rule.",
    "Ultimately, the right approach depends on your specific needs and goals.",
    "Studies have shown that small changes can produce meaningful improvements.",
]


CONTEXT_WORD = re.compile(r"[a-z]{4,}")
VAGUE_PROMPT_WORDS = 25


def select_points(points, prompt, parsed):
    """Choose and order the content. More context in, more on-target content out.

    A real model does not run this function. It does behave this way: a prompt
    that names the room, the gear, and what finished looks like pulls back
    sentences about the room, the gear, and finishing. A six-word prompt pulls
    back whatever is most common.
    """
    lowered = prompt.lower()
    scored = []
    for position, point in enumerate(points):
        overlap = sum(1 for word in CONTEXT_WORD.findall(point.lower()) if word in lowered)
        scored.append((-overlap, position, point, overlap))
    scored.sort()
    on_target = [s for s in scored if s[3] > 0]

    # Enough context to steer with: keep what it steered towards.
    if parsed["prompt_words"] >= VAGUE_PROMPT_WORDS and len(on_target) >= 2:
        chosen = [s[2] for s in on_target]
    else:
        chosen = [s[2] for s in scored]

    if parsed["step_count"]:
        wanted = parsed["step_count"]
        # Asked for more steps than there is on-target material, widen the net
        # before repeating. A model asked for five steps produces five
        # different steps, and some of them drift off the topic. It does not
        # print the same sentence twice.
        for candidate in (s[2] for s in scored):
            if len(chosen) >= wanted:
                break
            if candidate not in chosen:
                chosen.append(candidate)
        while len(chosen) < wanted:
            chosen = chosen + chosen
        chosen = chosen[:wanted]
    return chosen


def hedge_count(parsed):
    """How much padding. A constrained prompt gets none. A vague one gets all of it."""
    if parsed["word_cap"] or parsed["step_count"]:
        return 0
    if parsed["role"] or parsed["prompt_words"] >= VAGUE_PROMPT_WORDS:
        return 2
    return 4


def compose_reply(prompt):
    """Turn a prompt into a reply. Deterministic, template-built, no model."""
    parsed = parse_prompt(prompt)
    pack = TOPIC_PACKS[parsed["topic"]]
    points = select_points(list(pack["points"]), prompt, parsed)

    # A role line makes the reply commit to a viewpoint instead of hedging.
    if parsed["role"]:
        opener = f"As {article(parsed['role'])} {parsed['role']}, here is how I would handle {pack['subject']}."
    else:
        opener = f"Here are some thoughts on {pack['subject']}."

    # An audience instruction changes the vocabulary.
    if parsed["audience"]:
        opener += f" This is written for {article(parsed['audience'])} {parsed['audience']}."

    body = format_body(points, parsed, pack)

    # Asked for JSON and nothing else, the stub sends JSON and nothing else.
    # Asked only for JSON, it wraps the JSON in a sentence, the way a model
    # does, and your parser gets to fail on the sentence.
    if parsed["format"] == "json" and parsed["json_only"]:
        return body, parsed

    parts = [] if parsed["no_intro"] else [opener]
    parts.append(body)

    # A beginner audience gets a safety line a professional audience does not.
    if (parsed["audience"] and not parsed["no_intro"]
            and BEGINNER_AUDIENCE.search(parsed["audience"])):
        parts.append("If any of this does not match what you see, stop and ask "
                     "before you guess.")

    # No constraints means padding. That is the single most visible difference
    # between a constrained prompt and an unconstrained one.
    hedges = hedge_count(parsed)
    if hedges:
        parts.append(" ".join(HEDGES[:hedges]))

    text = "\n\n".join(p for p in parts if p)

    if parsed["word_cap"]:
        text = trim_to_words(text, parsed["word_cap"])

    # Sources go on after the cap. A model asked for 60 words and citations
    # gives you both, and it does not spend the 60 words on the citations.
    if parsed["wants_sources"]:
        text += "\n\n" + source_block(parsed, prompt)
    return text, parsed


def article(word):
    return "an" if word[:1].lower() in "aeiou" else "a"


def format_body(points, parsed, pack):
    fmt = parsed["format"]
    if fmt == "json":
        keys = parsed["json_keys"] or ["subject", "steps", "confidence"]
        payload = {}
        for key in keys:
            if key in ("steps", "items", "actions", "bullets"):
                payload[key] = points
            elif key in ("subject", "topic", "title"):
                payload[key] = pack["subject"]
            elif key in ("confidence", "certainty"):
                payload[key] = "high"
            elif key in ("summary", "answer", "text"):
                payload[key] = points[0] + "."
            else:
                payload[key] = points[0]
        return json.dumps(payload, indent=2)
    if fmt == "numbered":
        return "\n".join(f"{i}. {p}." for i, p in enumerate(points, 1))
    if fmt == "bullets":
        return "\n".join(f"- {p}." for p in points)
    if fmt == "table":
        rows = "\n".join(f"| {i} | {p}. |" for i, p in enumerate(points, 1))
        return "| # | Step |\n|---|---|\n" + rows
    return " ".join(f"{p}." for p in points)


def source_block(parsed, prompt):
    """Sources, and the one branch in this file that matters most.

    Asked for sources with no sources supplied, the stub invents them. That is
    the behaviour the Hallucination Hunt studies, reproduced on purpose.
    """
    if parsed["provided_sources"]:
        lines = [f"[{i}] {s}" for i, s in enumerate(parsed["provided_sources"], 1)]
        return "Sources:\n" + "\n".join(lines)
    if parsed["grounded"] and parsed["allows_refusal"]:
        return "Sources: none of the supplied sources address this. I do not know."
    return "Sources:\n" + "\n".join(f"[{i}] {s}" for i, s
                                    in enumerate(invented_sources(3, prompt), 1))


def trim_to_words(text, cap):
    """Cut the reply down to the cap without collapsing its line structure.

    A numbered list that has been through a naive word trim stops being a
    numbered list, and then the shape you asked for is gone for a reason that
    has nothing to do with the model.
    """
    if len(text.split()) <= cap:
        return text
    kept_lines = []
    budget = cap
    for line in text.splitlines():
        words = line.split()
        if not words:
            if kept_lines:
                kept_lines.append("")
            continue
        if len(words) <= budget:
            kept_lines.append(line)
            budget -= len(words)
            continue
        if budget > 0:
            partial = " ".join(words[:budget])
            if not partial.endswith((".", "?", "}", "|")):
                partial += "."
            kept_lines.append(partial)
        break
    while kept_lines and not kept_lines[-1]:
        kept_lines.pop()
    return "\n".join(kept_lines)


# ---------------------------------------------------------------------------
# The server
# ---------------------------------------------------------------------------

class StubModelServer(ThreadingHTTPServer):
    """An HTTP server that remembers its mode and counts generate calls."""

    daemon_threads = True
    block_on_close = False

    def __init__(self, address, mode=SUCCESS, delay_seconds=DEFAULT_DELAY_SECONDS, quiet=False):
        if mode not in MODES:
            raise ValueError(f"unknown mode '{mode}'")
        super().__init__(address, StubHandler)
        self.mode = mode
        self.delay_seconds = delay_seconds
        self.quiet = quiet
        self.generate_calls = 0
        self.requests = []
        self.lock = threading.Lock()

    @property
    def base_url(self):
        host, port = self.server_address[0], self.server_address[1]
        return f"http://{host}:{port}"

    def handle_error(self, request, client_address):
        if not self.quiet:
            super().handle_error(request, client_address)

    def record(self, request):
        with self.lock:
            self.generate_calls += 1
            self.requests.append(request)


class StubHandler(BaseHTTPRequestHandler):

    protocol_version = "HTTP/1.1"

    def do_GET(self):
        route = urlparse(self.path)
        if route.path == STATS_PATH:
            self.send_json(200, {"generate_calls": self.server.generate_calls,
                                 "mode": self.server.mode})
        elif route.path == PARSE_PATH:
            prompt = parse_qs(route.query).get("prompt", [""])[0]
            self.send_json(200, parse_prompt(prompt))
        elif route.path == TAGS_PATH:
            self.send_json(200, {"models": [{"name": STUB_MODEL_NAME, "size": 0}]})
        elif route.path == "/":
            self.send_text(200, "Stub model server is running")
        else:
            self.send_json(404, {"error": "not found"})

    def do_POST(self):
        request = self.read_json_body()
        if request is None:
            self.send_json(400, {"error": "the request body must be a JSON object"})
            return
        if self.path == MODE_PATH:
            self.change_mode(request)
        elif self.path == GENERATE_PATH:
            self.generate(request)
        else:
            self.send_json(404, {"error": "not found"})

    def change_mode(self, request):
        mode = request.get("mode")
        if mode not in MODES:
            self.send_json(400, {"error": f"mode must be one of {MODES}"})
            return
        self.server.mode = mode
        self.send_json(200, {"mode": mode})

    def generate(self, request):
        prompt = request.get("prompt")
        model = request.get("model")
        if not isinstance(prompt, str) or not isinstance(model, str):
            self.send_json(400, {"error": "model and prompt must both be strings"})
            return
        if request.get("stream") is not False:
            self.send_json(400, {"error": "this stub only supports stream: false"})
            return

        self.server.record(request)
        mode = self.server.mode
        if mode == SLOW:
            time.sleep(self.server.delay_seconds)

        text, _ = compose_reply(prompt)
        reply = {
            "model": model,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "response": text,
            "done": True,
            "prompt_eval_count": len(prompt.split()),
            "eval_count": len(text.split()),
        }

        if mode == ERROR:
            self.send_json(500, {"error": "the stub failed on purpose"})
        elif mode == MALFORMED:
            self.send_raw(200, b'{"model": "stub", "response": "The checkout sheet is',
                          "application/json")
        elif mode == RATE_LIMITED:
            self.send_json(429, {"error": "too many requests"},
                           extra_headers={"Retry-After": str(RETRY_AFTER_SECONDS)})
        elif mode == NOT_DONE:
            reply["done"] = False
            self.send_json(200, reply)
        elif mode == MISSING_RESPONSE:
            del reply["response"]
            self.send_json(200, reply)
        elif mode == EMPTY_RESPONSE:
            reply["response"] = "   "
            self.send_json(200, reply)
        else:
            self.send_json(200, reply)

    def read_json_body(self):
        """Return the request body as a dictionary, or None if it is not a JSON object."""
        try:
            length = int(self.headers.get("Content-Length", "0"))
            data = json.loads(self.rfile.read(length).decode("utf-8"))
        except ValueError:
            return None
        if not isinstance(data, dict):
            return None
        return data

    def send_json(self, status, data, extra_headers=None):
        self.send_raw(status, json.dumps(data).encode("utf-8"),
                      "application/json", extra_headers)

    def send_text(self, status, text):
        self.send_raw(status, text.encode("utf-8"), "text/plain; charset=utf-8")

    def send_raw(self, status, body, content_type, extra_headers=None):
        # In slow mode the client has usually given up and closed the
        # connection by the time this runs. That is expected, not an error.
        try:
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(body)))
            for name, value in (extra_headers or {}).items():
                self.send_header(name, value)
            self.end_headers()
            self.wfile.write(body)
        except ConnectionError:
            pass

    def log_message(self, format, *args):
        if not self.server.quiet:
            super().log_message(format, *args)


def start_in_background(mode=SUCCESS, delay_seconds=DEFAULT_DELAY_SECONDS,
                        host=DEFAULT_HOST, port=0):
    """Start a quiet stub on its own thread and return the server. Port 0 picks a free port.

    Call server.shutdown() and then server.server_close() to stop it.
    """
    server = StubModelServer((host, port), mode=mode, delay_seconds=delay_seconds, quiet=True)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    return server


def main():
    parser = argparse.ArgumentParser(
        description="A stand-in for a locally hosted, Ollama-compatible model server.")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--mode", choices=MODES, default=SUCCESS)
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY_SECONDS,
                        help="seconds to wait before replying in slow mode")
    arguments = parser.parse_args()

    server = StubModelServer((arguments.host, arguments.port), mode=arguments.mode,
                             delay_seconds=arguments.delay)
    print(f"Stub model server on {server.base_url} in {server.mode} mode. Press Ctrl+C to stop.")
    print("Every source this server produces is invented. None of them are real.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
