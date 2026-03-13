"""
Given a named CSS color string, generate a random hexadecimal (hex) color code that is dominant 
in the given color.

The function should handle "red", "green", or "blue" as an input argument.
If the input is not one of those, the function should return "Invalid color".
The function should return a random six-character hex color code where the input color value 
is greater than any of the others
"""
import random
def generate_hex(color):
    """
     Generates a random hexadecimal color code where the specified color channel is dominant.

    Args:
        color(str): The dominant color
    Returns:
        str: A 6-character hex color code
    """
    if color not in ["red","green","blue"]:
        return "Invalid color"

    while True:
        r = random.randint(0,255)
        g = random.randint(0, 255)
        b = random.randint(0,255)

        if color == "red":
            condition = r > g and r > b
        elif color == "green":
            condition = g > r and g > b
        else:
            condition = b > r and b > g

        if condition:
            return f"{r:02X}{g:02X}{b:02X}"

#Test Stage
print(generate_hex("red"))
