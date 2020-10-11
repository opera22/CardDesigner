from main import rootRef

def printEmployees():
    print("sup brotha")
    return

def removeEmployee(empId):
    if empExists(empId):
        rootRef.document(empId).delete()
        print("\nEmployee #" + str(empId) + " was removed.\n")
    else:
        print("\nNo employee with that ID!\n")
    return

def getEmpId(): 

    empId = ""
    while len(empId) != 6:
        empId = input("\nPlease enter the employee's 6-digit ID number: ")

    return empId

def empExists(empId):

    if rootRef.document(empId).get().exists:
        return True
    else:
        return False
