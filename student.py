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

       def Check_conflict(self,crn):
          Value1="""SELECT * FROM COURSE WHERE CRN=?"""
          self.cursor.execute(Value1,(crn,))
          Add_Course=self.cursor.fetchall()
          for C_info in Add_Course:
            S_DAY=C_info[2]
            E_DAY=C_info[3]
            S_TIME=C_info[4]
            E_TIME=C_info[5]

          Value=""" SELECT * FROM SCHEDULE WHERE ID=?"""  
          self.cursor.execute(Value,(self.ID,))
          Check_list=self.cursor.fetchall()
          Check_List_S_DAY=[]
          Check_List_E_DAY=[]
          Check_List_S_TIME=[]
          Check_List_E_TIME=[]
         
          for element in Check_list:
            Check_List_S_DAY.append(element[4])
            Check_List_E_DAY.append(element[5])
            Check_List_S_TIME.append(element[6])
            Check_List_E_TIME.append(element[7])
          
          if S_DAY not in  Check_List_S_DAY:
            if E_DAY not in Check_List_E_DAY:
               if S_TIME not in Check_List_S_TIME:
                if E_TIME not in Check_List_E_TIME:
                  return True
          else:
            return False

             
         
         

       def Add_Course(self,crn):
          Value="""SELECT * FROM  COURSE WHERE CRN=?"""
          self.cursor.execute(Value,(crn,))
          Schedule=self.cursor.fetchall()
          if self.Check_conflict(crn):
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
          else:
            return "There is a time conflict "

            

           
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