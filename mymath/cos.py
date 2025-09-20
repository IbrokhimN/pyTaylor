# cosine realization with usage of Taylor series

'''
input should be the float in grad
example: x = 50°
and by using Taylor series formula the cos of x will be calculated 
more in README.md file
'''

from mymath.utils import PI, checking

def cos(x: float) -> float:
    x = checking(x)
    return ( 1 - ((x**2)/2) + ((x**4)/24) - ((x**6)/720) +((x**8)/40320) ) # Taylor series formula for cos

