"""Exercise 5.12: Plot exact and inexact Fahrenheit-Celsius conversion formulas"""

import numpy as np
import matplotlib.pyplot as plt

inexactFtoC = lambda F: (F-30)/2
exactFtoC = lambda F: (F-32)*5/9

F = np.linspace(-20,120,1000)

plt.plot(F,inexactFtoC(F), label="Inexact")
plt.plot(F,exactFtoC(F), label="Exact")
# plt.plot(F,inexactFtoC(F)-exactFtoC(F), label="Difference")

plt.xlabel("Fahrenheit")
plt.ylabel("Celsius")
plt.legend()
plt.show()