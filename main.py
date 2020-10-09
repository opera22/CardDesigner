import firebase_admin
from firebase_admin import credentials, firestore

from PIL import Image, ImageFont, ImageDraw

cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()





username = input("Please enter your username: ")


ref = db.collection('users').document(username)

ref.set({

    "name":"",
    "lname":"",
    "age": 0

})

ref.update({"name":input("Enter your actual name: ")})


print("hi")