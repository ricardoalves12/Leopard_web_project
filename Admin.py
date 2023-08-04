import sqlite3
import random
from user import User


class Admin(User):
    def __init__(self,first_name,last_name,ID):
       super().__init__(self,first_name,last_name,ID)
       
    
    def Connect(self):
             self.connect=sqlite3.connect("Leopard_web_project/Database/tables.db")
             self.cursor=self.connect.cursor()
    
    
    def Disconnect(self):
          if self.connect:
            self.cursor.close()



    def Add_Course(self,id,C_Name,S_day,E_day,S_time,E_time,T_name):
      self.connect=sqlite3.connect("Database/tables.db")
      self.cursor=self.connect.cursor()
      Value ="""INSERT INTO COURSE(CRN,C_NAME,S_DAY,E_DAY,S_TIME,E_TIME,T_NAME) VALUES(?,?,?,?,?,?,?)"""
      Values=(id,C_Name,S_day,E_day,S_time,E_time,T_name)
      self.cursor.execute(Value,Values)
      self.connect.commit()
      self.connect.close()
      return True
    
    def Add(self,id,C_Name,C_day,C_time,Instructor,):
      Value ="""INSERT INTO COURSE(CRN,COURSE_NAME,COURSE_DAY,COURSE_TIME,INSTRUCTOR_NAME) VALUES(?,?,?,?,?)"""
      Values=(id,C_Name,C_day,C_time,Instructor)
      self.cursor.execute(Value,Values)
      self.connect.commit()

    def Remove(self,CRN):
      Value ="""DELETE FROM COURSE WHERE CRN=?"""
      Values=(CRN,)
      
      self.cursor.execute(Value,Values)
      self.connect.commit()





