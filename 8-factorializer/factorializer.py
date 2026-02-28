"""
Given an integer from zero to 20, return the factorial of that number. 
The factorial of a number is the product of all the numbers between 1 and the given number.
"""
def factorial(n):
    """
    Calculates the factorial of a given number.
    Args:
        n(int): User input to calculate factorial
    Returns:
        result(int): The factorial of n
    """
    if n == 0:
        return 1
    
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

#Test Stage
print(factorial(0))
print(factorial(5))