import math
import sys, os
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from mymath.tan import tan

vals = [i for i in range(0, 361) if i % 180 != 90]
math_vals = [math.tan(math.radians(x)) for x in vals]
my_vals = [tan(x) for x in vals]
plt.figure(figsize=(12,6))

plt.plot(vals, math_vals, label='math.tan', color='blue')
plt.plot(vals, my_vals, label='mymath.tan', color='red', linestyle='--')

plt.title("Сравнение math.tan и mymath.tan")
plt.xlabel("Градусы")
plt.ylabel("tan(x)")
plt.legend()
plt.grid(True)

plt.savefig("tan_comparison.png", dpi=300)
plt.show()
