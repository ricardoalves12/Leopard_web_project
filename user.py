import sqlite3
import random
class User:
    
    def __init__(self, f_name, l_name, user_id):
        self.first_name = f_name
        self.last_name = l_name
        self.ID = user_id
          
    def setUserInfo(self,F_name,L_name, Id):
        self.first_name= F_name
        self.last_name= L_name
        self.ID= Id

    def printInfo(self):
        return f"User Name: {self.first_name}, {self.last_name}\n ID: {self.ID}"


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
             S_day=row[2]
             E_day=row[3]
             S_time=row[4]
             E_time=row[5]
             T_name=row[6]
             self.connect.close()
           return(f"CRN: {CRN} \n Course name: {Course_name}\n Course day : {S_day}-{E_day}\n Course time: {S_time}-{E_time}\n Teacher: {T_name}")
          else:
            self.connect.close()
            return False  
    
  
    
   
       