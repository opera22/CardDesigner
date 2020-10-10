from misc import *
from businesscard import *

def mainMenu():

    print("Select an option:")
    print("(A) Add an employee")
    print("(R) Remove an employee")
    print("(V) View all employees")
    print("(E) Exit")
    userInput = input("").lower()

    if userInput == "a":
        pass
    elif userInput == "r":
        pass
    elif userInput == "v":
        printEmployees()
    elif userInput == "e":
        return False

    # if true, the menu will pop back up again 
    return True