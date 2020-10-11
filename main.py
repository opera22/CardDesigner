import firebase_admin
from firebase_admin import credentials, firestore

from PIL import Image, ImageFont, ImageDraw

from businesscard import *
from menus import *
from miscellaneous import *


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

    return


main()