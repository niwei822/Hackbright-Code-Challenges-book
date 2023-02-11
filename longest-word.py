"""Return longest word in list of words.

For example::

    >>> find_longest_word(["hi", "hello"])
    5

    >>> find_longest_word(["Balloonicorn", "Hackbright"])
    12

"""


def find_longest_word(words):
    """Return longest word in list of words."""
    counts = []
    for word in words:
        counts.append(len(word))
    return max(counts)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YOU'RE THE MAX!\n")
