"""
Given two arrays with strings values, 
return a new array containing all the values that appear in only one of the arrays.

The returned array should be sorted in alphabetical order.
"""


def array_diff(arr1, arr2):
    """
    This functions checks two arrays and returns sorted unique words

    Args:
        arr1: First array for check
        arr2: Second array for check
    
    Returns:
        array: Unique words array
    """
    diff = []
    for letter in arr1:
        if letter not in arr2:
            diff.append(letter)

    for letter in arr2:
        if letter not in arr1:
            diff.append(letter)

    diff.sort()
    return diff

print(array_diff(["apple", "banana"], ["apple", "banana", "cherry"]))
