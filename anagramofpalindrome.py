"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.

Examples::

    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""
    chars = {}
    count = 0
    for char in word:
        chars[char] = chars.get(char,0) + 1
    for i in chars.values():
        if i % 2 != 0:
            count += 1
    if count <= 1:
        return True
    return False


# if __name__ == '__main__':
#     import doctest

#     if doctest.testmod().failed == 0:
#         print("\n*** ALL TEST PASSED. AWESOMESAUCE!\n")
#print(is_anagram_of_palindrome("ab"))