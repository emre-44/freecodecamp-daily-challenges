"""
Vowel Balance

Given a string, determine whether the number of vowels 
in the first half of the string is equal to the number 
of vowels in the second half.

The string can contain any characters.
The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
If there's an odd number of characters in the string, ignore the center character.

"""


def is_balanced(s):
    """
    Checks if number of vowels in first half equals second half
    """
    s = s.replace(" ", "")
    length = len(s)
    middle = length // 2

    if length % 2 == 0:
        word1 = s[:middle] #string slicing
        word2 = s[middle:]
    else:
        word1 = s[:middle] #string slicing
        word2 = s[middle+1:]

    vowels = "aeiou"
    vowels_word1 = []
    vowels_word2 = []

    for letter in word1.lower():
        if letter in vowels:
            vowels_word1.append(letter)

    for letter in word2.lower():
        if letter in vowels:
            vowels_word2.append(letter)

    if len(vowels_word1) == len(vowels_word2):
        print("This word is vowel balanced")
    else:
        print("This word is not vowel balanced")

    return s

is_balanced("car")
is_balanced("vowel balance")
is_balanced("freecodecamp")
is_balanced("cake")
