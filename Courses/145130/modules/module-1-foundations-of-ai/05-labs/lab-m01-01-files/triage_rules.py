# triage_rules.py  .  Lab M01-01, the side you write
#
# This is a decision tree. Every rule in it is a rule a person wrote on
# purpose, in an order a person chose on purpose. Nothing in this file was
# fitted to data, and nothing in it changes unless you change it.
#
# That is the whole point of the comparison you are about to run. When this
# file gives a wrong answer you can point at the line that did it. Hold that
# thought until you see the other side.
#
# The starter below runs. It also answers "other" for every ticket, which is
# useless. Your job is steps 3 through 6 of the lab.

LABELS = ["hardware", "software", "network", "account", "other"]


def contains_any(text, phrases):
    """True when any phrase appears in text. Case does not matter."""
    lowered = text.lower()
    for phrase in phrases:
        if phrase in lowered:
            return True
    return False


def classify(text):
    """Return one label from LABELS for one help request.

    The tree you are building, drawn out. Read it top to bottom. The FIRST
    branch that matches wins, which means the order of these branches is a
    decision you are making, not a detail.

        is it about getting in?          -> account
        is it about reaching something?  -> network
        is it about a program?           -> software
        is it about a physical object?   -> hardware
        none of the above                -> other

    TODO step 3: write the account branch.
    TODO step 4: write the network, software, and hardware branches.
    TODO step 5: write down, in the lab report, why you put them in that order.
    TODO step 6: run check_rules.py until the settled tickets pass.
    """
    return "other"


def explain(text):
    """Return the reason this tree gave the label it gave.

    A decision tree can always answer the question "why did you say that".
    Keep this honest: it must name the branch that actually fired.

    TODO step 7: make this return the branch name, not the placeholder.
    """
    return "no branch matched, so the tree fell through to other"


if __name__ == "__main__":
    # A quick way to try one sentence without touching the other programs.
    sample = "I am locked out of my account after changing my password."
    print(f"text:   {sample}")
    print(f"label:  {classify(sample)}")
    print(f"reason: {explain(sample)}")
