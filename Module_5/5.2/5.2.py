"""Exercise 5.2: Fill arrays; loop version
The aim is to fill two arrays x and y with x and h.x/ values, respectively, where
h(x) is defined in (5.20). Let the x values be as in Exercise 5.1. Create empty x and
y arrays and compute each element in x and y with a for loop.

note : I don't know where to find (5.20). Therefore, I will instead use the function from 5.1.
"""
import numpy as np
x = np.zeros(41)
y = np.zeros(41)
distancebetweenpoints = 4/40

for i in range(0,41):
    x[i] = i*distancebetweenpoints
    y[i] = 1/(np.sqrt(2*np.pi))*np.exp(-1/2*x[i]**2)
print(x)
print(y)