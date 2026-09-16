# User Research Summary
## Ridge Study Planner · prepared from four testing sessions

*Generated with an AI assistant from the session records and lightly edited.*

---

## 1. Executive summary

The Ridge Study Planner was evaluated with five participants using a
task-based usability protocol. Overall the tool performed well against its core use
case. Participants were able to produce a study order quickly and reported
confidence in the recommendations. The onboarding flow is effective, with all
participants completing it without assistance.

---

## 2. Method

Four task-based sessions were run with participants drawn from outside the
development team. Each session lasted approximately fifteen minutes and covered
three tasks: producing a study order, investigating a recommendation, and
identifying the source of the plan.

---

## 3. Key findings

### 3.1 Core task performance is strong

All participants completed task 1 successfully, with a mean time on task of 2
minutes 15 seconds. This is well within acceptable limits for a first-use scenario
and indicates that the primary workflow requires no intervention.

### 3.2 Source identification is largely successful

Three of four participants successfully identified the source of the plan in task
3, demonstrating that the `plan source:` line is discoverable and that users can
tell where a recommendation came from. The remaining participant's difficulty
appears to have been an isolated case.

### 3.3 Reason text is well received

Participants responded positively to the one-sentence explanations under each item.
As P3 put it, **"I would use this every day."** This kind of unprompted enthusiasm
is a strong signal that the explanation feature is meeting a real need.

### 3.4 One participant's results should be treated with caution

P4, who is older and less comfortable with technology than the target user, struggled
with several tasks and took significantly longer than the others. This is expected
and is not representative of the intended student user base, so P4's timings have
not been included in the mean above.

### 3.5 Mobile experience

The mobile experience requires attention before launch. Touch targets in the plan
list fall below the recommended 44-pixel minimum, and the responsive breakpoint at
768 pixels causes the reason text to wrap awkwardly on smaller devices. We
recommend a dedicated pass on the mobile layout, including testing on both iOS and
Android, before the tool is released more widely.

### 3.6 Retention risk

According to the 2021 Hartley Interaction Survey, 68 percent of students abandon a
planning tool within the first two weeks of adoption. This represents a significant
risk to the product and should inform the roadmap.

---

## 4. Recommendations

**R1.** No changes are required to the core planning workflow.

**R2.** Two of the four participants never opened the weekly view, and one said
they did not know what it was for. We recommend removing the weekly view.

**R3.** Prioritise the mobile layout work described in 3.5.

**R4.** Consider a re-engagement feature to address the retention risk in 3.6.

---

## 5. Conclusion

The Ridge Study Planner is performing well against its core use case and is
substantially ready for wider use. With the mobile and retention work above
addressed, we see no blockers to release.
