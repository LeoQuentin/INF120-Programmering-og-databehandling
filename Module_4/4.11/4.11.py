"""Exercise 4.11: Use exceptions to handle wrong input
The program from Exercise 4.10 reads input from the command line. Extend that
program with exception handling such that missing command-line arguments are
detected. In the except IndexError block, use the raw_input function to ask 
the user for missing input data.
(I use input() instelad of raw_input() because I'm using Python 3)
"""

import sys
g = 9.81
try: 
    t = float(sys.argv[1])
    v0 = float(sys.argv[2])
except IndexError:
    t = float(input("t = "))
    v0 = float(input("v0 = "))
y = v0*t - 0.5*g*t**2
print(y)



