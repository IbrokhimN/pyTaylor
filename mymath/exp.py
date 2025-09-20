# exp realization with usage of Taylor series
# Ik that i could do just e**x but i try to realize almost everything with taylor series

def exp(x, terms=20):
    result = 0
    factorial = 1
    power = 1
    for n in range(terms):
        if n > 0:
            factorial *= n
            power *= x
        result += power / factorial
    return result
