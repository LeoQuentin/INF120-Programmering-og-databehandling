"""Exercise 4.16: Compute the distance it takes to stop a car
...
"""


import sys
g = 9.81
kmh = "km/h"
mps = "m/s"


try:
    v0 = sys.argv[1]
    u = sys.argv[2]
except IndexError:
    print("Please provide two arguments")
    v0 = input("v0 = ")
    u = input("u = ")

if type(v0) != float or int:
    try:
        v0 = eval(v0)
    except:
        if "km/h" in v0:
            v0 = eval(v0.replace("km/h",""))/3.6
        elif "m/s" in v0:
            v0 = eval(v0.replace("m/s",""))
        else:
            raise TypeError("Please provide a valid unit for v0")
try:
    u = eval(u)
except:
    raise TypeError("Please provide a valid unit for u")

def d(v0, u):
    return ((1/2)*((v0**2)/(u*g)))
print(f"distanse = {round(d(v0, u),4)}")