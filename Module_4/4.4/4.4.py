"""
Exercise 4.4: Read and write several numbers from and to file
This is a variant of Exercise 4.3 where we have several Fahrenheit degrees in a file
and want to read all of them into a list and convert the numbers to Celsius degrees.
Thereafter, we want to write out a file with two columns, the left with the Fahrenheit
degrees and the right with the Celsius degrees.
"""


def C(F):
    return 5/9 * (F - 32)
def F(C):
    return 9/5 * C + 32

import os
print(os.getcwd())
temptxtfile = open("Documents/Programmering/INF120-Programmering-og-databehandling/Problems/Module 4/4.4/TEMPDATAMULTIPLE.txt", "r")
# Here whomever runs this code will have to adjust the path to the file, as this is excluisive to my machine.
lines = temptxtfile.readlines()
temptxtfile.close()
farenheitDegreeString = lines[3:]
farenheitValues = []
for i in farenheitDegreeString:
    individualLines = i.split()
    farenheitValues.append(individualLines[2])
print(farenheitValues)

with open("Documents/Programmering/INF120-Programmering-og-databehandling/Problems/Module 4/4.4/celsius_farenheit_table.txt", "w") as convertedFile:
    convertedFile.write("Temperature data for farenheit and celcius \n----------------")
    convertedFile.write("\nfarenheit : celsius \n")
    for i in farenheitValues:
        convertedFile.write(f"\n{i} : {round(C(float(i)),2)}")
