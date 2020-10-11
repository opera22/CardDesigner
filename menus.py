from miscellaneous import *
from businesscard import *
import time

def mainMenu():

    print("Select an option:")
    print("(A) Add an employee")
    print("(R) Remove an employee")
    print("(V) View all employees")
    print("(E) Exit")
    userInput = input("").lower()

    if userInput == "a":
        addEmployeeMenu()
    elif userInput == "r":
        removeEmployee(getEmpId())
    elif userInput == "v":
        printEmployees()
    elif userInput == "e":
        return False

    # if true, the menu will pop back up again 
    return True

def addEmployeeMenu():

    empId = ""
    name = ""
    occupation = ""
    phoneNum = ""
    print("\nOkay, you'll need to enter some information...")
    time.sleep(2)
    


    return