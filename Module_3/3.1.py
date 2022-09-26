"""
Exercise 3.1: Implement a simple mathematical function
Implement the mathematical function
g(t)=e^sin(pi*t)
in a Python function g(t). Print out g.0/ and g.1/.
"""
import math
def g(t):
    return math.e ** -t * math.sin(math.pi*t)
print(g(0)); print(g(1))
