# Database Types and Structures, Compared Honestly
## 145130 Applications of AI · Module 4 · Week 10, Wednesday

**Slides for this lesson:** [outline](../04-slides/MCCTC_145130_Slides_W10_TypesAndStructures.md) ·
[deck](../04-slides/exports/MCCTC_145130_Slides_W10_TypesAndStructures.pptx)

**Every example was executed on the build machine, Python 3.13.7, SQLite 3.50.4.**

---

## Why this is a hard lesson to teach honestly

The exam asks you to identify types of databases and compare structures. The list you will be
asked about is:

> relational, object-oriented, NoSQL, graph, data warehouse, distributed, open source, cloud,
> artificial intelligence

and

> flat file, hierarchical, relational, data lakes, object-oriented, cloud, multi-modal

**Those two lists mix four different kinds of category**, and nobody tells you that, which is
why the topic feels slippery.

| Kind of category | Members of the list |
|---|---|
| **How the data is shaped** | flat file, hierarchical, relational, object-oriented, document, graph, vector, multi-modal |
| **What the system is for** | data warehouse, data lake |
| **How it is deployed** | distributed, cloud |
| **How it is licensed** | open source |

**A cloud relational database is all four at once.** PostgreSQL on a hosted service is
relational, distributed if you replicate it, cloud, and open source. Those are not competing
answers. Learn the list, and learn which question each word answers, because that is what
stops the topic feeling like memorising a pile.

---

## The one question that picks a structure

**What shape is the question you are going to ask?**

| The question looks like | The structure that fits | Why |
|---|---|---|
| "How many, by group, over a period" | relational | counting and grouping over rows with the same fields |
| "Give me this whole thing by its id" | key-value or document | one lookup, no joining, the whole object at once |
| "Who is three steps from this person" | graph | relationships are stored as things rather than found by joining |
| "Which text means roughly this" | vector | similarity in meaning rather than matching characters |
| "Everything we have ever collected, we will decide later" | data lake | keep the raw thing and work out the schema when somebody asks |
| "Last five years of sales, sliced every way" | data warehouse | read-heavy, historical, built for aggregation |

---

## Worked example 1: relational against document, same data

The makerspace catalog arrives as JSON: a document per item, with a nested array and a nested
object. That is exactly what a **document database** stores.

```python
import json

with open("catalog.json", encoding="utf-8") as handle:
    items = json.load(handle)["items"]
by_id = {item["item_id"]: item for item in items}

# The question a document store is good at: give me this whole thing.
item = by_id["EQ-0110"]
print(item["name"], "|", ", ".join(item["tags"]), "|", item["purchase"]["funded_by"])
```

Real output:

```
Resin 3D printer | printing, resin, training-required, ventilation-required | Booster club
```

**One lookup, everything about the item, no joins.** That is the document model's whole
argument, and it is a good one.

Now the other kind of question:

```python
counts = {}
for item in items:
    for tag in item["tags"]:
        counts[tag] = counts.get(tag, 0) + 1
print(sorted(counts.items(), key=lambda pair: -pair[1])[:3])
```

```
[('training-required', 7), ('battery', 4), ('printing', 3)]
```

That works, and notice what you did: **you wrote the loop.** The document store has no index
across documents unless you build one. In SQL the same question is one statement and the
database decides how:

```sql
SELECT t.tag, COUNT(*) FROM tags t
JOIN item_tags it ON it.tag_id = t.tag_id
GROUP BY t.tag ORDER BY COUNT(*) DESC LIMIT 3;
```

```
training-required  7
battery            4
printing           3
```

**Same answer. The difference is who wrote the loop.**

---

## Worked example 2: a graph question, and what it costs relationally

"Which members have borrowed the same equipment as Amara Delgado?" One join:

```sql
SELECT DISTINCT b.member_id
FROM loans a JOIN loans b ON b.item_id = a.item_id AND b.member_id <> a.member_id
WHERE a.member_id = 'RC-0142';
```

Real output from the reference database:

```
RC-0143  RC-0158  RC-0160  RC-0171  RC-0174  RC-0180  RC-0188  RC-0190
```

Eight of the other thirteen members, in one join. Now **two** steps: who has borrowed the same equipment as those people? That is the same join
again, nested. Three steps is three. Four steps is a query nobody wants to read and nobody
can debug.

**A graph database stores the relationship itself**, so "everybody within three steps" is one
short expression. That is the trade: a second system to run, learn, and back up, in exchange
for questions that get worse with every step in a relational model.

**At fourteen members, do not.** The join is fine, the data already holds every connection,
and the migration later is an export rather than a rebuild. **Say the size out loud when you
recommend a database.** A recommendation with no size in it is not a recommendation.

---

## Worked example 3: a vector database is a table and a loop

This is the part people think is magic. It is not.

```python
import math

def cosine(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    length_a = math.sqrt(sum(x * x for x in a))
    length_b = math.sqrt(sum(y * y for y in b))
    return dot / (length_a * length_b)

store = {
    "loan policy":    [0.90, 0.10, 0.20],
    "resin printer":  [0.10, 0.95, 0.05],
    "laptop carts":   [0.30, 0.10, 0.90],
}
question = [0.88, 0.08, 0.25]
for name, vector in sorted(store.items(), key=lambda pair: -cosine(question, pair[1])):
    print(f"{name:<15} {cosine(question, vector):+.4f}")
```

Real output:

```
loan policy     +0.9981
laptop carts    +0.5673
resin printer   +0.2009
```

**That is a vector database.** A store of vectors and a way to find the nearest ones.

What a real vector database adds is an **index** that finds approximate neighbours without
comparing every row, which starts to matter somewhere around a million vectors and does not
matter at fifty six. You will write this yourself in Week 12, in about eight lines, over
SQLite.

**"AI database" is not a data model.** It is a marketing word that usually means one of three
things: a vector store, a relational database with a vector column added, or a feature store
that keeps the inputs a model was trained on. When somebody says it, ask which one. That
question is the competency.

---

## The rest of the list, said plainly

**Flat file.** One table, no relationships, no rules. A CSV. Fine for a shopping list and for
handing data to another program. It is where your fixture comes from, and Monday showed what
it costs.

**Hierarchical.** A tree. Each record has one parent. This is what the Windows registry and a
file system are, and what XML and JSON documents are. Great for "everything under this
node", bad for anything that has two parents.

**Object-oriented.** Stores objects with their methods and inheritance, so your program's
classes and the database's records are the same thing. Rare now. What almost everybody
actually does is keep a relational database and use an object-relational mapper to translate.

**Data warehouse.** A relational database arranged for reading history rather than recording
today: denormalized on purpose, optimised for aggregation across years. **Denormalized on
purpose** is the phrase to keep. Tuesday's rule about writing each fact once is a rule for
systems that record events. A warehouse is built to answer questions.

**Data lake.** Keep the raw files, in whatever format they arrived, and decide the schema when
somebody asks a question. The honest version: it saves you from throwing away the thing you
did not know you needed, and it becomes useless the moment nobody can say what is in it.

**Multi-modal.** One system holding text, images, audio, and structured rows together, usually
so they can be searched by meaning across types. This is the newest word on the list and the
one most likely to mean different things to different vendors.

**Distributed.** The data lives on more than one machine. Buys you capacity and survival.
Costs you the guarantee that two readers see the same thing at the same moment, which is a
much bigger cost than it sounds.

**Cloud.** Somebody else runs the machine. A deployment choice, not a data model.

**Open source.** A licence. SQLite, PostgreSQL, and MySQL are open source and completely
different from each other, which is the point: the licence tells you about your rights, not
about your data.

---

## The wrong version, and what it produces

The wrong version of this lesson is not code. It is a sentence, and you will hear it:

> "We should use a NoSQL database because it scales better and it is more flexible."

Three problems.

1. **"NoSQL" is not one thing.** A document store, a key-value store, a column-family store,
   and a graph database are all called NoSQL and they are as different from each other as
   they are from a relational database.
2. **"Scales better" with no number.** Better than what, at what size, on what question?
   Fourteen members is not a scaling problem.
3. **"More flexible" describes a cost as if it were a benefit.** A store that accepts any
   shape accepts your typo too. Tuesday's whole lesson was that rules the database enforces
   are the ones that survive. Flexibility is what you give up to get them, and sometimes that
   is the right trade, and you should say so out loud when you make it.

**Why it is tempting.** Every one of those three phrases is something you have heard from
somebody who sounded like they knew. **You are going to meet this exact sentence in a Gate 2
this module**, written confidently, in a document that gets several other things right.

---

## Vocabulary

| Term | What it means |
|---|---|
| **relational** | data in tables with keys and enforced relationships |
| **document** | one self-contained record per thing, usually JSON, nesting allowed |
| **key-value** | a dictionary that survives a restart |
| **graph** | relationships stored as first-class things you traverse |
| **vector** | a store of embeddings, queried by similarity |
| **data warehouse** | a read-heavy, historical, deliberately denormalized relational store |
| **data lake** | raw files kept as they arrived, schema decided at read time |
| **multi-modal** | one store holding several kinds of content, searchable together |
| **NoSQL** | an umbrella word covering at least four unrelated models |
| **index** | a structure that finds rows without reading all of them |

---

## Self-check

**1.** The makerspace wants "every loan and every item, counted by category, every month".
Name the structure and one thing your choice makes harder.

**2.** Somebody recommends a graph database for the makerspace's "who works with whom"
question. Give the strongest case for and the strongest case against, in one sentence each.

**3.** What is actually inside a vector database, and what does a real one add that your Week
12 version will not have?

### Answers

**1.** Relational. It is counting and grouping over records with identical fields, which is
what the model was built for. **What it makes harder:** changing the shape. Adding "which
staff member checked this in" is a schema change, a migration script, and a rerun, where a
document store would accept one more key on new records with nothing to run.

**2.** **For:** the relational version of "two steps away" is a self join on a self join, and
three steps is unreadable, so if that question is ever asked seriously the graph model is the
right home for it. **Against:** fourteen members and fourteen items, the question has not
actually been asked yet, and it is a second system to install, learn, back up, and keep in
step with the relational one.

**3.** A table of vectors, plus a way to score similarity, plus a way to sort. A real one adds
an approximate nearest neighbour index so it does not compare every row, which starts to
matter in the millions. **It does not add meaning.** The meaning comes from the model that
produced the vectors, which is why a retrieval system built on a stub that hashes its input
has working plumbing and worthless results.
