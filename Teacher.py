import sqlite3
import random
from user import User
class Teacher(User):
         def __init__(self,first_name,last_name,id,Departemt,status,title,hire_year):
             super().__init__(first_name,last_name,id,status)
             self.department=Departemt
             self.Email= self.first_name + self.last_name[0] + " @wit.edu"
             self.title= title
             self.hire=hire_year
             self.id=id
             self.cursor=None
             self.connect=None
         
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

print(" Hello new user ")
Name=input("Can you please enter your first name: ")
Name2=input("Can you please enter your last name: ")
id = random.randint(1000,3000)
status=input("Please enter your status at the school :")
New_User=User(Name,Name2,id,"INSTRUCTOR")
New_User.Connect()
#New_User.implement()

if New_User.status=="INSTRUCTOR":
     Department=input(" Please enter your major: ")
     hire_year=input(" when do you expect to gradute: ")
     hire=int(hire_year)
     Title=input("What is your position: ")
     New_Teacher=Teacher(Name,Name2,id,Department,status,Title,hire)
     New_Teacher.Connect()
     New_Teacher.print(35)
     New_Teacher.Disconnect()