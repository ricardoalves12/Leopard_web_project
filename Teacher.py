import sqlite3
import random
from user import User
class Teacher(User):
         def __init__(self):
             super().__init__(first_name,last_name,id,status)
         
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
         def search_Course(self,crn):
            self.connect=sqlite3.connect("Database/tables.db")
            self.cursor=self.connect.cursor()
        
            Fetch="""SELECT * FROM COURSE WHERE CRN =? """
            course_crn=crn
            self.cursor.execute(Fetch,(course_crn,))
            result= self.cursor.fetchall()
            if result:
              for row in result:
                CRN=row[0]
                Course_name=row[1]
                Course_day=row[2]
                Course_time=row[3]
                Instructor_name=row[4]
                print(f"Course name: {Course_name}\n Course day : {Course_day}\n Course time: {Course_time}\n Teacher: {Instructor_name}")
            else:
                print("Course doesn't exist ")
            
         def print(self,crn):
            Fetch=""" SELECT 1 FROM COURSE WHERE INSTRUCTOR_NAME=? AND CRN=? """
            Value=(self.first_name,crn)
            self.cursor.execute(Fetch,(Value),)
            result=self.cursor.fetchone()
            if result:
                print(result[0])
            else:
                print(f"{self.first_name} is not teaching this course ")

