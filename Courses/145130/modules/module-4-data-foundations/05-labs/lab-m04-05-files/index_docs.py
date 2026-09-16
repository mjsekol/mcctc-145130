"""index_docs.py . chunk the handbook, embed every chunk, store the vectors.

Lab M04-05 starter. The same code is the retrieval half of the
Module 4 performance task, so it is deliberately the reference too.

Start the shared stack's stub first, in its own terminal:

    python Courses\\145130\\anchor-project\\ai-stack\\stub_model_server.py --port 11634

Then:

    python index_docs.py --model-url http://127.0.0.1:11634
    python index_docs.py --docs <folder> --index output\\handbook.index --k 4

The index is a separate SQLite file from the makerspace database on purpose.
They answer different questions, they are rebuilt at different times, and a
rebuild of one should never be able to damage the other.
"""

import argparse
import os
import sys
import time

from chunker import chunk_folder, DEFAULT_MAX_CHARACTERS, DEFAULT_OVERLAP
from embed import DEFAULT_MODEL, DEFAULT_MODEL_URL, EmbeddingError, embed
from vectorstore import VectorStore

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_DOCS = os.path.join(HERE, "..", "fixtures", "ridge-makerspace", "handbook")
DEFAULT_INDEX = os.path.join(HERE, "output", "handbook.index")


def build(docs_folder=DEFAULT_DOCS, index_path=DEFAULT_INDEX,
          base_url=DEFAULT_MODEL_URL, model=DEFAULT_MODEL,
          max_characters=DEFAULT_MAX_CHARACTERS, overlap=DEFAULT_OVERLAP,
          embed_function=embed, verbose=True):
    """Rebuild the index from scratch. Returns a counts dictionary.

    `embed_function` is an argument so the tests can pass a fake that returns a
    vector of a length the stub never produces. That is not test convenience for
    its own sake: it is the check that nothing in this program knows how long a
    vector is.
    """
    if os.path.exists(index_path):
        os.remove(index_path)
    chunks = chunk_folder(docs_folder, max_characters=max_characters, overlap=overlap)
    store = VectorStore(index_path)
    started = time.time()
    stored = 0
    failures = []
    for chunk in chunks:
        try:
            vector = embed_function(chunk["text"], model=model, base_url=base_url)
        except EmbeddingError as error:
            failures.append((chunk["doc_id"], chunk["ordinal"], error.kind, error.message))
            continue
        store.add(chunk, vector)
        stored += 1
    store.set_meta("model", model)
    store.set_meta("model_url", base_url)
    store.set_meta("source_folder", os.path.abspath(docs_folder))
    store.set_meta("max_characters", max_characters)
    store.set_meta("overlap", overlap)
    store.commit()
    counts = {
        "documents": len({chunk["doc_id"] for chunk in chunks}),
        "chunks": len(chunks),
        "stored": stored,
        "failed": len(failures),
        "dimensions": store.dimensions,
        "seconds": round(time.time() - started, 2),
    }
    if verbose:
        print("Ridge Creek handbook . index")
        print(f"  documents     {counts['documents']}")
        print(f"  chunks        {counts['chunks']}")
        print(f"  embedded      {counts['stored']}")
        print(f"  failed        {counts['failed']}")
        print(f"  dimensions    {counts['dimensions']}  (read from the answer, never assumed)")
        print(f"  seconds       {counts['seconds']}")
        print(f"  index         {index_path}")
        for doc_id, ordinal, kind, message in failures[:5]:
            print(f"  FAILED {doc_id} chunk {ordinal}: {kind}: {message}")
    store.close()
    return counts


def main(argv=None):
    parser = argparse.ArgumentParser(description="Build the handbook retrieval index.")
    parser.add_argument("--docs", default=DEFAULT_DOCS)
    parser.add_argument("--index", default=DEFAULT_INDEX)
    parser.add_argument("--model-url", dest="model_url", default=DEFAULT_MODEL_URL)
    parser.add_argument("--model", default=DEFAULT_MODEL)
    parser.add_argument("--max-characters", type=int, default=DEFAULT_MAX_CHARACTERS)
    parser.add_argument("--overlap", type=int, default=DEFAULT_OVERLAP)
    arguments = parser.parse_args(argv)
    try:
        build(arguments.docs, arguments.index, arguments.model_url, arguments.model,
              arguments.max_characters, arguments.overlap)
    except EmbeddingError as error:
        print(f"The embeddings endpoint did not answer: {error}")
        print("Start the stub in another terminal:")
        print("  python Courses\\145130\\anchor-project\\ai-stack\\stub_model_server.py --port 11634")
        return 1
    except FileNotFoundError as error:
        print(f"No document folder at {error.filename}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
