"""
Exercise 4.2: Read a number from the command line
Modify the program from Exercise 4.1 such that the Fahrenheit temperature is read
from the command line.
This program should be run from the command line, not from the Python shell.
"""

import sys

def C(F):
    return 5/9 * (F - 32)
def F(C):
    return 9/5 * C + 32

farenheit = float(sys.argv[1])

print(f"{farenheit} degrees farenheit is {round(C(farenheit),2)} degrees celcius")
