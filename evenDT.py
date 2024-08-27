import sympy as sp
import numpy as np

t = sp.symbols('t')
u = sp.Heaviside
y = t*u(t) + 3*u(t-4)
equation = sp.Piecewise((t, t < 0), (3, t >= 4), (0, True))
even = (equation + equation.subs(t, -t)) / 2
# sp.plot(t, equation, even, (t, -20, 20))
# print(even)
n = 100
func = sp.lambdify(t, even, 'numpy')

# Define a range of values for t
t_values = np.linspace(-20, 20, n)

# Evaluate the even function at these points
even_values = func(t_values)

# Select the values within the desired range
selected = even_values[(t_values >= -3) & (t_values <= 0)]

# Sum the selected values
sig = np.sum(selected)
print(sig)