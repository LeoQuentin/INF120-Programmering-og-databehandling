"""Exercise 4.7: Read input from the command line
a) Let a program store the result of applying the eval function to the first
command-line argument. Print out the resulting object and its type.
b) Run the program with different input: an integer, a real number, a list, and
a tuple
c) Try the string "this is a string" as a command-line argument. Why does
this string cause problems and what is the remedy?

This program should be run from the command line, as it is not possible to input a string from the command line in the python shell.
"""
import sys

input_from_terminal = sys.argv[1]
evaluated_input = eval(input_from_terminal)
print(evaluated_input, type(evaluated_input))

""" c) The eval() function takes a string and converts it into the appropriate data-type.
Doing this with a string defeats the purpose. If we wanted a program which could handle a string,
We would have to build some sort of exception handler that checks whether the input is a string or not."""