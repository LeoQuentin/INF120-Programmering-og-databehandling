"""
Exercise 3.2: Implement a simple mathematical function with a parameter
Let us extend the function g.t / in Exercise 3.1 to:
h(t) = e^(-at) * sin(pi*t)
where a is a parameter. How can the corresponding Python function be imple-
mented in this case? Print out h(0) and h(1) for the case a a = 10.
"""
import math
def h(t, a):
    return math.e ** (-a*t) * math.sin(math.pi*t)
print(h(0, 10)); print(h(1, 10))