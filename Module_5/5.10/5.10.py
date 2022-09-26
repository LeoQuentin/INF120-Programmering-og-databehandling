"""Exercise 5.10: Plot a formula for several parameters"""

import numpy as np
import matplotlib.pyplot as plt
import sys

if len(sys.argv) > 1:
    v0_values = np.zeros(len(sys.argv)-1)
    for i in range(1,len(sys.argv)):
        v0_values[i-1]=(sys.argv[i])
else:
    input_v0 = input("Enter v0 values separated by space: ")
    v0_values = np.array(input_v0.split(), dtype=float)

g = 9.81
for i in range(len(v0_values)):
    v0 = v0_values[i]
    t = np.linspace(0,2*v0/g,100)
    f_func = lambda t: v0*t - 0.5*g*t**2
    plt.plot(t,f_func(t), label=f"v0 = {v0}")
plt.legend()
plt.show()

