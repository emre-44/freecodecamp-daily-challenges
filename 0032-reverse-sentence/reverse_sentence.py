"""
Given a string of words, return a new string with the words in reverse order. For example, the first word should be at the end of the returned string, and the last word should be at the beginning of the returned string.

In the given string, words can be separated by one or more spaces.
The returned string should only have one space between words.
"""

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = list(reversed(words))
    reversed_sentence = " ".join(reversed_words)

    return reversed_sentence

print(reverse_sentence("world hello"))