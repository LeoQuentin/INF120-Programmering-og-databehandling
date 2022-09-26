"""Exercise 4.14: Evaluate a formula for data in a file
We consider the formula y(t)=v0*t - 0.5g*t^2 and want to evaluate y for a range of
t values found in a file (timedata.txt)
More precisely, the first two lines are always present, while the next lines contain
an arbitrary number of t values on each line, separated by one or more spaces.

a) 
Write a function that reads the input file and returns v0 and a list with the t
values. (A sample file is ball.dat7)

b) 
Make a test function that generates an input file, calls the function in a) for
reading the file, and checks that the returned data objects are correct.

c) 
Write a function that creates a file with two nicely formatted columns containing
the t values to the left and the corresponding y values to the right. Let the t
values appear in increasing order (note that the input file does not necessarily
have the t values sorted)
"""
import random
from tabulate import tabulate
g = 9.81

def dataPointSeperator(filename):
    """Function that takes a filename as input and returns a list of all the data points. 
    Main function of the program"""
    datapointsv0 = []
    global v0
    with open(f"Documents/Programmering/INF120-Programmering-og-databehandling/Problems/Module 4/4.14/{filename}", "r") as f:
        lines = f.readlines()
        lineWithv=lines[0]
        v0 = (float(lineWithv.split()[1]))
        linesWithData = lines[2:]
        for lines in linesWithData:
            for points in lines.split():
                datapointsv0.append(float(points))
        return(datapointsv0)

all_t_values = dataPointSeperator("timedata.txt")

def test_dataPointGeneratorAndTester():
    """Test function that generates an arbitrary amount of random points and writes them to both a list
    and a txt file and then tests against the dataPointSeperator function, with
    data from this function as input in the dataPointSeperator function"""
    with open("Documents/Programmering/INF120-Programmering-og-databehandling/Problems/Module 4/4.14/testdatafile.txt", "w") as f:
        f.write("v0: 3.5\nt:\n")
        randomDataPoints = [round(random.random(),4) for i in range(1000)]
        for i in randomDataPoints:
            rantint = random.randint(0,15)
            if rantint == 0:
                f.write(f"{i}\n")
            else:
                f.write(f"{i} ")
    assert randomDataPoints == dataPointSeperator("testdatafile.txt")
    return(randomDataPoints)

test_dataPointGeneratorAndTester()

def yCalculator(t_values):
    y_values = []
    t_values.sort()
    for t in t_values:
        y_value = v0*t - 0.5*g*t**2
        y_values.append(y_value)
    return(y_values)

def tableGenerator(t_values, y_values):
    table = []
    t_values.sort()
    for i in range(len(t_values)):
        table.append([t_values[i], y_values[i]])
    return(tabulate(table, headers=["t", "y"],tablefmt="fancy_grid"))

tableGenerator(all_t_values, yCalculator(all_t_values))
def tableFileWriter():
    with open("Documents/Programmering/INF120-Programmering-og-databehandling/Problems/Module 4/4.14/outputdata.txt", "w") as f:
        f.write(tableGenerator(all_t_values, yCalculator(all_t_values)))
tableFileWriter()
