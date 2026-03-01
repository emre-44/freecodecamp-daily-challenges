"""
Given a string, remove all spaces from the string, insert two spaces 
between every character, convert all alphabetical letters to uppercase, and return the result.

Non-alphabetical characters should remain unchanged (except for spaces).
"""

def space_jam(s):
    """
    Generates a double space between each character
    Args:
        s(string):The input string to be processed
    Returns:
        spacejam(string): The processed string with double spaces between each character
    """
    removed_space = s.replace(" ", "")
    spacejam_s = "  ".join(removed_space.upper())
    return spacejam_s

#Test stage
print(space_jam("spacejam"))