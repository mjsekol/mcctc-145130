# Four Failures, Four Messages
---
## Slide 1: The program said "Something went wrong"
- Four different problems
- Four different fixes
- One word for all of them
- The person tries the wrong fix three times out of four
Speaker notes: Somebody comes to you and says the program printed something went wrong. Which of four completely different things happened. You cannot tell, they cannot tell, and neither can the program, because it threw that information away before it printed. This is the same lesson as 404 and timeout and rate limit from last year, in a new shape.
Image: One terminal line reading Something went wrong, with four different repair paths branching from it in muted grey.
---
## Slide 2: Two levels of failure, and they have different owners
- Level one: the wire between your application and the service
- Level two: inside the envelope, what the service found
- Level one is four kinds plus one refusal
- Level two is one field called source
Speaker notes: There are two levels here and they are not the same kind of thing. Your application can fail to reach the service at all. Or it can reach the service, get an answer, and the answer says the model gave nothing usable. Those two have different owners, different fixes, and different messages. A program that mixes them up sends somebody looking in the wrong building.
Image: A two-band diagram, the upper band the HTTP wire, the lower band the envelope, in navy and accent blue.
---
## Slide 3: The four wire failures
```
ServiceDown        nothing is listening      start the service
Timeout            there, did not answer     wait, or raise the timeout
HttpError          a status, no envelope     look at the service console
MalformedPayload   answered, not the shape   you are on the wrong port
```
Speaker notes: Four kinds, four fixes. And there is a fifth outcome that is not a wire failure at all: RequestRejected. The service read your request, refused it with a 400, and the envelope says why. That is your mistake and nothing was asked of the model, and the message should say so, because otherwise somebody goes looking at the model.
Image: None. This slide is code.
---
## Slide 4: The message that saves the period
```
  The reply was not the shape this program expects.
  the reply to HTTP 404 was not the response this program expects: the
  response has no source field
  Confirm ... First 120 characters received: {"error": "not found"}
```
Speaker notes: This is the most common mistake in this lab: pointing the client at the model endpoint instead of at the service. Look at the last line. Printing the first hundred and twenty characters of whatever it received is the whole trick. The person sees error not found and knows in one second that something is answering and it is the wrong something.
Image: None. This slide is code.
---
## Slide 5: Two things about HttpClient nobody tells you
```csharp
catch (TaskCanceledException) when (token.IsCancellationRequested == false)
{
    return Failed(Timeout, $"did not answer within {http.Timeout.TotalSeconds:0.#} s.");
}
catch (HttpRequestException error) when (IsConnectionRefused(error))
{
    return Failed(ServiceDown, $"nothing is listening at {BaseAddress}.");
}
```
Speaker notes: Two details you will get wrong if nobody says them out loud. HttpClient reports its own timeout by cancelling the task, so you catch TaskCanceledException, and you check the token first or you will report a timeout when the user pressed control C. And a refused connection arrives as HttpRequestException with a SocketException inside it, so you read the socket error code.
Image: None. This slide is code.
---
## Slide 6: A 200 status is not proof
```csharp
public string? Problem()
{
    if (string.IsNullOrWhiteSpace(Source)) return "the response has no source field";
    if (string.IsNullOrWhiteSpace(Task))   return "the response has no task field";
    if (Ok && HasResult == false)          return "says ok, but carries no result";
    return null;
}
```
Speaker notes: Nothing throws here, and that is the point. System dot Text dot Json will happily deserialise a completely different object into your class and set every field it did not find to its default. Ok becomes false, Source becomes null, no exception anywhere, and your program prints something confident and empty. You have to check the shape yourself.
Image: None. This slide is code.
---
## Slide 7: Then read source, and say what you found
- from the model, or from the FALLBACK, not the model
- Print error.kind under it when there is one
- One word is the difference for the person reading
- Without it the two runs look identical
Speaker notes: Level two. The call worked, so now read source and say it out loud. From the model, or from the fallback, not the model. That one word is the whole difference for the person reading the output, because a fallback summary is a sentence copied out of the input by a keyword rule, and without the label it looks exactly like something a model wrote.
Image: Two identical-looking terminal outputs side by side, with one word different, highlighted in accent blue.
---
## Slide 8: Six messages, and every word is false
```
for task in TASKS:
    try:
        envelope = ask_with_retries(url, task, message["text"])
        show(envelope)
    except Exception:
        pass
from_model += 1

Digest finished. 6 messages summarized by the model, 0 built from the fallback.
```
Speaker notes: This ran against a service where the model was never used once. The model summarised nothing. The counter counted loop iterations. The except Exception pass swallowed two real failures. And it exited with code zero, so a script that called it believed everything worked. A program that reports success it did not have is worse than one that crashes, because a crash sends somebody to look.
Image: None. This slide is code.
---
## Slide 9: Why except Exception pass is tempting
- It makes the red text go away
- The loop now runs to the end
- The output looks complete
- Not crashing is not the same as working
Speaker notes: Be honest about why people write it. It is one line, it is late in the period, the red text was the thing stopping you from finishing, and now the loop runs to the end and the output looks complete. Not crashing feels like working. The gap between those two is exactly where this kind of bug lives, and it is the gap this whole course keeps pointing at.
Image: A terminal with no red text and a caption reading nothing here is true, in accent red.
---
## Slide 10: What you are about to build
- Wire your client to your service today
- Four failure kinds, four different messages
- Each message says what to do, not what happened
- Count what happened, not how many times the loop ran
Speaker notes: Today you connect your two halves. The acceptance criterion is not that it works. It is that you can produce all four wire failures on purpose, by stopping the service, by pointing at the wrong port, by making the service slow, and by having it return something that is not your envelope, and that each one prints a different sentence naming what to do.
Image: A student terminal with four failure messages captured in a scrollback, each one different.
