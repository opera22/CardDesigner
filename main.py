import firebase_admin
from firebase_admin import credentials, firestore

from PIL import Image, ImageFont, ImageDraw

from businesscard import *
from menus import *
from misc import *


def main():

    try:
        app = firebase_admin.get_app()
    except ValueError as e:
        cred = credentials.Certificate('serviceAccountKey.json')
        firebase_admin.initialize_app(cred)


    db = firestore.client()
    rootRef = db.collection("employees")

    print("--------------------------------------")
    print("Welcome to the Business Card Designer!")
    print("--------------------------------------")

    continueLoop = True
    while continueLoop:
        continueLoop = mainMenu()

    print("Goodbye for now!")



    #####################
    """id = ""
    while len(id) != 6:
        id = input("Please enter the employee's 6-digit ID number: ")


    rootRef.document("tom").set({ "name": "timothy" })
    rootRef.document("tom").delete()




    userRef = rootRef.document(id)

    userDoc = userRef.get()
    if not userDoc.exists:
        print("made it in")


    #db.collection("employees").document(id)




    printCard(0) """

    return

main()