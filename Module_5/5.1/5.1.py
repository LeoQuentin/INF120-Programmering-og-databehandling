"""Exercise 5.1: Fill lists with function values
Define: h(x)=1/(sqrt(2*pi)*e^(-1/2*x^2))))"""
import numpy as np

n = 41
xlist = np.linspace(0,4,n)
hlist = 1/(np.sqrt(2*np.pi))*np.exp(-1/2*xlist**2)
print(hlist)
print(xlist)
