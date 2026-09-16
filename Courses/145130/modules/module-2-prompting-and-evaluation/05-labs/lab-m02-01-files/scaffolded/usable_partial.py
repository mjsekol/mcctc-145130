# usable_partial.py  ·  SCAFFOLDED starter for Lab M02-01, step 19
#
# The first two checks are written. You write the other three.
# Copy this function into plan_check.py, replacing the one that is there.

REQUIRED_STEPS = 4


def usable(data):
    """Return an error message, or None if this reply can be used."""
    if not isinstance(data, dict):
        return "the reply is not a JSON object"
    if not isinstance(data.get("topic"), str) or not data["topic"].strip():
        return "the reply has no topic"

    # YOU WRITE THE REST.
    #
    # 1. 'steps' is missing, or it is not a list.
    #    Check the type before you check the length. A string has a length too,
    #    and len("soon") is 4, which would pass a length check for four steps.
    # 2. 'steps' does not have exactly REQUIRED_STEPS items.
    # 3. Any step is not text, or is text that is only whitespace.

    return None
