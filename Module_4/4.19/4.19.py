"""Exercise 4.19: Why we test for specific exception types
The simplest way of writing a try-except block is to test for any exception, for
example,
try:
    C = float(sys.arg[1])
except:
    print ’C must be provided as command-line argument’
    sys.exit(1)
Write the above statements in a program and test the program. What is the problem?
The fact that a user can forget to supply a command-line argument when running
the program was the original reason for using a try block. Find out what kind of
exception that is relevant for this error and test for this specific exception and re-run
the program. What is the problem now? Correct the program.
"""

import sys
try:
    C = float(sys.argv[1])
except IndexError:
    print("C must be provided as command-line argument")
    sys.exit(1)
except ValueError:
    print("C must be a number")
    sys.exit(1)

# The issue is that the user can supply a string, list or other non-float as a\
# command-line argument, which will cause a ValueError.