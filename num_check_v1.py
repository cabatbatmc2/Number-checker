#3/02/35: Number Checker V1
from easygui import *

def main_program():
    number = float(enterbox("Enter a number"))
    
    if number > 0:
        msgbox(f"{number} is a positive number")

    elif number < 0:
        msgbox(f"{number} is a negative number")

    else:
        msgbox(f"{number} is zero")

while True:
    main_program()
    repeat = buttonbox("Would you like to check another number?", choices = ["Yes", "No"])

    if repeat != "Yes":
        msgbox("Thank you for using Number Checker V1! See you next time.")
        break
