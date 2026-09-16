# The Questions You Ask Before Anything Touches Student Data
---
## Slide 1: You will be the person who is asked
- A teacher asks in a hallway on a Tuesday
- Everybody in the room wants the answer to be yes
- You are the only one who has read an agreement
- Not in five years. This year
Speaker notes: The skill is not knowing the answer. The skill is knowing the questions, and knowing when you have been handed something that is not an answer. That second half is most of today.
Image: A hallway, a teacher asking, a laptop open to a vendor page.
---
## Slide 2: The nine questions
- Where does it run, and does input leave the building
- Is input retained, by whom, for how long
- Is input used to train or improve anything
- What does the contract say when the page disagrees
Speaker notes: Nine, in order, and they are section eight of your assessment. The last one is the one people skip and it is the one that decides. A marketing page, a privacy policy, and a contract are three different documents, and only one of them is enforceable.
Image: A numbered list of nine, the ninth in accent blue.
---
## Slide 3: Where the answers actually live
- Marketing page: what they want you to believe
- Privacy policy: consumer promises, maybe not yours
- Contract or data processing agreement: what governs
- Your own test: what actually happens
Speaker notes: Trust runs from the bottom of that list upward. A test you ran beats a document somebody wrote about what the software does. And you can ask for the agreement. People do not, because asking feels presumptuous, and it is the normal thing to do.
Image: Four documents stacked, the bottom one weighted heaviest.
---
## Slide 4: Five carve-outs that survive a good answer
- "We do not sell your data": selling is narrow
- "Not used for training": look for the next sentence
- "You retain ownership": find the licence grant
- "Encrypted": in transit, at rest, keys held by whom
Speaker notes: Every one of those sentences is true and leaves a hole. And a fifth: we are FERPA compliant. FERPA obligations sit on the school. A vendor can help the school meet them or make it impossible, and a badge on a page is not a contractual commitment.
Image: Five sentences, each with a small gap cut out of it.
---
## Slide 5: The scan gets it wrong, and that is the lesson
```
study-buddy\study_buddy.py
   address: http://{MODEL_HOST}:{DEFAULT_PORT}/api/generate  (REMOTE)
   address: http://{MODEL_HOST}:{port}/api/generate  (REMOTE)
   network call: urlopen
```
Speaker notes: The address is built from an f-string, so the literal never appears in the source. The scanner found the template, could not resolve it, and labelled both lines remote, which is the opposite of the truth. It did find one thing worth having: exactly one network call in the whole tree, which tells you where to look.
Image: None. This slide is code.
---
## Slide 6: Read the two lines the tool could not
```
DEFAULT_PORT = 11634
MODEL_HOST = "127.0.0.1"

python study_buddy.py notes/chemistry.txt --hints --port 11634
No model answered at http://127.0.0.1:11634/api/generate.
```
Speaker notes: Now you know, and it took reading the file. Then the behavioural test: run it with an explicit port and the program prints its own address. Note the port. A real Ollama listens on 11434 and so do several stubs in this course, and a run against the wrong server looks exactly like a working run. This module uses 11634 and every command says so.
Image: None. This slide is code.
---
## Slide 7: Two of six answers answered the question
- "We take privacy extremely seriously"
- "We do not sell student data to third parties"
- "Industry-leading secure cloud providers"
- "Authorized personnel on a need-to-know basis"
Speaker notes: Four failures, and none of them are lies. Every one of those sentences is probably true. They are answers to questions nobody asked, and the reason they work is that they arrive in the tone of an answer.
Image: Four answer bubbles, each pointing at a different question than the one asked.
---
## Slide 8: What the good answer looked like
```
Upon written request within 30 days of termination, all customer
data is deleted from production systems and purged from backups
within 90 days.
```
Speaker notes: A trigger, an actor, and two deadlines. Specificity is the signal, and it is a property you can check for without knowing anything about the vendor. Count the specifics in any answer you are handed.
Image: None. This slide is code.
---
## Slide 9: The answer that opens a new question
- "Not used for training"
- "Aggregated, de-identified statistics improve the service"
- That is a good answer and a new row
- Be suspicious of the answer with no residue
Speaker notes: This is a vendor answering honestly and creating work for you. De-identified is a claim to be measured, which you proved yesterday with five records. An answer that raises a question is not a failure. The version that closes everything cleanly is the one to look at twice.
Image: One answer producing two new rows in an assessment table.
---
## Slide 10: How the decision actually gets made
- Somebody sees a page headed Privacy with a badge
- Says it looks fine. Two classes are using it by Friday
- Nothing errored. Nobody did anything wrong
- And nine questions were skipped
Speaker notes: By the time anybody asks, two classes have gradebooks in it and students have accounts. The cost of the answer being no has gone from zero to a week of everybody's time. The whole value of asking early is that no is still cheap.
Image: A timeline from hallway to two classrooms, with the questions never asked.
---
## Slide 11: What you are about to build
- Write the four questions you would send a vendor
- Run the network scan on your own project
- Then run the test that does not read source
- Write section 8 of your assessment
Speaker notes: Build one is the vendor questions for your own assessment's workflow, plus the code scan and the adapter-off test on your own project. Build two is section eight, with UNKNOWN written honestly wherever you do not have an answer, and every UNKNOWN carried down to section eleven.
Image: A section eight table with two answers and one honest UNKNOWN.
---
