"""
Given an array of integers representing the price of different laptops, 
and an integer representing your budget, return:

The second most expensive laptop if it is within your budget, or
The most expensive laptop that is within your budget, or
0 if no laptops are within your budget.
Duplicate prices should be ignored.
"""


def get_laptop_cost(laptops, budget):
    """
    Finds the most suitable laptop price within the given budget
    
    Args:
        laptops(list): An array of laptop prices
        budget(int): The maximum amount the consumer can spend
    Returns:
        int: The price of the laptop to buy
    """

    if laptops[-2] <= budget:
        return laptops[-2]
    
    result = 0
    for price in laptops:
        if price <= budget:
            if result <= price:
                result = price
    return result

#Test Stage
print(get_laptop_cost([1500, 2000, 1800, 1400], 1900))
print(get_laptop_cost([2099, 1599, 1899, 1499], 1000))