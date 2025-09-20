from mymath.sin import sin
from mymath.cos import cos

def tan(x: float) -> float:
    c = cos(x)
    if abs(c) < 1e-10:
        raise ValueError(f"tan({x}°) is undefined (cos(x)≈0)")
    return sin(x) / c
