"""
Given a string that contains properly nested parentheses, return the decoded version of the string using the following rules:

All characters inside each pair of parentheses should be reversed.
Parentheses should be removed from the final result.
If parentheses are nested, the innermost pair should be reversed first, and then its result should be included in the reversal of the outer pair.
Assume all parentheses are evenly balanced and correctly nested.
"""


def decode(s):
    """
    Decodes a string by reversing characters inside each pair of parentheses.
    Args:
        s(str): User input for decode.
    Returns:
        str: Decoded version of the input string.

    """
    stack = []

    for char in s:
        if char == ')':
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop()
            stack.extend(temp)
        else:
            stack.append(char)

    return ''.join(stack)


# Test Stage
print(decode("((is?)(a(t d)h)e(n y( uo)r)aC)"))
