"""Exercise 4.12: Test validity of input data
Test if the t value read in the program from Exercise 4.10 lies between 0 and 2(v0)=g.
If not, print a message and abort the execution.
"""

import sys
g = 9.81

try: 
    t = float(sys.argv[1])
    v0 = float(sys.argv[2])
except IndexError:
    t = float(input("t = "))
    v0 = float(input("v0 = "))
if t > 2*v0/g or t < 0:
    print(f"t must be between 0 and 2*v0/g, the latter with these values would equate to {round(2*v0/g,3)}")
    sys.exit()
else: 
    y = v0*t - 0.5*g*t**2
    print(y)
