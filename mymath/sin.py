# sine realization with usage of Taylor series

'''
input should be the float in grad
example: x = 50°
and by using Taylor series formila the sin of x will be calculated 
more in README.md file
'''

from mymath.utils import PI, checking

def sin(x: float) -> float:
    x = checking(x)
    return ( x - ((x**3)/6) + ((x**5)/120) - ((x**7)/5040) + ((x**9)/362880)) # Taylor series formula for sin
