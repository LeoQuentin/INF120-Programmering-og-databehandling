"""Exercise 5.6: Simulate by hand a vectorized expression"""
import numpy as np

x = np.array([0,2])
t = np.array([1,1.5])

yforloop = np.zeros(len(x))
for i in range(len(x)):
    yforloop[i] = np.cos(np.sin(x[i]))+np.exp(1/t[i])
print(yforloop)

y = np.cos(np.sin(x))+np.exp(1/t)
print(y)