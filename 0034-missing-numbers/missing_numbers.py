"""
Given an array of integers from 1 to n, inclusive, return an array of all 
the missing integers between 1 and n (where n is the largest number in the given array).

The given array may be unsorted and may contain duplicates.
The returned array should be in ascending order.
If no integers are missing, return an empty array.
"""

def find_missing_numbers(arr):
    if not arr:
        return []
    
    largest_num = max(arr)  
    num_set = set(arr)  
    
    missing = []
    for i in range(1, largest_num + 1):
        if i not in num_set:
            missing.append(i)
    
    return missing