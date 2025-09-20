from math import factorial

def sqrt(x: float, n_terms: int = 10) -> float:
    """
Calculates sqrt(x) using the Taylor expansion around a=1.
n_terms is the number of terms in the series.
    """
    if x <= 0:
        raise ValueError("x must be positive")
    y = x - 1
    result = 0
    for n in range(n_terms):
        coeff = 1
        for k in range(n):
            coeff *= (0.5 - k)
        coeff /= factorial(n)
        result += coeff * (y ** n)
    return result
