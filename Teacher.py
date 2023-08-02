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
        
        
         
         def print_S_list(self):
            Fetch=""" SELECT ST_NAME FROM SCHEDULE WHERE T_NAME=? """
            self.cursor.execute(Fetch,(self.first_name,))
            result=self.cursor.fetchone()
            for element in result:
                print(element)

