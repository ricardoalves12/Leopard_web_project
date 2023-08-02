import sqlite3
import random
class User:
    
    def __init__(self):
        self.first_name = " "
        self.last_name = " "
        self.ID = 0
          
    def setUserInfo(self,F_name,L_name, Id):
        self.first_name= F_name
        self.last_name= L_name
        self.ID= Id

    def printInfo(self):
        return f"User Name: {self.first_name}, {self.last_name}\nID: {self.ID}"


    def CheckLoginCredentials(self, username, password):
         DbConnect = sqlite3.connect("Database/tables.db")
         db= DbConnect.cursor()         
         db.execute("SELECT 1 FROM AUTHENTIFY  WHERE USER_NAME = ? and PASSWORD = ? ", (username, password))
         result = db.fetchone()
         if result:
             return True
         else:
             return False

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
             self.connect.close()
           return(f"Course name: {Course_name}\n Course day : {Course_day}\n Course Name: {Course_name}\n Course time: {Course_time}\n Teacher: {Instructor_name}")
          else:
            self.connect.close()
            return("Course doesn't exist ")  
    
  
    
   
       