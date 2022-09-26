"""Exercise 5.7: Demonstrate array slicing"""

import numpy as np

w = np.linspace(0,3,31)
print(w)

print(w[:]) # same as print(w[0:31])
print(w[:-2]) # same as print(w[0:29])
print(w[::5]) # same as print(w[0:31:5])
print(w[2:-2:6]) # same as print(w[2:29:6]) 