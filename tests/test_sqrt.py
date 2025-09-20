import math
import sys, os
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from mymath.sqrt import sqrt 
vals = [1 + i/100 for i in range(-99, 100)] 
math_vals = [math.sqrt(x) for x in vals]
my_vals = [sqrt(x, n_terms=20) for x in vals]
plt.figure(figsize=(12,6))
plt.plot(vals, math_vals, label='math.sqrt', color='blue')
plt.plot(vals, my_vals, label='mymath.sqrt', color='red', linestyle='--')
plt.title("Сравнение math.sqrt и mymath.sqrt (Taylor)")
plt.xlabel("x")
plt.ylabel("sqrt(x)")
plt.legend()
plt.grid(True)
plt.savefig("sqrt_comparison.png", dpi=300)
plt.show()
