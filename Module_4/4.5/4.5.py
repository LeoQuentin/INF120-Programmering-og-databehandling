"""Exercise 4.5: Use exceptions to handle wrong input
Extend the program from Exercise 4.2 with a try-except block to handle the
potential error that the Fahrenheit temperature is missing on the command line.
"""

import sys

def C(F):
    return 5/9 * (F - 32)
def F(C):
    return 9/5 * C + 32

try:
    farenheit = float(sys.argv[1])
    print(f"{farenheit} degrees farenheit is {round(C(farenheit),2)} degrees celcius")
except IndexError:
    print("Please provide a temperature in farenheit")
    
