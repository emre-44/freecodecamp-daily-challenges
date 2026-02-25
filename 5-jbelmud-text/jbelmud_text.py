"""
Given a string, return a jumbled version of that string 
where each word is transformed using the following constraints:

The first and last letters of the words remain in place
All letters between the first and last letter are sorted alphabetically.
The input strings will contain no punctuation, and will be entirely lowercase.
"""
def jbelmu(text):
    """
    Generates a sorted characters between first and last character

    Args:
        text(string): The input string to proced
    Returns:
        string: The result string of the operation
    """

    words = text.split()
    result = []

    for word in words:
        letters = list(word)

        if len(letters) <= 2:
            result.append(word)
            continue

        first_letter = letters.pop(0)
        last_letter = letters.pop(-1)

        letters.sort()

        letters.insert(0, first_letter)
        letters.append(last_letter)

        result.append(''.join(letters))

    return ' '.join(result)

#Test Stage
print(jbelmu("hello world"))
