"""
Given an array of integers and an array of string operators, apply the operations to 
the numbers sequentially from left-to-right. Repeat the operations as needed until 
all numbers are used. Return the final result.

For example, given [1, 2, 3, 4, 5] and ['+', '*'], return the result of evaluating 
1 + 2 * 3 + 4 * 5 from left-to-right ignoring standard order of operations.

Valid operators are +, -, *, /, and %.
"""

def evaluate(numbers, operators):
    """
    Applies arithmetic operations sequentially to the numbers from left to right.
    Args:
        numbers(list): A list of integers to perform operations on
        operators(list): A list of string operators ('+', '-', '*', '/', '%')
    Returns:
        int: 
    """
    result = numbers[0]

    op_index = 0

    for i in range (1,len(numbers)):
        operator = operators[op_index % len(operators)]

        if operator == "+":
            result += numbers[i]
        elif operator == "-":
            result -= numbers[i]
        elif operator == "*":
            result *= numbers[i]
        elif operator == "/":
            result /= numbers[i]
        elif operator == "%":
            result %= numbers[i]

        op_index += 1

    return result

#Test Stage
print(evaluate([5, 6, 7, 8, 9], ['+', '-']))
