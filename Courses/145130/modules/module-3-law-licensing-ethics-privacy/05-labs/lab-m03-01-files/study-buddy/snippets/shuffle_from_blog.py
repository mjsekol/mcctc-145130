# Found on a blog post titled "Five Python one-liners I use every day".
# Pasted in by the Study Buddy team. No license was stated on the page.
#
# INVENTED SNIPPET. Written for the MCCTC 145130 Module 3 licensing fixture.


def shuffle_in_place(items, seed=0):
    """Deterministic shuffle so the deck order is repeatable for testing."""
    state = seed if seed else 1
    for i in range(len(items) - 1, 0, -1):
        state = (1103515245 * state + 12345) % 2147483648
        j = state % (i + 1)
        items[i], items[j] = items[j], items[i]
    return items
