import firebase_admin
from firebase_admin import credentials, firestore

from PIL import Image, ImageFont, ImageDraw
from printCard import *

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
rootRef = db.collection("employees")

#####################
id = ""



rootRef.document("tom").set({ "name": "timothy" })
rootRef.document("tom").delete()


while len(id) != 6:
    id = input("Please enter the employee's 6-digit ID number: ")

userRef = rootRef.document(id)

userDoc = userRef.get()
if not userDoc.exists:
    print("made it in")


#db.collection("employees").document(id)




printCard(0)