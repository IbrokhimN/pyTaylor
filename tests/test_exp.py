import math
import sys, os
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from mymath.exp import exp
vals = [i for i in range(-5, 6)]  
math_vals = [math.exp(x) for x in vals]
my_vals = [exp(x) for x in vals]
plt.figure(figsize=(12,6))

plt.plot(vals, math_vals, label='math.exp', color='blue')
plt.plot(vals, my_vals, label='mymath.exp', color='red', linestyle='--')

plt.title("Сравнение math.exp и mymath.exp")
plt.xlabel("x")
plt.ylabel("exp(x)")
plt.legend()
plt.grid(True)

plt.savefig("exp_comparison.png", dpi=300)
plt.show()
