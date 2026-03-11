"""
Given an array of integers, return an array of integers that appear more than once in the initial array, 
sorted in ascending order. If no values appear more than once, return an empty array.

Only include one instance of each value in the returned array.

"""

def find_duplicates(arr):
    """
    Returns array of integers that appear more than once, sorted ascending.
    """
    seen = set()
    duplicates = set()
    
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return sorted(duplicates)

# Test Stage
print(find_duplicates([1, 2, 3, 4, 1, 2]))