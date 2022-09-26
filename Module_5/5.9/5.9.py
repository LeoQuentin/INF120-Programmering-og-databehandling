"""Exercise 5.9: Plot a formula"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

v0 = 10
g = 9.81

t = np.linspace(0,2*v0/g,100)
f_func = lambda t: v0*t - 0.5*g*t**2

plt.xlabel("time (s)")
plt.ylabel("height (m)")


lines = plt.plot(t,f_func(t))

plt.show()
