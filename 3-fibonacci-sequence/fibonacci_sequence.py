"""
The Fibonacci sequence is a series of numbers where each number 
is the sum of the two preceding ones. When starting with 0 and 1, 
the first 10 numbers in the sequence are 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.

Given an array containing the first two numbers of a Fibonacci sequence, 
and an integer representing the length of the sequence, return an array 
containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence.

"""
def fibonacci_sequence(start_sequence, length):
    """
    Generate a Fibonacci sequence starting with given numbers.
    
    Args:
        start_sequence(list): A list containing the first two numbers of the Fibonacci sequence 
        length (int): The desired length of the sequence. Must be non-negative.
    
    Returns:
        list: A Fibonacci sequence 
    
    """

    if length < 0:
        return "Length cannot be negative!"
    if length == 0:
        return []
    if not isinstance(start_sequence, list) or len(start_sequence) < 2:
        return "Start sequence must be a list with at least 2 elements!"

    result = start_sequence[:]

    for i in range(2, length):
        result.append(result[i-1] + result[i-2])

    return result[:length]

#Test Stage
print(fibonacci_sequence([0,1], 12))
