"""Exercise 5.4: Plot a function
Make a plot of the function in Exercise 5.1 for x in [-4,4].
"""
import numpy as np
import matplotlib.pyplot as plt

n = 200
xlist = np.linspace(-4,4,n)
hlist = 1/(np.sqrt(2*np.pi))*np.exp(-1/2*xlist**2)
plt.plot(xlist, hlist)
plt.show()
