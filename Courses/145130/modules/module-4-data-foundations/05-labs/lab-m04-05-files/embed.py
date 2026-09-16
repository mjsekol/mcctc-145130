"""embed.py . the only file that talks to the embeddings endpoint.

Lab M04-05 solution. The same code is the retrieval half of the
Module 4 performance task, so it is deliberately the reference too.

    POST {base_url}/api/embeddings   {"model": "...", "prompt": "..."}
    ->                               {"model": "...", "embedding": [float, ...]}

That is the contract in the shared stack's `docs/io-spec.md` section 7. The stub
model server in `Courses/145130/anchor-project/ai-stack/stub_model_server.py`
answers it with no model installed.

THE RULE THIS FILE EXISTS TO ENFORCE

**Nothing here knows how long a vector is.** The stub returns 32 numbers. A real
model returns hundreds, and a different real model returns a different number of
hundreds. Code that hardcodes 32 works on the stub, passes its tests, and breaks
on the first lab machine with a model on it. The length is read from the answer
and carried with the data.

The second rule: an embedding is not text you can eyeball. A wrong one looks
exactly like a right one. So every reply is checked for shape before it is used,
and a failure gets a named kind, the way the shared stack does.

There is no API key here and there never will be. The endpoint is local.

THE PORT

Module 4 uses **11634**, not 11434. A real Ollama listens on 11434 and so does
every other course stub's default, and a run against the wrong server looks
exactly like a working run. Start the stub with `--port 11634` and pass
`--model-url http://127.0.0.1:11634` to every program, even though it is also
the default here. An explicit port is a thing you can check.
"""

import json
import math
import os
import urllib.error
import urllib.request

DEFAULT_MODEL_URL = os.environ.get("RIDGE_MODEL_URL", "http://127.0.0.1:11634")
DEFAULT_MODEL = os.environ.get("RIDGE_MODEL", "llama3.2")
DEFAULT_TIMEOUT = float(os.environ.get("RIDGE_MODEL_TIMEOUT", "20"))


class EmbeddingError(Exception):
    """A failure with a kind you can branch on, like the shared stack's errors."""

    def __init__(self, kind, message):
        super().__init__(f"{kind}: {message}")
        self.kind = kind
        self.message = message


def embed(text, model=DEFAULT_MODEL, base_url=DEFAULT_MODEL_URL, timeout=DEFAULT_TIMEOUT):
    """One piece of text in, one list of floats out. Raises EmbeddingError."""
    if not isinstance(text, str) or text.strip() == "":
        raise EmbeddingError("empty_input", "there is nothing to embed")
    body = json.dumps({"model": model, "prompt": text}).encode("utf-8")
    request = urllib.request.Request(
        base_url.rstrip("/") + "/api/embeddings",
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read().decode("utf-8")
    except urllib.error.HTTPError as error:
        raise EmbeddingError("model_http_error",
                             f"the model server answered with HTTP {error.code}") from error
    except urllib.error.URLError as error:
        reason = getattr(error, "reason", error)
        if isinstance(reason, TimeoutError):
            raise EmbeddingError("timeout", f"no answer within {timeout} seconds") from error
        if isinstance(reason, ConnectionRefusedError):
            raise EmbeddingError("connection_refused",
                                 f"nothing is listening at {base_url}") from error
        raise EmbeddingError("unreachable", f"{base_url} could not be reached: {reason}") from error
    except TimeoutError as error:
        raise EmbeddingError("timeout", f"no answer within {timeout} seconds") from error

    try:
        payload = json.loads(raw)
    except ValueError as error:
        raise EmbeddingError("malformed_json",
                             "the reply was not valid JSON") from error
    if not isinstance(payload, dict):
        raise EmbeddingError("malformed_json", "the reply was not a JSON object")
    vector = payload.get("embedding")
    if not isinstance(vector, list):
        raise EmbeddingError("missing_field", "the reply has no embedding list")
    if len(vector) == 0:
        raise EmbeddingError("empty_embedding", "the embedding list is empty")
    cleaned = []
    for value in vector:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise EmbeddingError("bad_value", f"the embedding holds {value!r}, not a number")
        if math.isnan(value) or math.isinf(value):
            raise EmbeddingError("bad_value", "the embedding holds a value that is not finite")
        cleaned.append(float(value))
    return cleaned


def embed_all(texts, on_error="raise", **options):
    """Embed a list of texts. Returns (vectors, failures).

    `on_error='collect'` keeps going and reports which items failed, because a
    document set of forty chunks should not be abandoned at chunk nine. Which
    behaviour you want is a decision, so it is an argument rather than a default
    somebody has to read the source to discover.
    """
    vectors = []
    failures = []
    for position, text in enumerate(texts):
        try:
            vectors.append(embed(text, **options))
        except EmbeddingError as error:
            if on_error == "raise":
                raise
            failures.append((position, error.kind, error.message))
            vectors.append(None)
    return vectors, failures


def probe(base_url=DEFAULT_MODEL_URL, model=DEFAULT_MODEL, timeout=DEFAULT_TIMEOUT):
    """Ask for one small embedding and report the length. Never assume it."""
    vector = embed("probe", model=model, base_url=base_url, timeout=timeout)
    return {"base_url": base_url, "model": model, "dimensions": len(vector)}
