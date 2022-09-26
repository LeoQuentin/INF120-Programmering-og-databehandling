"""Exercise 4.20: Make a complete module
a) Make six conversion functions between temperatures in Celsius, Kelvin, and
Fahrenheit: C2F, F2C, C2K, K2C, F2K, and K2F.

b) Collect these functions in a module convert_temp.

c) Import the module in an interactive Python shell and demonstrate some sample
calls on temperature conversions.

d) Insert the session from c) in a triple quoted string at the top of the module file as
a doc string for demonstrating the usage.

e) Write a function test_conversion() that verifies the implementation. Call
this function from the test block if the first command-line argument is verify
"""
from convert_temp import *
# c)
def run_c_program(): 
    input_conversiontype = input("Enter a conversion type (C2F, F2C, C2K, K2C, F2K, K2F, or type exit to quit): ").upper()
    if input_conversiontype == "C2F" or "F2C" or "C2K" or "K2C" or "F2K" or "K2F":
        input_value = float(input("Enter a value: "))
        if input_conversiontype == "C2F":
            print(C2F(input_value))
        elif input_conversiontype == "F2C":
            print(F2C(input_value))
        elif input_conversiontype == "C2K":
            print(C2K(input_value))
        elif input_conversiontype == "K2C":
            print(K2C(input_value))
        elif input_conversiontype == "F2K":
            print(F2K(input_value))
        elif input_conversiontype == "K2F":
            print(K2F(input_value))
        elif input_conversiontype == "exit":
            programStillRuns = False

# d)
def test_conversion():
    """Test the conversion functions."""
    tol = 1E-12
    assert 32 - tol < C2F(0) < 32 + tol
    assert 0 - tol < F2C(32) < 0 + tol
    assert 273.15 - tol < C2K(0) < 273.15 + tol
    assert 0 - tol < K2C(273.15) < 0.0 + tol
    assert 273.15 - tol < F2K(32) < 273.15 + tol
    assert 32.0 - tol < K2F(273.15) < 32.0 + tol
    print("All tests passed")
    run_e_program()

# e)
def run_e_program():
    input_temperature = float(input("Enter a temperature: "))
    input_temperature_unit = input("Enter a temperature unit (C, F, or K): ").upper()
    if input_temperature_unit == "C":
        farenheit = (C2F(input_temperature))
        kelvin = (C2K(input_temperature))
        print(f"{round(input_temperature,4)}°C is {round(farenheit,4)}°F and {round(kelvin,4)}°K")
    if input_temperature_unit == "F":
        celsius = (F2C(input_temperature))
        kelvin = (F2K(input_temperature))
        print(f"{round(input_temperature,4)}°F is {round(celsius,4)}°C and {round(kelvin,4)}°K")
    if input_temperature_unit == "K":
        celsius = (K2C(input_temperature))
        farenheit = (K2F(input_temperature))
        print(f"{round(input_temperature,4)}°K is {round(celsius,4)}°C and {round(farenheit,4)}°F")


import sys
try:
    if sys.argv[1] == "verify":
        test_conversion()
except IndexError:
    print("No arguments given at startup, running program")