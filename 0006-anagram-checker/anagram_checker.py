"""
Given two strings, determine if they are anagrams of each other 
(contain the same characters in any order).

Ignore casing and white space.
"""

def are_anagrams(str1, str2):
    """
    Check if two strings are anagrams of each other.

     Args:
        str1 (str): First string to compare
        str2 (str): Second string to compare
    
    Returns:
        bool: True if the strings are anagrams, False otherwise
    """

    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)
