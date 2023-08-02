import sqlite3
import random
from user import User


class Admin(User):
    def __init__(self,first_name,last_name,id,status,title,office):
       super().__init__(first_name,last_name,id,status)
       
       self.Email= self.first_name + self.last_name[0] + " @wit.edu"
       self.title= title
       self.office=office
       self.id=id
       self.cursor=None
       self.connect=None
    
    def Connect(self):
             self.connect=sqlite3.connect("Leopard_web_project/Database/tables.db")
             self.cursor=self.connect.cursor()
    
    
    def Disconnect(self):
          if self.connect:
            self.cursor.close()
    
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





