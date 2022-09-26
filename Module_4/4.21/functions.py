import math

def f(t, T):
    if 0 < t < T/2:
        return 1
    elif t == T/2:
        return 0
    elif T/2 < t < T:
        return -1

def S(t, n, T):
    sum = 0
    for i in range(1, n+1):
        sum += (1/(2*i-1))*math.sin(2*(2*i-1)*math.pi*t/T)
    sum = sum * 4/math.pi
    return sum
