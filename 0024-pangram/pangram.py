"""
Given a word or sentence and a string of lowercase letters, determine if the word or 
sentence uses all the letters from the given set at least once and no other letters.

Ignore non-alphabetical characters in the word or sentence.
Ignore letter casing in the word or sentence.

"""

def is_pangram(sentence, letters):
    """
    Check it if letters contains all letters from sentence

    Args:
        sentence(str): Sentence for check
        letters(str): Letters for check if sentence have
    Returns:
        bool: Return value for sentence have letters
    """
    sentence_letters = set()

    for char in sentence:
        if char.isalpha():  
            sentence_letters.add(char.lower()) 

    letters_check = set(letters)

    return letters_check == sentence_letters

# Test Stage
print(is_pangram("Hello World!", "helowrd"))
