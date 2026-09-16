# Embeddings, and a Vector Store You Can Read
---
## Slide 1: The stub says thirty two
- Write that number in your README
- Do not write it anywhere else
- A real model returns hundreds
- Code that learned 32 passes every test here
Speaker notes: One probe call and the answer is thirty two numbers. That is a fact about the stub, not about embeddings. A real model returns hundreds and a different real model returns a different number of hundreds. Code with thirty two in it passes everything on this machine and fails on the first lab machine with a model on it.
Image: A terminal showing dimensions 32, with a large red circle around the number and a slash through a source file.
---
## Slide 2: What an embedding actually is
- A list of numbers standing for a piece of text
- The direction encodes what it is about
- Similar text should point in similar directions
- The meaning comes from the model, not your store
Speaker notes: That is the whole idea. Two things follow that people skip. An embedding is not readable, so a wrong one looks exactly like a right one and there is no eyeballing it. And your store contributes no meaning at all. If the model is a hash function the numbers are stable and meaningless, and your store will rank them anyway.
Image: Two short sentences with arrows pointing in similar directions, and a third pointing away.
---
## Slide 3: The call
```
POST http://127.0.0.1:11634/api/embeddings
{"model": "llama3.2", "prompt": "how long can I keep a camera kit"}
-> {"model": "llama3.2", "embedding": [0.2657, 0.1585, ...]}
```
Speaker notes: One endpoint, one field that matters. Note the port. Module four uses eleven six three four, not eleven four three four, because a real Ollama and several other course stubs all sit on the default and a run against the wrong server looks exactly like a working run. Pass the port explicitly, every time.
Image: None. This slide is code.
---
## Slide 4: Cosine similarity, in eight lines
```python
dot = sum(x * y for x, y in zip(a, b))
length_a = math.sqrt(sum(x * x for x in a))
length_b = math.sqrt(sum(y * y for y in b))
return dot / (length_a * length_b)
```
Speaker notes: The cosine of the angle between two vectors. One is the same direction, zero is at right angles. And it ignores length, which is what you want, because a longer chunk should not score higher for being longer. That is the entire similarity machinery.
Image: None. This slide is code.
---
## Slide 5: The store is two tables and a foreign key
- chunks holds the text and where it came from
- vectors holds one vector per chunk
- ON DELETE CASCADE, because a vector is part of its chunk
- A vector database is a database
Speaker notes: Everything from Week 10 is in here. A primary key, a foreign key with a cascade, a unique constraint saying a document has one chunk per ordinal. There is nothing new about a vector store except what is in the column, and that is worth saying because people think otherwise.
Image: Two small tables joined, with the vector column drawn as a long list of numbers.
---
## Slide 6: Learn the length, refuse the rest
- The first vector sets the index length
- Store it in index_meta
- Refuse any vector that disagrees
- Put both numbers in the message
Speaker notes: The index learns its length from the first vector it is given and then refuses anything else, with both numbers in the message. An error that says dimension mismatch tells nobody which two things did not match. And this has to be an error rather than a score, which is the next slide.
Image: A gate with a number on it accepting one vector and refusing a longer one.
---
## Slide 7: Why it cannot be a score
- Cosine between different lengths is undefined
- Pad or truncate and you get a number
- That number sorts and prints normally
- A search that works and means nothing
Speaker notes: If you forced it, you would get a number. It would sort, it would format to four decimal places, and it would look exactly like a real score. The failure mode of not raising here is a search that works and is meaningless, which is the hardest kind of wrong to find in anything.
Image: Two vectors of different lengths with a padded tail, and a plausible looking score underneath.
---
## Slide 8: Search is a full scan and that is fine
```python
scored.sort(key=lambda hit: (-hit["score"], hit["doc_id"], hit["ordinal"]))
return scored[:k]
```
Speaker notes: Every row gets compared. At fifty six chunks that is the right answer and saying so is more useful than pretending an index is required. Look at the sort key: score, then something stable. Two chunks with the same score have to come back in the same order every run or nobody can check your work, including you.
Image: None. This slide is code.
---
## Slide 9: Four failures, four messages
```
connection_refused: nothing is listening at http://127.0.0.1:11634
Start the stub in another terminal:
  python ...\stub_model_server.py --port 11634
```
Speaker notes: Refused means start the server. Timeout means it is there and slow, so do not restart it. A bad status means it answered and refused, so check the model name. A reply that is not the shape we expect usually means the wrong port. Four problems, four fixes, four messages, and you learned that in Module 1.
Image: None. This slide is code.
---
## Slide 10: What you are about to build
- Part two of lab M04-05, two terminals
- Write cosine, add, and search
- The number 32 in no .py file you write
- Then ask it three questions and record all three
Speaker notes: Build one is part two of the retrieval lab. Stub in terminal one on port eleven six three four, your programs in terminal two. You write three functions. I will grep your submission for the number thirty two. Then you ask it three questions and write down what came back, including the one that goes badly.
Image: Two terminals side by side, one running the stub, one running the indexer.
---
