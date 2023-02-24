"""Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only."""
def lengthOfLastWord(s):
    words = s.strip().split()
    return len(words[-1])
print(lengthOfLastWord("   fly me   to   the moon  "))