from user import User 
import numpy as np
import sqlite3
import random 
class Student(User):
       def __init__(self,first_name,last_name,ID):
          super().__init__(first_name,last_name,ID)  
          
     
       def Add_Course(self,crn):
          self.connect=sqlite3.connect("Database/tables.db")
          self.cursor=self.connect.cursor()
          Value="""SELECT * FROM  COURSE WHERE CRN=?"""
          self.cursor.execute(Value,(crn,))
          Schedule=self.cursor.fetchall()
          if Schedule != []:
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
             self.connect.close()
          else:
              return False
          
       def Remove(self,Course_number):
             self.connect=sqlite3.connect("Database/tables.db")
             self.cursor=self.connect.cursor()
             self.cursor.execute("SELECT 1 FROM SCHEDULE WHERE CRN =? AND ID =? ", (Course_number, self.ID))
             crn_exist = self.cursor.fetchone()
             Remove="""DELETE FROM SCHEDULE WHERE CRN=? AND ID=? """
             Val=(Course_number,self.ID)
             if crn_exist:
                self.cursor.execute(Remove,(Val))
                self.connect.commit()
                self.connect.close()
             else:
                 return False

       def display_schedule(self):
            self.connect=sqlite3.connect("Database/tables.db")
            self.cursor=self.connect.cursor()
            Fetch="""SELECT * FROM SCHEDULE WHERE ID=?"""
            self.cursor.execute(Fetch,(self.ID,))
            Schedule=self.cursor.fetchall()
            courses = np.array([])
            for element in Schedule:
              CRN=element[2]
              C_NAME=element[3]
              S_DAY=element[4]
              E_DAY=element[5]
              S_TIME=element[6]
              E_TIME=element[7]  
              courses = np.append(courses,(f"{CRN}|{C_NAME}|{S_DAY}-{E_DAY}|{S_TIME}-{E_TIME}"))
            self.connect.close()
            return courses
            
         
  
         

      



         
        
        



