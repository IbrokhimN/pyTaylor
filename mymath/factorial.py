"""
Fast approximation of factorial using Stirling's formula.
Accurate for large n, works for n >= 0. For small integers, Python's math.factorial is exact.
"""

import math

def factorial(n: int) -> float:
    """
    Calculate n! using Stirling's approximation.
    
    Formula:
        n! ≈ sqrt(2 * pi * n) * (n / e)^n
    
    For better accuracy, a correction term can be added:
        n! ≈ sqrt(2 * pi * n) * (n / e)^n * (1 + 1/(12n))
    
    Args:
        n (int): Non-negative integer.
    
    Returns:
        float: Approximate factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1.0

    # Stirling's approximation
    stirling = math.sqrt(2 * math.pi * n) * (n / math.e)**n
    # Optional correction term for higher accuracy
    stirling *= 1 + 1/(12*n)
    return stirling
