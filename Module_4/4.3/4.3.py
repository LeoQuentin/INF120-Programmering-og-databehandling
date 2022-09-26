"""Exercise 4.3: Read a number from a file
Modify the program from Exercise 4.1 such that the Fahrenheit temperature is read
from a file with the following content:
(content in TEMPDATA.txt)
"""

def C(F):
    return 5/9 * (F - 32)
def F(C):
    return 9/5 * C + 32

import os
print(os.getcwd())
temptxtfile = open("Documents/Programmering/INF120-Programmering-og-databehandling/Problems/Module 4/4.3/TEMPDATA.txt", "r")
# Here whomever runs this code will have to adjust the path to the file, as this is excluisive to my machine. 
lines = temptxtfile.readlines()
farenheitDegreeString = lines[3]
farenheitDegreeList = farenheitDegreeString.split()
farenheitDegree = float(farenheitDegreeList[2])
temptxtfile.close()

print(f"{farenheitDegree} degrees farenheit is {round(C(farenheitDegree),2)} degrees celcius")
