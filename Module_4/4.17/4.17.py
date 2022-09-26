"""Exercise 4.17: Look up calendar functionality
The purpose of this exercise is to make a program that takes a date, consisting of
year (4 digits), month (2 digits), and day (1 to 31) on the command line and prints the
corresponding name of the weekday (Monday, Tuesday, etc.). Python has a module
calendar, which makes it easy to solve the exercise, but the task is to find out how
to use this module.
"""


import calendar
from datetime import date
yyyymmdd = input("Enter a date (YYYYMMDD): ")
year = int(yyyymmdd[:4])
month = int(yyyymmdd[4:6])
day = int(yyyymmdd[6:])

print(calendar.day_name[date(year, month, day).weekday()])