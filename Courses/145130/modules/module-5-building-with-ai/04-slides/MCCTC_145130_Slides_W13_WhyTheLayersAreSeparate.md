# Why the Model Layer and the Application Layer Are Separate
---
## Slide 1: The model answered in prose. Your program needs a shape.
- You asked for JSON
- Sometimes you get JSON
- Sometimes a code fence, a sentence, or a refusal
- Somebody has to turn one into the other
Speaker notes: You already know how to call something over HTTP. You did it last year with a weather feed and again with a local model. So the new thing today is not the HTTP call. The new thing is where you put the boundary. A language model answers in prose and your program needs a shape, and the whole design question this week is which part of your code has to know about that.
Image: A terminal showing three different model answers to the same prompt, one bare JSON, one in a code fence, one a polite refusal.
---
## Slide 2: Two programs, one written contract
```
You -> your application (C#) -> your model service (Flask) -> model or stub
          HttpClient               /health /generate             /api/generate
```
Speaker notes: There are two programs here, not one. The service is Python and it talks to the model. The application is C sharp and it talks to the service. Between them is a written contract, and for this week's demo service that file is called CONTRACT dot md. It says exactly what goes in, exactly what comes back, and exactly what every failure is called. Point at that file. It is the most important file in the folder.
Image: None. This slide is code.
---
## Slide 3: The four reasons, and you owe me all four
- Different jobs, different languages
- One place knows about mess
- One place knows how to fail
- You can replace either side
Speaker notes: Four reasons, and you will be asked for all four at your demonstration without reading them. Model runtimes are Python and your application is C sharp, so the two programs already exist. One place deals with fences and prose. One place owns the timeout, the retry, and the fallback. And either side can be swapped without touching the other, which you will actually do next semester.
Image: A four-quadrant diagram in navy and accent blue, each quadrant holding one reason.
---
## Slide 4: The machine this was built on has no model installed
```
  service          contract-demo-service
  model_endpoint   http://127.0.0.1:11535
  model_reachable  false

  The service is up and cannot see a model. Every answer will be a
  fallback. That is a different problem from the service being down.
```
Speaker notes: This is real output from the machine these materials were built on, and that machine has no model runtime installed at all. Read the third line. Reachable, no. And the service is still running, still answering, still telling you exactly what is wrong. Now watch what happens when I ask it to do something anyway.
Image: None. This slide is code.
---
## Slide 5: The model is gone and exactly one layer noticed
```
  source       fallback
  elapsed_ms   2057
  headline: The 3D printer in room 118 jammed near the nozzle.
  error kind:    connection_refused
  error message: nothing is listening at http://127.0.0.1:11535
```
Speaker notes: No crash. No stack trace. Nothing had to be recompiled. The caller got a headline, the same field it always gets, plus one extra piece of information: this did not come from the model. That is what the boundary bought. The model disappeared and exactly one layer had to care.
Image: None. This slide is code.
---
## Slide 6: ok and error are not opposites
- Read source first, every time
- source model means the model answered
- source fallback means the service built it
- source none means the request was refused
Speaker notes: Write this one down. In this envelope, ok and error are not opposites. A fallback answer has ok true, source fallback, and an error that says why the model was not used. That is the system working correctly on a day the model is unavailable. A program that treats it as a failure will refuse to work on a day it could have worked.
Image: A three-row table showing source, ok, and error for the three cases, with source highlighted in accent blue.
---
## Slide 7: Watch me do it wrong
```csharp
if (envelope.Ok)
{
    Console.WriteLine(result.Headline);   // looks fine
}
```
Speaker notes: Here is the shortcut. Read ok, print the answer, move on. Three lines, no branching, and it compiles. I am going to run this against a service that cannot see a model. Predict what the person sees before I press enter.
Image: None. This slide is code.
---
## Slide 8: A headline that nothing wrote
```
  headline: My laptop keeps dropping the wifi in the back corner of the lab.
```
Speaker notes: No error. No warning. Nothing red anywhere on this screen. That sentence was not written by a model. It is the first line of the request, copied by a rule inside the service, and the program presented it as though a model had written it. This is the shape you have met in every course here. The dangerous failure is the one that does not crash.
Image: None. This slide is code.
---
## Slide 9: The boundary costs you something, and you pay it first
- Two programs to start, two places a bug can be
- A contract to agree before either one works
- The benefit arrives the day the model is missing
- In this building that day is most days
Speaker notes: Be honest about this. On Monday the boundary is all cost. The team that puts everything in one program will be running before you are. The benefit shows up the first time the model is slow, or missing, or answering in a shape nobody planned for, and in this building that is most days. Do not let anybody tell you the tradeoff is free.
Image: A simple two-column comparison, cost on the left in muted grey, benefit on the right in accent blue.
---
## Slide 10: What you are about to build
- Lab M05-01, the contract trace, seven real cases
- Start the stub, the service, then the probe
- Fill in the table by reading, not guessing
- Your own design starts Tuesday
Speaker notes: Build one is lab M zero five dash zero one. You start two servers, you send seven requests, and you write down what came back for each one in a table. You are not writing code today. You are learning to read a contract, because on Tuesday you write your own and on Thursday somebody else has to build against it.
Image: A terminal with three windows tiled, the stub, the service, and the probe, with the envelope fields highlighted.
