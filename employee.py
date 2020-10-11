from menus import *
from main import rootRef
from businesscard import *

class Employee:   

    def Employee(self, empId, name, occupation, phoneNum, email):

        if not empExists(empId):

            rootRef.document(empId).set({

                "name" : name,
                "occupation" : occupation,
                "phoneNum" : phoneNum,
                "email" : email

            })
        else:
            print("\nAn employee with that ID already exists!\n")

        return


