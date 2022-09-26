"""
Exercise 3.4: Write a Fahrenheit-Celsius conversion functions
The formula for converting Fahrenheit degrees to Celsius reads
C = 5/9 * (F - 32)
Write a function C(F) that implements this formula. Also write the inverse function
F(C) for going from Celsius to Fahrenheit degrees. How can you test that the two
functions work?
Hint C(F(c)) should result in c and F(C(f)) should result in f.
"""
def C(F):
    return 5/9 * (F - 32)
def F(C):
    return 9/5 * C + 32

print(C(F(100)))
print(F(C(100)))
