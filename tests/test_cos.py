import math
import sys, os
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from mymath.cos import cos
vals = [i for i in range(0, 361)]
math_vals = [math.cos(math.radians(x)) for x in vals]
my_vals = [cos(x) for x in vals]
plt.figure(figsize=(12,6))

plt.plot(vals, math_vals, label='math.cos', color='blue')
plt.plot(vals, my_vals, label='mymath.cos', color='red', linestyle='--')

plt.title("Сравнение math.cos и mymath.cos")
plt.xlabel("Градусы")
plt.ylabel("cos(x)")
plt.legend()
plt.grid(True)
plt.savefig("cos_comparison.png", dpi=300)
plt.show()
