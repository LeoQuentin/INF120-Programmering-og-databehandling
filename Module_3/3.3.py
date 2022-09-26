"""
Exercise 3.3: Explain how a program works
Explain how the following program works:
def add(A, B):
    C = A + B
    return C

a = 3
b = 2
print add(a, b)
print add(2*a, b+1)*3

Figure out what is being printed without running the program.
"""

# In this program, nothing will be printed. Running the program will result in a syntax error.
# This is because the print function will not work without parenthesis directly after.
# The correct way to write this program is:
"""
def add(A, B):
    C = A + B
    return C

a = 3
b = 2
print(add(a, b))
print(add(2*a, b+1)*3)
"""