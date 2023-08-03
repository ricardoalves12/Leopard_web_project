import sqlite3
import random
from user import User
from Teacher import Teacher
from student import Student

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
             self.connect=sqlite3.connect("Documents/LeoRepo/Leopard_web_project/Database/tables.db")
             self.cursor=self.connect.cursor()
    
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
    def Disconnect(self):
          if self.connect:
            self.cursor.close()
    
    def Add_Course(self,id,C_Name,S_day,E_day,S_time,E_time,T_name):
      Value ="""INSERT INTO COURSE(CRN,C_NAME,S_DAY,E_DAY,S_TIME,E_TIME,T_NAME) VALUES(?,?,?,?,?,?,?)"""
      Values=(id,C_Name,S_day,E_day,S_time,E_time,T_name)
      self.cursor.execute(Value,Values)
      self.connect.commit()
      return True

    
    
    def Add_Teacher(self,T_name,T_last_name,T_title,T_hyear,T_department):
      ID=random.randint(2007,3000)
      Email=T_name + T_last_name[0]+ "@wit.edu"
      user_name=T_last_name+T_name[0]
      Value="""INSERT INTO INSTRUCTOR VALUES(?,?,?,?,?,?,?)"""
      Val=(ID,T_name,T_last_name,T_title,T_hyear,T_department,Email)
      self.cursor.execute(Value,(Val))
      self.connect.commit()
      Value1="""INSERT INTO AUTHENTIFY(USER_ID,STATUS,FIRST_NAME,LAST_NAME,USER_NAME) VALUES (?,?,?,?,?)"""
      Val1=(ID,"TEACHER",T_name,T_last_name,user_name)
      self.cursor.execute(Value1,(Val1))
      self.connect.commit()
      

      
    
  
    def Add_student(self,S_name,S_last_name,S_Gradyear, S_Major):
      ID=random.randint(10012,20000)
      Email=S_name+S_last_name[0]+"@wit.edu"
      username=S_last_name+S_name[0]
      Value="""INSERT INTO STUDENT(ID,NAME,SURNAME,GRADYEAR,MAJOR,EMAIL) VALUES(?,?,?,?,?,?)"""
      Val=(ID,S_name,S_last_name,S_Gradyear,S_Major,Email)
      self.cursor.execute(Value,(Val))
      self.connect.commit()
      Value1="""INSERT INTO AUTHENTIFY(USER_ID,STATUS,FIRST_NAME,LAST_NAME,USER_NAME) VALUES (?,?,?,?,?)"""
      Val1=(ID,"STUDENT",S_name,S_last_name,username)
      self.cursor.execute(Value1,(Val1))
      self.connect.commit()

    def unlink_link_T(self,CRN,new_T):
      Value="""UPDATE COURSE SET T_NAME=? WHERE CRN=? """
      self.cursor.execute(Value,(new_T,CRN))
      self.connect.commit()
      Value1="""UPDATE SCHEDULE SET T_NAME=? WHERE CRN=? """
      self.cursor.execute(Value1(new_T,CRN,))
    
    def unlink_S(self,CRN,ID):
      Value="""DELETE FROM SCHEDULE WHERE ID=? AND CRN=?"""
      self.cursor.execute(Value,(CRN,ID,))
      self.connect.commit()
    


         
       
    def Remove_Course(self,CRN):
      Value ="""DELETE FROM COURSE WHERE CRN=?"""
      Values=(CRN,)
      
      
      self.cursor.execute(Value,Values)
      self.connect.commit()
      return True

