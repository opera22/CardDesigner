from menus import *
from businesscard import *

def getEmpId(): 
 
    id = ""
    while len(id) != 6:
        id = input("Please enter the employee's 6-digit ID number: ")

    return id


"""
        empRef = rootRef.document(id)
        empDoc = empRef.get()

        if not empDoc.exists:
            print("This user does not exist!")
            if input("Would you like to return to the main menu (Y/N)? ").lower() == "y":
                return "-1"
        else:
            return id
"""

def createEmp():


    pass

    return

def printEmployees():

    pass

    return

def doesEmpExist(id):

    if not rootRef.document(id).get().exists:
        return False
    else:
        return True


