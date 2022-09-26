"""Exercise 4.10: Read parameters in a formula from the command line
Modify the program listed in Exercise 4.9 such that v0 and t are read from the
command line.
"""

import sys
t = float(sys.argv[1])
v0 = float(sys.argv[2])
g = 9.81

y = v0*t - 0.5*g*t**2
print(y)