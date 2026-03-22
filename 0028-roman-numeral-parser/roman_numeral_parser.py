"""

Given a string representing a Roman numeral, return its integer value.
Roman numerals consist of the following symbols and values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000
Numerals are read left to right. If a smaller numeral appears before a larger one, 
the value is subtracted. Otherwise, values are added.
"""

def parse_roman_numeral(numeral):
    """
    Convert a Roman numeral string to its integer value.

    Args:
        numeral(str): A string containing Roman numerals

    Returns:
        int: The integer value of Roman numeral
    """
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    n = len(numeral)

    for i in range(n):
        current_value = roman_values[numeral[i]]

        if i+1 < n and current_value < roman_values[numeral[i+1]]:
            total -= current_value
        else:
            total += current_value
    
    return total

#Test Stage
print(parse_roman_numeral("XXVI"))