"""
Given a string, determine if all the characters in the string are unique.

Uppercase and lowercase letters should be considered different characters.
"""

def all_unique(s):
    letters = []
    for letter in s:
        letters.append(letter)
    
    for letter in letters:
        letters.remove(letter)
        if letter in letters:
            return False
    return True
print(all_unique("abc"))
