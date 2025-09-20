import math
import sys, os
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from mymath.sin import sin

vals = [i for i in range(0, 361)]
math_vals = [math.sin(math.radians(x)) for x in vals]
my_vals = [sin(x) for x in vals]
plt.figure(figsize=(12,6))

plt.plot(vals, math_vals, label='math.sin', color='blue')
plt.plot(vals, my_vals, label='mymath.sin', color='red', linestyle='--')

plt.title("Сравнение math.sin и mymath.sin")
plt.xlabel("Градусы")
plt.ylabel("sin(x)")
plt.legend()
plt.grid(True)
plt.savefig("sin_comparison.png", dpi=300)
plt.show()
