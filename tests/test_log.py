import math
import sys, os
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from mymath.log import ln
vals = [i/10 for i in range(1, 101)] 
math_vals = [math.log(x) for x in vals]
my_vals = [ln(x) for x in vals]
plt.figure(figsize=(12,6))
plt.plot(vals, math_vals, label='math.log', color='blue')
plt.plot(vals, my_vals, label='mymath.ln', color='red', linestyle='--')
plt.title("Сравнение math.log и mymath.ln")
plt.xlabel("x")
plt.ylabel("ln(x)")
plt.legend()
plt.grid(True)
plt.savefig("log_comparison.png", dpi=300)
plt.show()
