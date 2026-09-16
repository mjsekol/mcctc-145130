# Integrating Into Systems That Already Exist
---
## Slide 1: The failure is never in the model
- The model works
- Your program works
- The joint between them does not
- That joint has a name
Speaker notes: Yesterday you named nine technologies and the systems each has to be bolted onto. Today you stand at one of those joints and break it on purpose, seven different ways. The joint is called a seam, and nearly every interesting failure in a real system lives there rather than inside either side of it.
Image: Two solid blocks with a cracked join between them.
---
## Slide 2: A seam is three things
- A contract, written down
- A failure policy, decided in advance
- A record of where each value came from
- All three are yours today
Speaker notes: Write these three down. Nothing sits between your program and the model, so there is no layer writing the failure policy on your behalf and no field arriving with provenance already in it. You write all three today. That is more work than it sounds and it is the whole reason Module 5 exists.
Image: Three parts of a mechanical joint, labelled.
---
## Slide 3: Seven failures, one request
```
success        200  ok               1 call
success_prose  200  ok               1 call
error          500  http_error       1 call
rate_limited   429  rate_limited     2 calls
malformed      200  malformed_json   1 call
unusable       200  ok               1 call
slow           none timeout          2 calls
```
Speaker notes: Real output from the lab you are about to run. One help request, sent once per mode of the stand-in, so the only thing changing between rows is the failure. Look at the kind column. Your program worked those out from what it could see. Nothing handed them to you.
Image: None. This slide is code.
---
## Slide 4: Work from the outside in
- Did anything arrive at all
- Was the status 200
- Was the body JSON
- Did it say done, and was there text
Speaker notes: That order is not a style choice. Each check only makes sense if the one before it passed. A program that reads the status first crashes on the timeout row, because a request that never arrived has no status. Every one of you will write that bug once today, and the lab is arranged so you write it early.
Image: Four nested rings, checked from the outside inward.
---
## Slide 5: Two rows retried, five did not
- Rate limited, retried
- Timeout, retried
- Malformed JSON, not retried
- That was your rule, not the server's
Speaker notes: Nothing retries for you. The retried column is a function you wrote. Before I give you the rule, predict it. Why would those two be worth trying again and that one not.
Image: A bar chart of call counts per mode, two bars at two.
---
## Slide 6: The rule, in one sentence
- Retry a failure that might differ next time
- Never retry one that will not
- Timing failures might
- Content failures will not
Speaker notes: A rate limit and a timeout are about when. Wait and the same request can succeed. Malformed JSON is about what came back, and sending the same request to the same system gets the same broken answer while costing another twenty seconds of somebody's period. Retrying it is not being careful. It is the same mistake, repeated.
Image: Two doors, one marked try again and one marked it will be identical.
---
## Slide 7: Now look at the row that should bother you
```
unusable   200   ok   1 call
   response: "I am not able to help with that request."
```
Speaker notes: Status two hundred. Valid JSON. Done is true. Real text in the response field. Every single check your program makes passes, so your program says ok, and it is right to. And the answer is completely useless. Sit with that for a second, because it is the most important row in the table.
Image: None. This slide is code.
---
## Slide 8: Nothing you checked was about meaning
- Something arrived: yes
- Status 200: yes
- Body parsed: yes
- Text present: yes. Useful: nobody asked
Speaker notes: Walk the five checks with me. Every one of them has the right answer. Not one of them asks whether the text contains what the task actually needed. To catch this you have to write down the shape the task requires, a label from the five, and check the answer against it. Which means somebody has to define that shape first.
Image: A checklist with five ticks and a sixth line left blank.
---
## Slide 9: That is the argument for Module 5
- Every program talking to a model needs that check
- Writing it in each one is how it gets skipped
- Write it once, in a layer
- That layer is your Module 5 build
Speaker notes: You are going to feel this again on Friday, in a Gate 2 program that gets it wrong. The conclusion is not that today's design is bad. It is that this check belongs somewhere shared, and you build that somewhere in Module 5. Today you earn the right to think that is a good idea.
Image: Several programs each repeating the same check, then one shared layer.
---
## Slide 10: Four fixes, so four sentences
```
ok            -> "Answer from the model."
refused       -> "No model is running. Start the model server."
timeout       -> "The model did not answer in time. Wait and try again."
http_error    -> "The server has a problem of its own. Tell an adult."
```
Speaker notes: Timeout and rate limited share a sentence, and that is correct, because the action is identical. Two problems with two different actions may not share one. And notice the last branch in your code keeps the kind in the message: the person cannot act on malformed underscore json, but the adult they show it to can.
Image: None. This slide is code.
---
## Slide 11: What you are about to build
- Choose five or more modes, one must be slow
- Write kind_of, from the outside in
- Write one sentence per kind
- Write should_retry as a rule, not a list
Speaker notes: Build one is the three functions. Build two is the note the staff would actually read, and the part I grade hardest is section four: which row passed every check and was still useless, and what it would take to catch it. If you write that section well you have already made the case for your own Module 5 project.
Image: A table being filled in one row per failure mode.
---
