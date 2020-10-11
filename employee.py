from menus import *
from main import rootRef
from businesscard import *

class Employee:   

    def Employee(self, id, name, occupation, phoneNum, email):

        if not empExists(id):

            rootRef.document(id).set({

                "name" : name,
                "occupation" : occupation,
                "phoneNum" : phoneNum,
                "email" : email

            })
        else:
            print("An employee with that ID already exists!")

        return


