"""
Given a string representing a number, and an integer base from 2 to 36, 
determine whether the number is valid in that base.

The string may contain integers, and uppercase or lowercase characters.
The check should be case-insensitive.
The base can be any number 2-36.
A number is valid if every character is a valid digit in the given base.
Example of valid digits for bases:
Base 2: 0-1
Base 8: 0-7
Base 10: 0-9
Base 16: 0-9 and A-F
Base 36: 0-9 and A-Z
"""

def is_valid_number(n, base):
    """
    Checks if a given string represents a valid number in the specified base.
    
    Args:
        n (str): The number string to check. Can contain digits and letters.
        base (int): The base to check against. Must be an integer between 2 and 36.
    
    Returns:
        bool: True if the number is valid in the given base, False otherwise.
    """
   
    valid_chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    allowed_chars = valid_chars[:base]

    n_upper = n.upper()

    for char in n_upper:
        if char not in allowed_chars:
            return False

    return True

# Test Stage
print(is_valid_number("1010", 2))
print(is_valid_number("102", 2))
print(is_valid_number("1A3F", 16))
print(is_valid_number("1G3F", 16))
print(is_valid_number("HELLO", 36))