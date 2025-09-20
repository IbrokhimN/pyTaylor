# exp realization with usage of Taylor series
# Ik that i could do just e**x but i try to realize almost everything with taylor series


def exp(x: float) -> float:
    """
    Calculate e^x using Taylor series approximation.
    
    Parameters:
        x (float): exponent
        
    Returns:
        float: approximate value of e^x
    """
    return ( 1 + x + ((x**2)/2) + ((x**3)/6) + ((x**4)/24) ) # Taylor series formula for exp
