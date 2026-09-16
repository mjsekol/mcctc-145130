# Modeling the Solution Before You Build It
---
## Slide 1: Two people. One design. Written down nowhere.
- You split the build on Monday
- You agreed out loud on "return the summary"
- You connect the halves on Thursday
- They do not fit
Speaker notes: Here is how this week goes wrong, and it goes wrong the same way every year. Two of you split the build. You agree out loud on what the service will return. Nobody writes it down, because you both understand it. On Thursday you connect the two halves and find out that you understood two different things. Today costs forty minutes and it is the cheapest forty minutes in this module.
Image: Two students at separate machines, a speech bubble between them containing the same words in two different shapes.
---
## Slide 2: Five tools, five different questions
- IPO chart: what goes in, happens, comes out
- Dataflow diagram: what moves between layers
- Decision table: every combination, what happens
- Pseudocode: the exact logic, no language
Speaker notes: These are not interchangeable and picking the wrong one is how design documents end up unread. The IPO chart is always first and always one page. The dataflow diagram is for when there is more than one program. The decision table is for three or more conditions that combine. Pseudocode is the step right before you write the function.
Image: Four icons in a row, navy outlines, each labelled with the question it answers rather than its name.
---
## Slide 3: The row everybody leaves off
```
Input            From              Allowed              Untrusted
command          the person        four words           yes
text             the person        1 to 4000 chars      yes
model answer     the model         any text at all      YES
```
Speaker notes: Look at the last row. The model's answer is an input to your system. It arrives from outside, you do not control it, and it is the input most likely to be shaped in a way you did not plan for. If it is not on your input list, your design has a hole in it and the hole is exactly where the refusals go.
Image: None. This slide is code.
---
## Slide 4: A decision table finds the row you would never write
```
#  HTTP        source     error   What the program does
1  200         model      null    print it, say it came from the model
2  200         fallback   set     print it, say it came from the fallback
3  400         none       set     do not print, name the kind
4  200         missing    any     not the envelope, name the port
```
Speaker notes: Row two is the point of this whole slide. Row two is a success that carries an error, and nobody writes row two by accident. You write it because you filled in the table and saw an empty cell staring at you. Rows five, six and seven are the wire failures, which is Week fourteen.
Image: None. This slide is code.
---
## Slide 5: Count the messages
- Seven rows in that table
- At least five different messages
- One word for all of them throws the answer away
- Each one has a different fix
Speaker notes: Count how many different messages a program needs to serve those seven rows. At least five. A program that prints the word Error for rows three through seven has thrown away the one thing the person actually needed, which is which of the five happened. You met this last year with 404 and timeout and rate limit. Same idea, new shapes.
Image: Five terminal lines stacked, each a different message, with the fix for each in accent blue beside it.
---
## Slide 6: Pseudocode is not code with the syntax removed
```
run_task(task, prompt):
    try:
        answer = ask the model, with a timeout, retrying only what can change
        result = parse the answer into this task's shape
        reason = check the result against this task's rules
        if reason is nothing: return envelope(source: "model")
        error = ("task_validation_failed", reason)
    catch a model failure as e:
        error = (e.kind, e.message)
    return envelope(source: "fallback", fallback result, error)
```
Speaker notes: Ten lines, and every decision the real service makes is in them. No imports, no syntax to get wrong, no language. The real function is twenty lines of Python and does exactly this. Here is the test of pseudocode. Hand it to your partner and ask them what happens when the model answers with something the parser cannot use. If they can answer from this alone, it is finished.
Image: None. This slide is code.
---
## Slide 7: You may use a model to help you model
- Draft a diagram or a decision table with it
- Check every line against your own code
- Record what you changed, in the decision log
- Submit nothing you cannot defend
Speaker notes: The competency names artificial intelligence alongside the graphic tools, which means using a model to help you model. That is allowed and it has one rule attached. Every draft you take from a model goes in your decision log with what you changed and why, and you defend it line by line. The only way to fail outright in this program is submitting work you cannot explain.
Image: A generated diagram on the left with three lines struck through in accent red, and a decision log entry on the right.
---
## Slide 8: What the design you did not write down produces
```
service returns:  {"summary": "...", "bullets": [...]}
client expects:   {"result": {"text": "...", "points": [...]}}

  summary:
```
Speaker notes: Neither of them is wrong. They never agreed. The C sharp program runs, deserialises without complaining, and prints one empty line, because System dot Text dot Json sets a missing field to its default rather than telling you. That is two days of work that do not fit together, found on Thursday, in a three week module.
Image: None. This slide is code.
---
## Slide 9: Why the tables feel like a waste of time
- Code on Monday gives you something on screen
- Tables on Monday give you nothing you can run
- The mistake found Monday costs a conversation
- The same mistake Thursday costs a rewrite
Speaker notes: Be honest about why people skip this. You can see code working and you cannot see a design working. Forty minutes of tables produces nothing on a screen. The cost is not paid evenly. A design mistake found on Monday costs you a conversation. The same mistake found Thursday costs both of you a rewrite, and Thursday of Week thirteen is the last day I am in the room before the competition week.
Image: Two cost curves, one flat and low, one rising steeply after Wednesday, navy and accent red.
---
## Slide 10: What you are about to build
- Lab M05-02 starts Thursday, design today
- Your IPO chart, one page, both of you
- Your result shape, in JSON, pasted into both files
- Your decision table, every row, including the empty ones
Speaker notes: Build one is your own IPO chart, on paper, both of you at one table. Build two is the result shape and the decision table. The rule for the result shape is that you do not describe it, you write it, in JSON, and both of you paste the same block into your own file. Not a description. The shape.
Image: Two students at one table with one sheet of paper between them, a JSON block visible on it.
