import firebase_admin
from firebase_admin import credentials, firestore
from PIL import Image, ImageFont, ImageDraw, ImageOps

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
        print()
        print("-------------")
        print("Card Designer")
        print("-------------")
        empId = getEmpId()
        continueLoop = True
        while continueLoop:
            continueLoop = businessCardMenu(empId)
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

    if not empExists(empId):
        print("No employee with that ID!")
        return False
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

def businessCardMenu(empId):

    if not empExists(empId):
        print("No employee with that ID!")
        return False

    # need to put this info into the databse, bc it resets every loop
    borderSize = 0.05
    #color = "darkblue"
    color = "navy"
    font = "arial.ttf"

    print("Change a setting, or print the business card:")
    print("(B) Border size: " + str(borderSize))
    print("(C) Color: " + color)
    print("(F) Font: " + font)
    print("(P) Print")
    print("(E) Exit")
    userInput = input().lower()

    if userInput == "b":
        pass
    elif userInput == "c":
        color = changeColorMenu()
    elif userInput == "f":
        pass
    elif userInput == "p":
        printCard(empId, borderSize, color, font)
    elif userInput == "e":
        return False

    return True

def changeColorMenu():

    print()
    print("Select the main color:")
    print("(B) Black")
    print("(L) Blue")
    print("(R) Red")
    userInput = input().lower()

    if userInput == "b":
        return "black"
    elif userInput == "l":
        return "#00044d"
    elif userInput == "R":
        return "#450000"
    else:
        return "black"

################################################################
# BusinessCard Functions #
################################################################

def printCard(empId, borderSize, color, font):

    doc = rootRef.document(empId).get()
    name = doc.get("name")
    occupation = doc.get("occupation")
    phoneNum = doc.get("phoneNum")
    email = doc.get("email")
    firstLetter = name[0]

    str1 = "REACT"
    image = Image.new("RGBA", (600,400), "white")
    draw = ImageDraw.Draw(image)
    fontName = ImageFont.truetype(font, 35)
    fontOccupation = ImageFont.truetype(font, 15)
    fontPhoneNum = ImageFont.truetype(font, 15) 
    fontEmail = ImageFont.truetype(font, 15)
    fontFirstLetter = ImageFont.truetype("Garamond.ttf", 300)

    w,h = fontName.getsize(name)
    # the line below the occupation should change according to length of name, not length of occupation;
    # that's why I'm initializing a separate width and heigth here for "line"
    lineW, lineH = fontName.getsize(name)
    draw.multiline_text(((800-w)/2, (380-h)/2), name, font = fontName, fill = color, align = "center")

    w,h = fontOccupation.getsize(occupation)
    draw.multiline_text(((800-w)/2, (450-h)/2), occupation, font = fontOccupation, fill = color, align = "center")
    # this next line is extremely obtuse, but all it's doing is drawing a line with the right length and position
    draw.line([((800-lineW)/2 - lineW/8, (530-lineH)/2), ((800-lineW)/2 + 9 * lineW/8, (530-lineH)/2)], fill = color, width = 2, joint = "curve")

    w,h = fontPhoneNum.getsize(phoneNum)
    draw.multiline_text(((800-w)/2, (650-h)/2), phoneNum, font = fontPhoneNum, fill = color, align = "center")

    w,h = fontFirstLetter.getsize(firstLetter)
    draw.multiline_text(((300-w)/2, (340-h)/2), firstLetter, font = fontFirstLetter, fill = color, align = "center")



    image = ImageOps.expand(image, border = 15, fill = color)




    image.show()

    return

################################################################
# Add to/Remove from Employee Database #
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

    docs = rootRef.stream()

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
