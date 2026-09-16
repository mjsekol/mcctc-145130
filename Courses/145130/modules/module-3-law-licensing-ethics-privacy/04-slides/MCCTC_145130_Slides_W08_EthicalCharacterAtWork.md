# Ethical Character, in Code, Where Nobody Is Watching
---
## Slide 1: You will never see the person you hurt
- Be unkind to a face and you see the face
- Publish the two lowest scores in the class
- You see a working feature and a green test
- The harm is real and outside your view
Speaker notes: Your program is a decision that runs by itself, thousands of times, for people you never meet. That is different from every other place character shows up in your life, because the feedback loop is broken. Today we make four abstract words into things you can look at in a file.
Image: A developer at a screen, and a separate panel of five people the screen never shows.
---
## Slide 2: Four traits, four places to look
- Honesty: the usage log and the limitations section
- Integrity: what the diff says at 11pm
- Compassion: the defaults and the error messages
- Justice: what the metric actually measures
Speaker notes: Honesty, integrity, compassion, justice. Every one of them has a file you can open. If you cannot point at the file, you are talking about a feeling rather than a practice, and feelings do not survive a deadline.
Image: Four repository files, each labelled with one trait.
---
## Slide 3: The 11pm failure modes, named in advance
- Delete the failing test instead of fixing it
- Widen the except until the error stops
- Commit generated work you have not read
- Write "works on my machine" as the testing section
Speaker notes: Every one of those is a real thing real professionals do under pressure. Naming them now is the point of this slide, because you recognize a failure mode faster when somebody told you its name before you were in it. All four are visible in the history forever, with your name on them.
Image: A commit history at 11pm, four commits flagged.
---
## Slide 4: The one rule that outranks everything
- The only way to fail outright here
- Is submitting work you cannot explain
- Gate 3 gives you every tool there is
- The submission is a claim, and it has to be true
Speaker notes: This rule is not about punishing you for using tools. It is here because the submission is a claim, and the claim is I made this and I stand behind it. If that claim is false, everything downstream of it is unreliable, including your own estimate of how long the next feature takes.
Image: A submit button with a sentence under it reading I can explain every line.
---
## Slide 5: The test, in four lines
```python
lines = open(path, encoding="utf-8").read().splitlines()
real = [(n, t) for n, t in enumerate(lines, 1)
        if t.strip() and not t.strip().startswith("#")]
step = max(1, len(real) // count)
picked = real[step // 2::step][:count]
```
Speaker notes: This picks lines out of a file and makes you explain them. Run it on your own work before a demo. Then run it on work you did not write and notice how different the two feel. That difference is what an interviewer is measuring in the first four seconds.
Image: None. This slide is code.
---
## Slide 6: Three lines, two questions each
```
line 17: import urllib.request
line 49: return None
line 82: "No model answered at "
  why is this line here, and what breaks without it?
  what would you have written instead, and why did you not?
```
Speaker notes: Line forty nine is the interesting one. It refuses to return a reply the model did not finish. Somebody who wrote it can tell you in a sentence why a half-finished hint is worse than no hint. Somebody who pasted it cannot, and it shows up in about four seconds.
Image: None. This slide is code.
---
## Slide 7: Twelve lines that publish two students
```
THIS WEEK'S DRILL LEADERBOARD
1. Marisol Vega          118 cards  61% correct
2. Devon Whitaker         96 cards  94% correct
3. Priya Raman            40 cards  88% correct
4. Aiden Kowalczyk        12 cards  42% correct
5. Zainab Osei             9 cards  33% correct
```
Speaker notes: No error. Twelve lines of code, a clean table, and every student invented. Now look at what it does. It ranks by cards drilled and calls that a leaderboard. The student at the top has the lowest accuracy of the top three.
Image: None. This slide is code.
---
## Slide 8: What that table measures
- Cards drilled, which is time available
- Time is not distributed evenly across a class
- Places four and five publish a low number
- The default is public, and the default is everybody
Speaker notes: The metric measures free time. Zainab works evenings at the family store, which you will read in the roster next week. Ranking by volume and calling it a leaderboard is a justice failure. Publishing the bottom two by name is a compassion failure. Calling it a leaderboard is an honesty failure.
Image: The same five rows with the metric column circled in accent red.
---
## Slide 9: One-line changes that fix it
- Rank by accuracy above a minimum attempt count
- Or show each student only their own progress
- Make participation something you opt into
- Show a top three and stop
Speaker notes: Each of those is a one-line change and each of them is an ethical decision. That is the whole point of this example. Ethics in software is not a seminar, it is a default value, a sort key, and a heading.
Image: Four small diffs, each one line long.
---
## Slide 10: The sentence that will get you
- "I understand it, I only could not have written it"
- Reading is a much weaker signal than writing
- Code you understand while reading
- Is code you cannot debug at 11pm
Speaker notes: That sentence is true in the moment and it is not evidence. You can follow a proof and not be able to prove it. Debugging requires knowing what the author was trying to do, and you were not the author. In a room where everybody uses the same tools, the person who slows down looks slower. For one week.
Image: Two panels: reading code calmly, and debugging the same code at night.
---
## Slide 11: What you are about to build
- Run the explain check on your own file, five lines
- Answer both questions out loud, timed
- Rewrite the leaderboard so it is defensible
- Name what your version is now worse at
Speaker notes: Build one is the explain check on work you wrote last week, five lines, timed, honest count. Build two rewrites the leaderboard. The requirement that carries the grade is the last one: name one thing your version is worse at. Every design choice gives something up, and an answer that claims to give up nothing has not been thought through.
Image: A rewritten leaderboard beside a short list of what it gave up.
---
