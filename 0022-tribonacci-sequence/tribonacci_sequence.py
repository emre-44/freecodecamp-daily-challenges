"""
The Tribonacci sequence is a series of numbers where each number is the sum of the three preceding ones. 
When starting with 0, 0 and 1, the first 10 numbers in the sequence are 0, 0, 1, 1, 2, 4, 7, 13, 24, 44.

Given an array containing the first three numbers of a Tribonacci sequence,
 and an integer representing the length of the sequence, 
return an array containing the sequence of the given length.

Your function should handle sequences of any length greater than or equal to zero.
If the length is zero, return an empty array.
Note that the starting numbers are part of the sequence.

"""
def tribonacci_sequence(start_sequence, length):
    """
    Generates a Tribonacci sequence starting from the given initial values.
    
    Args:
        start_sequence(list): A list of 3 numbers that will be the first three terms of the sequence
        length(int): Length of the output sequence
    Returns:
        result(list): A list containing the first 'length' terms of the Tribonacci sequence
    """
    if not start_sequence or len(start_sequence) < 3:
        return []

    result = list(start_sequence[:3])

    for i in range(3, length):

        next_value = result[i-1] + result[i-2] + result[i-3]
        result.append(next_value)

    return result[:length]

print(tribonacci_sequence([0, 0, 1], 20))
