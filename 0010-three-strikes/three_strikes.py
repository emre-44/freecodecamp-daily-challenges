"""
Given an integer between 1 and 10,000, return a count of 
how many numbers from 1 up to that integer whose square contains at least one digit 3.
"""

def squares_with_three(n):
    """
    Return integer whose square contains at least one digit 3.
    Args:
        n(int): User input for find squares with three

    Returns:
        count(int): The quantity of numbers containing three
    """
    try:
        if 1 <= n and n <= 10000:
            count = 0
            for x in range (1,n+1):
                square = x*x
                if '3' in str(square):
                    count += 1
        else:
            print("Input integer between 1 and 10000")

    except TypeError:
        print("Error: n must be a number")
        return None
    
    return count