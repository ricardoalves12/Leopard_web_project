from user import User 
import sqlite3
import random 
class Student(User):
       def __init__(self,first_name,last_name,id,major,grad_year,status):
          super().__init__(first_name,last_name,id,status)
          
          
          self.Major=major
          self.graduate=grad_year
          self.Email= self.first_name + self.last_name[0] + " @wit.edu"
          self.schedule={}
          self.cursor=None
          self.connect=None
     
       def Connect(self):
          self.connect=sqlite3.connect("Documents/LeoRepo/Leopard_web_project/Database/tables.db")
          self.cursor=self.connect.cursor()
        
       def Disconnect(self):
          if self.connect:
            self.cursor.close()
       def implement(self):
            
            Update="""INSERT INTO STUDENT VALUES(?,?,?,?,?,?)"""
            Values=(self.ID,self.first_name,self.last_name,self.graduate,self.Major,self.Email)
            self.cursor.execute(Update,Values)
            self.connect.commit()
            

            

       def Add_Course(self,crn):
          Value="""SELECT * FROM  COURSE WHERE CRN=?"""
          self.cursor.execute(Value,(crn,))
          Schedule=self.cursor.fetchall()
          for element in Schedule:
            CRN=element[0]
            C_NAME=element[1]
            S_DAY=element[2]
            E_DAY=element[3]
            S_TIME=element[4]
            E_TIME=element[5]
            T_NAME=element[6]
          Value="""INSERT INTO SCHEDULE(ID,ST_NAME,CRN,COURSE,S_DAY,E_DAY,S_TIME,E_TIME,T_NAME) VALUES(?,?,?,?,?,?,?,?,?)"""  
          Val=(self.ID,self.first_name,CRN,C_NAME,S_DAY,E_DAY,S_TIME,E_TIME,T_NAME)
          self.cursor.execute(Value,(Val))
          self.connect.commit()

            

           
       def Remove(self,Course_number):
         
         Remove="""DELETE FROM SCHEDULE WHERE CRN=? AND ID=? """
         Val=(Course_number,self.ID)
         self.cursor.execute(Remove,(Val))
         self.connect.commit()
       
       def display_schedule(self):
        Fetch="""SELECT * FROM SCHEDULE WHERE ID=?"""
        self.cursor.execute(Fetch,(self.ID,))
        Schedule=self.cursor.fetchall()
        for element in Schedule:
          CRN=element[2]
          C_NAME=element[3]
          S_DAY=element[4]
          E_DAY=element[5]
          S_TIME=element[6]
          E_TIME=element[7]  
          print(f"{CRN}|{C_NAME}|{S_DAY}|{E_DAY}|{S_TIME}|{E_TIME}")