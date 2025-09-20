'''
Realization of natural logarithm using Taylor series around 1
Input: x > 0
'''

def ln(x: float, n_terms: int = 20) -> float:
    if x <= 0:
        raise ValueError("ln(x) is defined for x > 0")
    
    y = (x - 1) / (x + 1)
    result = 0.0
    for n in range(n_terms):
        term = (1 / (2 * n + 1)) * (y ** (2 * n + 1))
        result += term
    return 2 * result
