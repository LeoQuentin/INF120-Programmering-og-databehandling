"""Exercise 4.9: Prompt the user for input to a formula
Consider the simplest program for evaluating the formula y(t)=v0t−0.5gt^2:
----------------------------------------
v0 = 3; g = 9.81; t = 0.6
y = v0*t - 0.5*g*t**2
print y
----------------------------------------
Modify this code so that the program asks the user questions t=? and v0=?, and 
then gets t and v0 from the user’s input through the keyboard. 
"""

t = float(input("t=? "))
v0 = float(input("v0=? "))
g = 9.81

y = v0*t - 0.5*g*t**2
print(y)