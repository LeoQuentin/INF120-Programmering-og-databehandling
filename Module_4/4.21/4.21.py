"""Exercise 4.21: Organize a previous program as a module
Collect the f and S functions in the program from Exercise 3.21 in a sep-
arate file such that this file becomes a module. Put the statements making
the table (i.e., the main program from Exercise 3.21) in a separate function
table(n_values, alpha_values, T). Make a test block in the module to
read T and a series of n and a values as positional command-line arguments and
make a corresponding call to table.
"""
import sys
from functions import *
from tabulate import tabulate
n_values = [1, 3, 5, 10, 30, 100]
alpha_values = [0.01, 0.25, 0.49]
T = math.pi * 2

def table(n_values, alpha_values, T):
    table = []
    for n in n_values:
        for alpha in alpha_values:
            table.append([n, alpha, f(alpha*T, T) - S(alpha*T, n, T)])
    return(tabulate(table, headers=["n", "alpha", "f(t, T) - S(t, n, T)"]))

def test_table():
    try:
        n_values = eval(sys.argv[1])
        alpha_values = eval(sys.argv[2])
        T = eval(sys.argv[3])
        print(table(n_values, alpha_values, T))
    except IndexError:
        print("Please enter n_values, alpha_values and T as positional command-line arguments")
        sys.exit(1)
    except:
        print("Something went wrong")

# test_table()
print(table(n_values, alpha_values, T))
