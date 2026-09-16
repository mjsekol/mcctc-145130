"""ask.py . ask the handbook a question and see where the answer came from.

Lab M04-05 solution. The same code is the retrieval half of the
Module 4 performance task, so it is deliberately the reference too.

    python ask.py "how long can I keep a camera kit" --model-url http://127.0.0.1:11634
    python ask.py "how many items at once" --k 5 --model-url http://127.0.0.1:11634

WHAT THIS PROGRAM DOES AND DOES NOT DO

It retrieves. It does not answer. Every line it prints is text somebody wrote in
the handbook, with the file and heading it came from, so you can open that file
and read the sentence in context.

That is deliberate, and it is the part of retrieval worth defending. A system
that hands you a generated paragraph has to be trusted. A system that hands you
the paragraph plus its source can be checked in ten seconds by somebody who
knows the handbook better than you do.

ON THE STUB, THE RANKING IS MEANINGLESS

The shared stack's stub builds its vector from a hash of the text. The same text
always gives the same vector, and text that means the same thing gives a
completely different one. So on the stub, this program proves your plumbing
works and tells you nothing about whether the right chunk came back. Say that
out loud when you demonstrate it. A retrieval demo that hides it is the kind of
confident wrong thing this course exists to catch.
"""

import argparse
import os
import sys

from embed import DEFAULT_MODEL, DEFAULT_MODEL_URL, EmbeddingError, embed
from vectorstore import DimensionMismatch, VectorStore

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_INDEX = os.path.join(HERE, "output", "handbook.index")


def preview(text, width=300):
    """The chunk, flattened to one paragraph and shortened for the terminal."""
    flat = " ".join(text.split())
    return flat if len(flat) <= width else flat[:width - 3] + "..."


def ask(question, index_path=DEFAULT_INDEX, k=4, base_url=DEFAULT_MODEL_URL,
        model=DEFAULT_MODEL, embed_function=embed):
    store = VectorStore(index_path)
    if store.count() == 0:
        store.close()
        raise FileNotFoundError(index_path)
    query_vector = embed_function(question, model=model, base_url=base_url)
    hits = store.search(query_vector, k=k)
    store.close()
    return hits


def main(argv=None):
    parser = argparse.ArgumentParser(description="Query the handbook index.")
    parser.add_argument("question")
    parser.add_argument("--index", default=DEFAULT_INDEX)
    parser.add_argument("--k", type=int, default=4)
    parser.add_argument("--model-url", dest="model_url", default=DEFAULT_MODEL_URL)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    arguments = parser.parse_args(argv)

    if not os.path.exists(arguments.index):
        print(f"No index at {arguments.index}. Run: python index_docs.py")
        return 1
    try:
        hits = ask(arguments.question, arguments.index, arguments.k,
                   arguments.model_url, arguments.model)
    except EmbeddingError as error:
        print(f"The embeddings endpoint did not answer: {error}")
        print("Start the stub in another terminal:")
        print("  python Courses\\145130\\anchor-project\\ai-stack\\stub_model_server.py --port 11634")
        return 1
    except DimensionMismatch as error:
        print(f"The question and the index do not match.\n  {error}")
        return 1

    print(f'Question: "{arguments.question}"')
    print(f"Retrieved {len(hits)} chunks. Nothing below was generated. Every line is"
          " from a handbook file.")
    print()
    for position, hit in enumerate(hits, start=1):
        print(f"{position}. score {hit['score']:+.4f}   {hit['doc_id']} . {hit['heading']}"
              f"   characters {hit['char_start']}-{hit['char_end']}")
        print(f"   {preview(hit['text'])}")
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
