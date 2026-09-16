# measure.py  .  Lab M01-04, the three functions the whole benchmark rests on
#
# bench.py does the talking to the model. This file does the arithmetic, and
# the arithmetic is where benchmarks go wrong. A number that is measured
# carefully and divided carelessly is still a wrong number, and it looks
# exactly as confident as a right one.
#
# Three functions, and one rule that governs all of them:
#
#   when you cannot know a number, return None. Never return a guess.
#
# Run python check_measure.py until every case passes.


def median(values):
    """Return the middle value of a list of numbers.

    Why median and not average: one slow run, usually the first, drags an
    average somewhere no run actually was. The median is the value a typical
    run had.

    With an even number of values there is no single middle, so return the
    average of the two middle values. With an empty list there is no answer at
    all, so return None.

    TODO step 4.
    """
    return None


def generation_ms(total_ms, ttft_ms):
    """Return the milliseconds spent generating text after the first token.

    Why this exists: total latency includes the wait before any text appears.
    Tokens were not being produced during that wait, so dividing tokens by
    total latency reports a rate the model never ran at.

    Return None when ttft_ms is None, because a server that does not stream
    cannot tell you when the first token arrived, and None is the honest
    answer. Return None when ttft_ms is larger than total_ms, because that
    measurement contradicts itself and a negative duration is not a duration.

    TODO step 5.
    """
    return None


def tokens_per_second(token_count, generation_milliseconds):
    """Return tokens divided by seconds of generation, or None.

    Return None when generation_milliseconds is None or is zero or less. A
    rate over no time is not a large rate, it is not a rate.

    Round to one decimal place. More digits than that claim a precision this
    measurement does not have.

    TODO step 6.
    """
    return None
