# Output Your Program Can Parse
---
## Slide 1: Today the reader is a program and it has no patience
- Everything this week assumed a human reading the reply
- A human copes with a friendly sentence before the list
- A parser does not
- A human reading about six items knows what to do
- Your code does not
Speaker notes: Three days of this week have been about a person reading the output. Today the reader is your program, and that changes the requirements completely. A friendly opening sentence is pleasant to a human and fatal to a parser. About six items is understandable to a human and meaningless to an integer conversion. You have written programs that consume APIs for two years, and everything you learned there is about to be the wrong instinct.
Image: Two readers side by side, a person shrugging at a messy reply and a parser icon stopped at a red error.
---
## Slide 2: A model has no contract
- An API tells you the shape before you call it
- You build against that guarantee and it holds
- A model gives you roughly the shape you asked for
- Most of the time
- Your program has to survive the rest of the time
Speaker notes: This is the sentence that reframes the whole day. An API has a contract. You read the documentation, you know which keys come back, and if the shape changes somebody versioned it and told you. A model has no contract. There is no schema, no guarantee, and nobody to tell. It will hand you something shaped roughly like what you asked for most of the time, and the whole engineering problem is the rest of the time.
Image: Two contracts side by side, one signed and stamped, one blank with the word probably written on it.
---
## Slide 3: Three rules, in order of how often they are skipped
- Ask for the shape, and say the word only
- Validate before you trust
- Decide what happens when it is wrong, before it is wrong
- Silence is not a plan
Speaker notes: Return JSON is an invitation. Return only JSON, no other text, is an instruction. The difference is four words. Second rule. Parsing succeeding does not mean the data is what you asked for, and that catches people who have never seen it fail. Third rule, and it is the one that separates a demo from a program. The model will eventually return something unusable. That is not an exception case, it is a normal Tuesday, and your program needs a decided answer before that Tuesday arrives.
Image: Three numbered rules descending, each with a small counter showing how often it is skipped.
---
## Slide 4: The wrong way. Is this reply JSON?
```
Explain the Friday equipment checkout. Return JSON with keys subject, steps.

Here are some thoughts on the Friday equipment checkout.

{
  "subject": "the Friday equipment checkout",
  "steps": [
    "Open the checkout sheet before anyone lines up",
    "Set the return slot to the next school day, first period"
  ]
}

It is worth noting that outcomes vary by situation. Many educators agree that
consistency matters more than any single rule.
```
Speaker notes: I have trimmed the step list to fit the slide, and the full reply has six of them. Ask the room whether that is JSON, and take a show of hands. Most hands go up, and they are looking at the braces in the middle and ignoring everything around them. Hold that vote. I am about to hand exactly this reply to a parser in front of you.
Image: None. This slide is the recorded run.
---
## Slide 5: What the parser says
```
python -c "import json; r=json.load(open('runs/loose.json',encoding='utf-8')); json.loads(r['response'])"

json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
```
Speaker notes: Line one, column one. Read that carefully, because it tells you something specific. The parser never reached your JSON. It read the letter H from Here are some thoughts, which is not how a JSON document starts, and it stopped there. Everything below it, all the correct braces and keys and the six good steps, was never looked at.
Image: None. This slide is the error.
---
## Slide 6: Four words between working and broken
- The strict prompt file differs by four words
- The words are only and no other text
- That version parses, with keys steps and subject
- You are shifting a probability, not issuing a command
- Which is exactly why your program still has to check
Speaker notes: Run the strict version and parse it in front of them. Parsed OK, keys steps and subject. Two prompts, four words apart, and one of them your program can use. Now be honest about the mechanism. The model is not obeying you. Text that follows return JSON with keys often has a friendly sentence in front of it, because that is how such answers are usually written. Text that follows only JSON, no other text, much less often does. You moved a probability. A shifted probability is not a guarantee, and next week is full of cases where it did not hold.
Image: Two prompt files side by side with the four extra words highlighted in accent blue.
---
## Slide 7: Valid JSON, useless data
```
reply = '{"subject": "checkout", "steps": "I will list them shortly", "count": "about six"}'
data = json.loads(reply)          # succeeds
print(type(data["steps"]).__name__)
print(data["count"] + 1)

str
TypeError: can only concatenate str (not "int") to str
```
Speaker notes: The parse succeeded. No error, no complaint, and a dictionary came back. Steps was supposed to be a list and it is a string. Count was supposed to be a number and it is the words about six. The JSON is valid and the data is wrong, and your program found out one line later when it tried to do arithmetic on the word about.
Image: None. This slide is the recorded run.
---
## Slide 8: The check your program needs, written out
```python
def usable(data):
    """Return an error message, or None if the reply can be used."""
    if not isinstance(data, dict):
        return "the reply is not an object"
    if not isinstance(data.get("subject"), str) or not data["subject"].strip():
        return "subject is missing or empty"
    steps = data.get("steps")
    if not isinstance(steps, list) or not steps:
        return "steps is missing or is not a non-empty list"
    if not all(isinstance(s, str) and s.strip() for s in steps):
        return "at least one step is not text"
    return None
```
Speaker notes: Read what this does. Is it an object. Is subject a non-empty string. Is steps a list, and is it non-empty. Is every step actual text. Now read what it does not do, because that is the part worth arguing about. It says nothing about whether the steps are correct, safe, in the right order, or about your school. It checks shape, and shape is all a program can check. Everything else is a human, and it is next week.
Image: None. This slide is the validator.
---
## Slide 9: Every way a reply can be unusable
```
| Mode | What ask.py reports | Exit code |
|---|---|---|
| error | the server answered HTTP 500 | 3 |
| malformed | not valid JSON | 4 |
| missing_response | the reply has no 'response' field | 5 |
| not_done | the reply is not marked done | 5 |
| empty_response | the reply is empty | 5 |
| rate_limited | waits for Retry-After, retries 3 times, then 429 | 3 |
| slow --delay 30 | no answer inside 20 seconds | 6 |
| (nothing running) | nothing is listening at the endpoint | 2 |
```
Speaker notes: Eight ways to fail and ask dot py already tells them apart. Cause each one on purpose before you build anything that depends on a model, because a failure you have seen once is a failure you will handle. Look at the exit codes and notice they are not all the same, which is deliberate. Different failures want different responses from the caller.
Image: None. This slide is the recorded failure table.
---
## Slide 10: Three of those return HTTP 200
- not_done, missing_response and empty_response all return 200
- A program that checks the status code trusts all three
- Status two hundred reads as success and is not
- The reply is partial, or keyless, or empty
- The dangerous outputs are the ones that look finished
Speaker notes: This is the running thread of the module showing up at the network layer. Three of those failure modes hand your program a clean HTTP two hundred. Nothing is red. Nothing throws. A program that only checks the status code treats a partial reply, a reply with no response field, and an empty string as three successes. Tomorrow you review a program that looks better than anything you would have written, and it has a defect in each of these areas.
Image: Three HTTP 200 responses in green, each with a different broken body underneath it.
---
## Slide 11: What you are about to build
- Lab M02-01 steps seventeen through twenty-one
- Ask for JSON two ways and compare what parses
- Write the usable validator and prove it rejects a bad reply
- Run against six stub failure modes, one exit code each
- Then Prompt Autopsy prompts four and five
Speaker notes: Build one is the lab. Acceptance is that your usable function rejects a reply with steps as a string and accepts a correct one, and that your script exits with a different, correct code for each of error, malformed, missing response, not done, and empty response. Put a short table of mode against exit code in your write-up. Build two is prompts four and five of the autopsy, and at least one of them has to ask for structured output. By the end of today you should have five recorded runs and a full comparison table, and the question I will ask at close is whether your five prompts are five genuinely different prompts or five rewordings. That distinction is the project.
Image: A terminal showing five different exit codes from five deliberate failures, each labelled.
---
