"""
Exercise 4.1: Make an interactive program
Make a program that asks the user for a temperature in Fahrenheit degrees and reads
the number; computes the corresponding temperature in Celsius degrees; and prints
out the temperature in the Celsius scale.
"""
def C(F):
    return 5/9 * (F - 32)
def F(C):
    return 9/5 * C + 32

farenheit = float(input("Enter the farenheit value: "))
print(f"{farenheit} degrees farenheit is {round(C(farenheit),2)} degrees celcius")
"""
farenheit_or_celcius = input("Do you want to convert from farenheit or celcius? Type farenheit or celcius: ")
if farenheit_or_celcius == "farenheit":
    farenheit = float(input("Enter the farenheit value: "))
    print(f"{farenheit} degrees farenheit is {round(C(farenheit),2)} degrees celcius")
elif farenheit_or_celcius == "celcius":
    celcius = float(input("Enter the celcius value: "))
    print(f"{celcius} degrees celcius is {round(F(celcius),2)} degrees farenheit")
else:
    print("Invalid input")"""