# Database Types and Structures, Compared Honestly
---
## Slide 1: The list nobody explains
- Relational, NoSQL, graph, data warehouse
- Distributed, open source, cloud, AI database
- Flat file, hierarchical, data lake, multi-modal
- These are four different kinds of category
Speaker notes: This is the list the exam asks you about and it feels slippery for a reason nobody tells you. Those words are not competing answers to one question. They answer four different questions, and once you see which is which the whole topic stops being a pile you have to memorise.
Image: The full list of words scattered, with four faint coloured groupings behind them.
---
## Slide 2: Four questions, not one
- How is the data shaped
- What is the system for
- How is it deployed
- How is it licensed
Speaker notes: Shape is relational, document, graph, vector. Purpose is warehouse or lake. Deployment is distributed or cloud. Licence is open source. A hosted PostgreSQL is all four at once: relational, distributed, cloud, and open source. Those are not four answers to pick between.
Image: A four column table with the example words sorted into the right column.
---
## Slide 3: The question picks the structure
- How many, by group, over a period, relational
- Give me this whole thing by id, document
- Who is three steps away, graph
- Which text means roughly this, vector
Speaker notes: One rule for the whole topic. Look at the shape of the question you are going to ask and pick the structure that answers that shape cheaply. Not the newest one, not the one in the job advert. And say the size out loud, because a recommendation with no size in it is not a recommendation.
Image: Four question bubbles, each with an arrow to one structure.
---
## Slide 4: Document store is good at this
```python
item = by_id["EQ-0110"]
print(item["name"], "|", ", ".join(item["tags"]))
```
```
Resin 3D printer | printing, resin, training-required, ventilation-required
```
Speaker notes: One lookup, everything about that item, no joins at all. That is the document model's whole argument and it is a good one. The catalog arrives in exactly this shape, so somebody could reasonably say we already have a document database and it is called a JSON file.
Image: None. This slide is code.
---
## Slide 5: And this is where it costs you
```python
counts = {}
for item in items:
    for tag in item["tags"]:
        counts[tag] = counts.get(tag, 0) + 1
```
```
[('training-required', 7), ('battery', 4), ('printing', 3)]
```
Speaker notes: Same answer as the SQL version, one line longer, and notice what you did. You wrote the loop. The document store has no index across documents unless you build one. Same answer, different person writing the loop, and that is most of the trade in one sentence.
Image: None. This slide is code.
---
## Slide 6: Graph, and what a step costs
- One step is one join, eight members come back
- Two steps is a self join on a self join
- Three steps is a query nobody can debug
- At fourteen members, do not
Speaker notes: Who has borrowed the same equipment as Amara is one join and it returns eight of the other thirteen members. Two steps is that join nested inside itself. A graph database stores the relationship as a thing, so three steps is one short expression. It is also a whole second system to install, learn, and back up.
Image: A small network of members and items with a path traced two steps out.
---
## Slide 7: A vector database is a table and a loop
- Store vectors, score similarity, sort, return the top
- That is the entire mechanism
- A real one adds an approximate neighbour index
- That matters at a million rows, not fifty six
Speaker notes: This is the part people think is magic. It is not. You will write the whole thing in Week 12 in about eight lines over SQLite. What a real vector database adds is an index so it does not compare every row, and that starts to matter in the millions. It does not add meaning.
Image: A table of number lists with an arrow to a sorted result list.
---
## Slide 8: AI database is not a data model
- It usually means one of three different things
- A vector store, or a relational database with vectors
- Or a feature store holding a model's training inputs
- Ask which one. That question is the competency
Speaker notes: When somebody says AI database, they mean one of those three, and they often have not decided which. Asking is not being difficult, it is the skill. You will meet this in a Gate 2 in this module, in a document that gets several other things right.
Image: One label, three different boxes underneath it, with a question mark between.
---
## Slide 9: The sentence to distrust
- We should use NoSQL, it scales better and is more flexible
- NoSQL is at least four unrelated models
- Scales better than what, at what size
- Flexible describes a cost as if it were a benefit
Speaker notes: You will hear this sentence, from somebody who sounds like they know. Three problems. NoSQL names four different things. Better has no comparison and no number. And a store that accepts any shape accepts your typo too, which is exactly what Tuesday was about. Sometimes that is the right trade, and you say so out loud when you make it.
Image: The sentence in quotation marks with three annotations pointing at the three problems.
---
## Slide 10: What you are about to build
- Your project memo recommends one per workload
- Every recommendation names a cost
- One contested call, argued against yourself
- Build two starts the comparison memo today
Speaker notes: Build two is the start of the database comparison memo, which is due Friday of Week 11 and is the largest single piece of written work in this module. Four workloads, four recommendations, and every one of them names something it makes harder. A recommendation with no cost in it is a sales pitch and it scores like one.
Image: A memo page with four headings and a cost line under each.
---
