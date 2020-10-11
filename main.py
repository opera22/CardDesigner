import firebase_admin
from firebase_admin import credentials, firestore
from PIL import Image, ImageFont, ImageDraw

try:
    app = firebase_admin.get_app()
except ValueError as e:
    cred = credentials.Certificate('serviceAccountKey.json')
    firebase_admin.initialize_app(cred)

db = firestore.client()
rootRef = db.collection("employees")

################################################################
# Main Code -- Main Menu Loop, etc. #
################################################################
def main():   

    print("--------------------------------------")
    print("Welcome to the Business Card Designer!")
    print("--------------------------------------")

    continueLoop = True
    while continueLoop:
        continueLoop = mainMenu()

    print("\n~ Goodbye for now! ~\n")

    return

################################################################
# MENUS #
################################################################

def mainMenu():

    print("Select an option:")
    print("(A) Add an employee")
    print("(R) Remove an employee")
    print("(V) View all employees")
    print("(M) Modify an existing employee")
    print("(B) Business card designer")
    print("(E) Exit")
    userInput = input("").lower()

    if userInput == "a":
        addEmployeeMenu()
    elif userInput == "r":
        removeEmployee(getEmpId())
    elif userInput == "v":
        printEmployees()
    elif userInput == "m":
        print()
        print("------------------")
        print("Update an Employee")
        print("------------------")
        empId = getEmpId()
        continueLoop = True
        while continueLoop:
            continueLoop = modifyEmployeeMenu(empId)
    elif userInput == "b":
        businessCardMenu()
    elif userInput == "e":
        return False

    # if true, the menu will pop back up again 
    return True

def addEmployeeMenu():

    print("\nOkay, you'll need to enter some information...")
    empId = getEmpId()
    name = input("Now enter his/her full name: ")
    occupation = input("Now enter his/her occupation: ")
    phoneNum = input("Now enter his/her phone number in the format 123-456-7890: ")
    email = input("Lastly, enter his/her email in the format johnsmith@gmail.com: ")

    addEmployeeToDB(empId, name, occupation, phoneNum, email)
    
    return

def modifyEmployeeMenu(empId):

    doc = rootRef.document(empId).get()
    print("\n" + doc.get("name") + "\'s profile")
    print("-----------------------")
    printEmployee(empId)
    print("Select an option:")
    print("(N) Update name")
    print("(O) Update occupation")
    print("(P) Update phone number")
    print("(M) Update email")
    print("(E) Exit")

    userInput = input("").lower()

    if userInput == "n":
        rootRef.document(empId).update({"name": input("Enter the new name: ")})
    elif userInput == "o":
        rootRef.document(empId).update({"occupation": input("Enter the new occupcation: ")})
    elif userInput == "p":
        rootRef.document(empId).update({"phoneNum": input("Enter the new phone number: ")})
    elif userInput == "m":
        rootRef.document(empId).update({"email": input("Enter the new email: ")})
    elif userInput == "e":
        return False
    return True




def businessCardMenu():

    return

################################################################
# BusinessCard Class #
################################################################

class BusinessCard:

    def printCard(self, empId):

        print(str(empId))

        return

################################################################
# Modify Employee Database #
################################################################

def addEmployeeToDB(empId, name, occupation, phoneNum, email):

        if not empExists(empId):

            rootRef.document(empId).set({

                "name" : name,
                "occupation" : occupation,
                "phoneNum" : phoneNum,
                "email" : email

            })
            print("\n" + name + " was added to the database!\n")
        else:
            print("\nAn employee with that ID already exists!\n")

        return

def removeEmployee(empId):
    if empExists(empId):
        rootRef.document(empId).delete()
        print("\nEmployee #" + str(empId) + " was removed.\n")
    else:
        print("\nNo employee with that ID!\n")
    return

################################################################
# Miscellaneous Functions #
################################################################

def printEmployees():

    print()
    print("-----------------")
    print("List of Employees")
    print("-----------------")

    docs = db.collection("employees").stream()

    for doc in docs:
        print(doc.get("name"))
        print("ID: " + doc.id)
        print("Occupation: " + doc.get("occupation"))
        print("Phone Number: " + doc.get("phoneNum"))
        print("Email: " + doc.get("email"))
        print()

    return

def printEmployee(empId):

    doc = rootRef.document(empId).get()

    print(doc.get("name"))
    print("ID: " + doc.id)
    print("Occupation: " + doc.get("occupation"))
    print("Phone Number: " + doc.get("phoneNum"))
    print("Email: " + doc.get("email"))
    print()

    return

def getEmpId(): 

    empId = ""
    while len(empId) != 6:
        empId = input("Please enter the employee's 6-digit ID number: ")

    return empId

def empExists(empId):

    if rootRef.document(empId).get().exists:
        return True
    else:
        return False

main()
