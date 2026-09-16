# parse_plan.py  .  Lab M05-02, Parse What The Model Said  .  STARTER
#
# This file runs. It imports, every function returns, and nothing crashes.
# It also parses nothing, so every test in test_parse_plan.py that matters
# fails. That is the starting line, not a bug.
#
# The shape you are building, and the only shape the rest of the program will
# ever see:
#
#   {"title": str, "steps": [str], "minutes": int}
#
# Two functions, and keeping them apart is the point of the lab.
#
#   parse_study_plan(text)     pull a shape out of the mess. Return a dict or
#                              None. Do not decide whether it is good enough.
#   validate_study_plan(plan)  decide whether it is good enough. Return the
#                              reason it is not, or None when it is fine.
#
# A parser that also validates gives the caller one answer, None, for ten
# different problems. The service above you has to write a real reason into
# the envelope, and it cannot invent one you did not give it.
#
#   python test_parse_plan.py
#   python run_answers.py
#
# Standard library only. Nothing here talks to a model or to a network.

import json
import re

# The field limits. These are not suggestions. The planner screen prints the
# title on one line, walks the steps as a checklist, and starts a timer from
# the minutes.
MAX_TITLE_CHARACTERS = 120
MAX_STEP_CHARACTERS = 160
MIN_STEPS = 2
MAX_STEPS = 8
MIN_MINUTES = 5
MAX_MINUTES = 240

# Three patterns you will want. You may add more.
# A fenced block, with or without a language tag after the backticks.
FENCE_PATTERN = re.compile(r"```[a-zA-Z0-9_-]*\n(.*?)```", re.DOTALL)
# A bullet or a numbered item. A model picks either one and does not tell you.
STEP_PATTERN = re.compile(r"^\s*(?:[-*•]|\d+[.)])\s+(.*\S)\s*$")
# A "Label: value" line, for the answers that are prose and not JSON.
LABEL_PATTERN = re.compile(r"^\s*(title|plan|steps|minutes|time)\s*:\s*(.*)$", re.IGNORECASE)


def strip_fences(text):
    """The inside of the first fenced block, or the text unchanged.

    STEP 1. Models wrap JSON in a code fence about as often as they do not,
    and the backticks are not valid JSON. Use FENCE_PATTERN.
    """
    return text.strip()


def find_json_object(text):
    """A dict parsed out of the text, or None.

    STEP 2. Try the whole string first. If json.loads raises, try again on
    the widest run from the first { to the last }. The second attempt is
    what rescues an answer that opens with "Sure, here is the JSON".
    """
    return None


def as_minutes(value):
    """A whole number of minutes, or None.

    STEP 4. A model asked for a number sends "about 25 minutes" often enough
    that refusing it throws away a usable answer. Pull the first run of
    digits out of a string. Return None when there are none.
    """
    return None


def as_steps(value):
    """A list of strings from whatever the model put in the steps field.

    STEP 5. A list of strings is the good case. A model asked for a list
    sometimes sends one string with newlines in it instead.
    """
    return []


def build_plan(title, steps, minutes):
    """One study_plan, trimmed to the field limits.

    STEP 6. Trim here and only here. Trimming is shape work, not judgement,
    so it belongs to the parser and not to the validator.
    """
    return {"title": title, "steps": steps, "minutes": minutes}


def parse_study_plan(text):
    """Model text to {"title", "steps", "minutes"}, or None if nothing fits.

    STEP 3 and STEP 7. JSON first, because a JSON answer is unambiguous.
    Prose second, because reading prose means guessing, and you guess last.
    """
    return None


def validate_study_plan(plan):
    """The reason this plan is unusable, or None when it is fine.

    STEP 8. One sentence per rule, written for a person, not a stack trace.
    The sentence you write here is what ends up in the envelope's error
    message, and somebody reads it at 11pm trying to work out what broke.
    """
    return "validate_study_plan has not been written yet"


def fallback_study_plan(request_text):
    """A plan built here, with no model involved.

    STEP 9. It is allowed to be worse than a model plan. It is not allowed
    to fail your own validator, because then a failure becomes two failures.
    """
    return {"title": "", "steps": [], "minutes": 0}
