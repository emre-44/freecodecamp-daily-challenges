"""
Given a string, return its camel case version using the following rules:

Words in the string argument are separated by one or more characters from the following set: 
space ( ), dash (-), or underscore (_). Treat any sequence of these as a word break.
The first word should be all lowercase.
Each subsequent word should start with an uppercase letter, with the rest of it lowercase.
All spaces and separators should be removed
"""

def to_camel_case(text):
    """
    Doc
    Args: 
        text(str): The user input for camel case
    Returns:
        str: Camel case string
    """
    for sep in ['-', '_']:
        text = text.replace(sep, ' ')

    words = text.split()

    if not words:
        return ""

    result = words[0].lower()

    for word in words[1:]:
        if word:
            result += word[0].upper() + word[1:].lower()

    return result

#Test Stage
print(to_camel_case("hello world"))
