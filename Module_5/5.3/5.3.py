"""Exercise 5.3: Fill arrays; vectorized version
Vectorize the code in Exercise 5.2 by creating the x values using the linspace
function from the numpy package and by evaluating h(x) for an array argument.
Filename: fill_arrays_vectorized.
"""
import numpy as np

# Note, this is the same code as in 5.1. As previously stated, I don't know where to find (5.20).
n = 41
xlist = np.linspace(0,4,n)
hlist = 1/(np.sqrt(2*np.pi))*np.exp(-1/2*xlist**2)
print(hlist)
print(xlist)
