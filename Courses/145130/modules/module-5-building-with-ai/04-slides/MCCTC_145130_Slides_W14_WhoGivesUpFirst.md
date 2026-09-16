# Who Gives Up First
---
## Slide 1: Twenty-one seconds of waiting, and no answer at all
- One note, two tasks, a slow model
- The service had a good answer ready at eight seconds
- Twice
- Nobody ever saw it
Speaker notes: This is real, captured from this week's Gate two program. One practice note, two tasks, against a service whose model takes eight seconds. Twenty one point three seconds of wall clock time and no answer at all. The service had a perfectly good labelled fallback ready at eight seconds, twice, and the person at the terminal never saw either one. Here is why.
Image: A stopwatch at 21.3 seconds beside an empty terminal, in navy and accent red.
---
## Slide 2: There are three clocks and you know about one
- The model takes as long as it takes
- The service has a timeout and a retry policy
- Your application has a timeout of its own
- Set them wrong and the symptom is silence
Speaker notes: Three clocks running in this system and most people only know about the one in their own code. The model is slow. The service has its own timeout and its own retry count. Your application has a timeout too, and probably one you typed because the number felt right. When these are set against each other wrongly, the symptom is not an error. It is a person staring at a terminal.
Image: Three concentric rings labelled model, service, application, with a different duration on each.
---
## Slide 3: The rule, and the arithmetic
```
service worst case = model timeout x (retries + 1)

  20 s timeout, 1 retry   ->  40 s worst case
  your client at 30 s     ->  you give up first, every time
  your client at 45 s     ->  you get the labelled fallback
```
Speaker notes: Write this line down. Your application has to wait longer than the service's own worst case, and the worst case is not the timeout. It is the timeout multiplied by the number of attempts. At the anchor stack defaults that is forty seconds, so a client at thirty gives up first every single time the model is slow.
Image: None. This slide is code.
---
## Slide 4: Work these three out before I show you
```
     model takes   service timeout   retries   client timeout
A        8 s            20 s            1          30 s
B        8 s             3 s            1          45 s
C        8 s             5 s            1           5 s
```
Speaker notes: Three settings. For each one write down two things: how long the person waits, and what they see at the end. Take ninety seconds. Do not guess, do the arithmetic. I am going to show you all three captured from a real run and I want you to have committed to an answer first.
Image: None. This slide is code.
---
## Slide 5: Setting B is the system working correctly
```
  [classify] from FALLBACK, not the model in 6297 ms
  why: timeout: no answer from the model within 3 seconds
  label: network
  note:  No model answer. A keyword rule in the service matched 'wifi'.
```
Speaker notes: Six point three seconds is two attempts at three seconds each. The client's forty five was never close to being tested. The person waits six seconds and gets a labelled fallback, and knows exactly where it came from. That is not a failure. That is the whole design doing its job on a day the model could not help.
Image: None. This slide is code.
---
## Slide 6: Setting C threw the answer away
```
  The model service took too long.
  the service at http://127.0.0.1:5157 did not answer within 5 seconds.

  The model service took too long.
  ... wall clock 21.3 s
```
Speaker notes: The message blames the model. The model was fine. The service was about to hand over an answer and this program gave up first, twice, and then retried on its own, which is how five seconds turned into twenty one. You threw away a good answer by being impatient, and then you printed a message that points at the wrong layer.
Image: None. This slide is code.
---
## Slide 7: More retries is the wrong fix
- Retry helps when the problem might be temporary
- It never helps when the reply itself is wrong
- Going from 1 retry to 3 takes 40 seconds to 80
- Thirty people, one model server, 149 minutes
Speaker notes: When people hit a timeout they raise retries, and that is backwards. Retrying a malformed body gets you the same malformed body and costs another twenty seconds. And every retry multiplies the worst case, which makes your client more likely to give up first, not less. The fix for a timeout is almost always a longer wait upstream, not more attempts downstream.
Image: A bar chart, one retry against three, showing the worst case doubling, in navy with the larger bar in accent red.
---
## Slide 8: Six lines that find it in one command
```csharp
double serviceWorstCase = report.TimeoutSeconds * (report.Retries + 1);
if (RequestTimeout.TotalSeconds <= serviceWorstCase)
{
    Console.WriteLine($"  This program gives up at {RequestTimeout.TotalSeconds:0.#} s");
    Console.WriteLine($"  and the service can take {serviceWorstCase:0.#} s. Raise the timeout.");
}
```
Speaker notes: The health endpoint already reports the service's timeout and its retry count. So ask for them, do the multiplication, and compare. Six lines, and the failure that used to take twenty one seconds of silence to find now takes one command. This is the cheapest thing in the whole module and almost nobody writes it unprompted.
Image: None. This slide is code.
---
## Slide 9: Why five seconds felt right
- A web page that takes 5 seconds is broken
- A query that takes 5 seconds is broken
- Two years of instinct says 5 seconds is generous
- All of that instinct is wrong here
Speaker notes: Five seconds is a completely sensible number in every other program you have written. You have two years of instinct saying it is generous, and all of it is wrong here, because there is a language model in the path and a local model on lab hardware is slow in a way nothing else you have called is slow. Never type a timeout as a number that feels good. Write it as arithmetic on the number below you.
Image: A comment block above a value, with the arithmetic spelled out in the comment, in accent blue.
---
## Slide 10: What you are about to build
- Read both numbers out of your own two programs
- Write the arithmetic in a comment beside each
- Add the health warning to your client
- Then make your model slow on purpose and watch
Speaker notes: Today you find your own two numbers, write the arithmetic in a comment beside each of them, and add the comparison to your health command. Then you start your model layer in slow mode on purpose and watch your own program either wait properly or give up first. Do not skip the second half. Reading the numbers is not the same as seeing it happen.
Image: A student comparing two numbers on two screens, with a slow-mode server running between them.
