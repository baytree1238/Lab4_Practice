"""
Q1
This program asks the user to enter a number.
After entering number, the program ask the user which operation they want to apply to the number.
program should print the result of applying the operation to the number entered.
If the user does not enter a valid operator then the program print the message
"Operator not supported"
"""
import math

number = float(input("Enter a number: "))
operation = (input("Enter an operation: "))

if operation == "exp":
    result = round(math.exp(number),2)
    print(f"{operation}({number}) = {result}")
elif operation == "log":
    result = round(math.log(number),2)
    print(f"{operation}({number}) = {result}")
elif operation == "log10":
    result = round(math.log10(number), 2)
    print(f"{operation}({number}) = {result}")
elif operation == "sqrt":
    result = round(math.sqrt(number),2)
    print(f"{operation}({number}) = {result}")
else:
    print("Operator not supported.")


"""
Q2
This program asks the user to enter the name of a month and prints out
the number of days in that month.
if input is not recognized month name, then the program should show the message "Invalid month."
"""
month = input("Enter the month: ")

if month in ("Janurary" or "March" or "May" or "July" or "August" or "October" or "December"):
    days = 31
    print(f"{month} has {days} days.")
elif month == "February":
    days = 28
    print(f"{month} has {days} days.")
elif month in ("April" or "June" or "September" or "November"):
    days = 30
    print(f"{month} has {days} days.")
else:
    print("Invalid month.")
