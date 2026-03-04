"""
Given an integer, determine if that number is a prime number or a negative prime number.

A prime number is a positive integer greater than 1 that is only divisible by 1 and itself.
A negative prime number is the negative version of a positive prime number.
1 and 0 are not considered prime numbers.
"""
def is_unnatural_prime(n):
    """
    Checks natural and unnatural prime numbers
    Args:
        n(int): User input for check prime
    Returns:
        bool: This input is prime or not
    """
    if n == 1 or n == -1 or n == 0:
        return False
    elif n > 0:
        for i in range(2,(n//2)+1):
            if n % i == 0:
                return False
    elif n < 0:
        n = abs (n)
        for i in range(2,(n//2)+1):
            if n % i == 0:
                return False
    return True

#Test Stage
print(is_unnatural_prime(-15))
