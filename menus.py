from miscellaneous import *
from businesscard import *
from employee import Employee
from time import sleep

def mainMenu():

    print("Select an option:")
    print("(A) Add an employee")
    print("(R) Remove an employee")
    print("(V) View all employees")
    print("(M) Modify an existing employee")
    print("(E) Exit")
    userInput = input("").lower()

    if userInput == "a":
        addEmployeeMenu()
    elif userInput == "r":
        removeEmployee(getEmpId())
    elif userInput == "v":
        printEmployees()
    elif userInput == "m":
        modifyEmployeeMenu()
    elif userInput == "e":
        return False

    # if true, the menu will pop back up again 
    return True

def addEmployeeMenu():

    empId = ""
    name = ""
    occupation = ""
    phoneNum = ""
    email = ""

    print("\nOkay, you'll need to enter some information...")
    time.sleep(2)
    empId = getEmpId()
    occupation = input("Now enter his/her occupation title: ")
    phoneNum = input("Now enter his/her phone number in the format 123-456-7890: ")
    email = input("Lastly, enter his/her email in the format johnsmith@gmail.com: ")

    myEmployee = Employee(empId, name, occupation, phoneNum, email)
    
    return

def modifyEmployeeMenu():

    return