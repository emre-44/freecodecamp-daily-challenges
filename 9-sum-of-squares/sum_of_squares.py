"""
Given a positive integer up to 1,000, return the sum of all 
the integers squared from 1 up to the number.
"""
def sum_of_squares(n):
    total = 0
    for x in range(1,n+1):
        total += x*x       
    return total

#Test Stage
print(sum_of_squares(5))