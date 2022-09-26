"""Example use:
Enter a conversion type (C2F, F2C, C2K, K2C, F2K, K2F, or type exit to quit): k2f
Enter a value: 0 
-459.67
Enter a conversion type (C2F, F2C, C2K, K2C, F2K, K2F, or type exit to quit): C2f
Enter a value: 30
86.0
"""
def C2F(C):
    return (C * 9/5) + 32
def F2C(F):
    return (F - 32) * 5/9
def C2K(C):
    return C + 273.15
def K2C(K):
    return K - 273.15
def F2K(F):
    return (F + 459.67) * 5/9
def K2F(K):
    return K * 9/5 - 459.67
