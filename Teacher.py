import sqlite3
import random
from user import User
class Teacher(User):
         def __init__(self):
             super().__init__()            
         
         def Connect(self):
             self.connect=sqlite3.connect("Leopard_web_project/Database/tables.db")
             self.cursor=self.connect.cursor()
        
         def Disconnect(self):
             if self.connect:
                self.cursor.close()
          
         def implement(self):
            
            Update="""INSERT INTO INSTRUCTOR VALUES(?,?,?,?,?,?,?)"""
            Values=(self.id,self.first_name,self.last_name,self.title,self.hire,self.department,self.Email)
            self.cursor.execute(Update,Values)
            self.connect.commit()
        
         def Print_Class_List(self,crn, instructorName):
            self.connect=sqlite3.connect("Database/tables.db")
            self.cursor=self.connect.cursor()
            Fetch=""" SELECT ROSTER FROM COURSE WHERE INSTRUCTOR_NAME=? AND CRN=? """
            Value=(instructorName,crn)
            self.cursor.execute(Fetch,(Value),)
            result=self.cursor.fetchone()
            if result:
                print(result[0])
            else:
                print(f"{instructorName} is not teaching this course ")
            
            self.cursor.close()