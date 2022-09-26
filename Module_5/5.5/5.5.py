"""Exercise 5.5: Apply a function to a vector
Given a vector v = (2, 3, -1) and a function f(x) = x^3 + xe^x + 1, apply f to
each element in v. Then calculate by hand f(v) as the NumPy expression v**3 +
v*exp(v) + 1 using vector computing rules. Demonstrate that the two results are
equal."""
import numpy as np

v = np.array([2,3,-1])
f = lambda x: x**3 + x*np.exp(x) + 1
print(f(v))

v1 = (2**3 + 2*np.exp(2) + 1)
v2 = (3**3 + 3*np.exp(3) + 1)
v3 = (-1**3 + -1*np.exp(-1) + 1)

v_secondary = np.array([v1,v2,v3])
print(v_secondary)

equal_or_not = np.array_equal(f(v), v_secondary)
print(equal_or_not)