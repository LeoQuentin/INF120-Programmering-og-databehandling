"""Exercise 4.13: Raise an exception in case of wrong input
Instead of printing an error message and aborting the program explicitly, raise
a ValueError exception in the if test on legal t values in the program from Exer-
cise 4.12. Notify the user about the legal interval for t in the exception message.
"""

import sys
g = 9.81

try: 
    v0 = float(sys.argv[1])
    t = float(sys.argv[2])
except IndexError:
    v0 = float(input("v0 = "))
    t = float(input("t = "))

if t<0 or t>(2*v0/g):
    raise ValueError(f"t must be between 0 and 2*v0/g, the latter with these values would equate to {round(2*v0/g,5)}")
    sys.exit(1)
y = v0*t - 0.5*g*t**2
print(y)