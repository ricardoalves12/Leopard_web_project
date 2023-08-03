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
          
         def print_T_schedule(self):
            Fetch="""SELECT * FROM COURSE WHERE T_NAME=?"""
            self.cursor.execute(Fetch,(self.first_name,))
            Schedule=self.cursor.fetchall()
            new_array=[]
            for element in Schedule:
                CRN=element[0]
                C_NAME=element[1]
                S_DAY=element[2]
                E_DAY=element[3]
                S_TIME=element[4]
                E_TIME=element[5]
                new_array.append(f"{CRN}|{C_NAME}|{S_DAY}|{E_DAY}|{S_TIME}|{E_TIME}")
            String_array='\n'.join(new_array)
            return String_array
           
        
         
         def print_S_list(self):
            Fetch=""" SELECT ST_NAME FROM SCHEDULE WHERE T_NAME=? """
            self.cursor.execute(Fetch,(self.first_name,))
            result=self.cursor.fetchone()
            for element in result:
                print(element)

