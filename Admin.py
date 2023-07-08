
from Class_Create import Class_Creator

class Admin:
    def __init__(self,Name):
      self.name=Name

    def Add(self,Category,database_name):
      Database=Class_Creator(database_name)
      
      if Category=="STUDENT":
        ID=int(input(" Enter the student ID: "))
        NAME=input(" Enter the student name: ")
        SURNAME=input(" Enter the student surname: ")
        GRADYEAR=int(input(" Enter the student gradution year:"))
        MAJOR= input(" Enter the student major: ")
        EMAIL= input(" Enter the student email: ")

        

    
    def modify(self):
        print(f'You can now modify the system ')






