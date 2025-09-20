# Taylor-Math: Mathematical Functions via Taylor Series

## Overview
**Taylor-Math** is a Python package that implements common mathematical functions using **Taylor series** and other classical approximations. The goal is to study and visualize the behavior of mathematical functions through series expansions, rather than relying on built-in functions.

This package includes:
- `sin(x)` – Sine function using Taylor series.
- `cos(x)` – Cosine function using Taylor series.
- `tan(x)` – Tangent function using Taylor series.
- `exp(x)` – Exponential function using Taylor series.
- `log(x)` – Natural logarithm using Taylor series.
- `sqrt(x)` – Square root function using series approximation.
- `factorial(n)` – Factorial using **Stirling's approximation**.
- `constants.py` – Common mathematical constants.
- `utils.py` – Utility functions such as argument normalization.

---

## Formulas Used

### 1. Sine
\[
\sin(x) \approx x - \frac{x^3}{3!} + \frac{x^5}{5!} - \frac{x^7}{7!} + \frac{x^9}{9!}
\]

### 2. Cosine
\[
\cos(x) \approx 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \frac{x^6}{6!} + \frac{x^8}{8!}
\]

### 3. Tangent
\[
\tan(x) \approx x + \frac{1}{3}x^3 + \frac{2}{15}x^5 + \frac{17}{315}x^7
\]

### 4. Exponential
\[
e^x \approx 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!}
\]

### 5. Natural Logarithm (ln)
\[
\ln(1+x) \approx x - \frac{x^2}{2} + \frac{x^3}{3} - \frac{x^4}{4} + \dots
\]

### 6. Square Root
\[
\sqrt{1+x} \approx 1 + \frac{x}{2} - \frac{x^2}{8} + \frac{x^3}{16} - \frac{5x^4}{128} + \dots
\]

### 7. Factorial (Stirling's Approximation)
\[
n! \approx \sqrt{2 \pi n} \left(\frac{n}{e}\right)^n \left( 1 + \frac{1}{12n} \right)
\]

---

## Example Usage

```python
from mymath.sin import sin
from mymath.cos import cos
from mymath.factorial import factorial

print(sin(30))       # sine in degrees
print(cos(60))       # cosine in degrees
print(factorial(10)) # approximate factorial
````

You can also visualize the functions and compare them with Python's `math` library using `matplotlib` examples in the `examples/` folder.

---

## License

This project is licensed under the **MIT License**.

---

## Notes

* Input angles are in **degrees** and normalized internally to radians.
* For factorials, Stirling's formula provides fast approximation, especially useful for large numbers.
* This project is intended for educational and research purposes.

