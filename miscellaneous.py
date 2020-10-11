from main import rootRef

def printEmployees():
    print("sup brotha")
    return

def removeEmployee(id):

    rootRef.document(id).delete()
    print("Employee #" + str(id) + " was removed.")
    return

def getEmpId(): 

    id = ""
    while len(id) != 6:
        id = input("Please enter the employee's 6-digit ID number: ")

    return id

def empExists(id):

    if rootRef.document(id).get().exists:
        return True
    else:
        return False
