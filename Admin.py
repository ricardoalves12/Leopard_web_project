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
    
    def Add(self,id,C_Name,S_day,E_day,S_time,E_time,T_name):
      Value ="""INSERT INTO COURSE(CRN,C_NAME,S_DAY,E_DAY,S_TIME,E_TIME,T_NAME) VALUES(?,?,?,?,?,?,?)"""
      Values=(id,C_Name,S_day,E_day,S_time,E_time,T_name)
      self.cursor.execute(Value,Values)
      self.connect.commit()
      return True

    
    
    def Add_Teacher(self,T_name,T_last_name,T_title,T_hyear,T_department):
      ID=random.randint(2007,3000)
      New_user=User(T_name,T_last_name,ID,"TEACHER")
      New_user.Connect()
      New_user.implement()
      New_user.Disconnect()
      New_Teacher=Teacher(T_name,T_last_name,ID,T_department,"TEACHER",T_title,T_hyear)
      New_Teacher.Connect()
      New_Teacher.implement()
      New_Teacher.Disconnect()
    
  
    def Add_student(self,S_name,S_last_name,S_Gradyear, S_Major):
      ID=random.randint(10012,20000)
      New_user=User(S_name,S_last_name,ID,"STUDENT")
      New_user.Connect()
      New_user.implement()
      New_user.Disconnect()
      New_Student=Student(S_name,S_last_name,ID,S_Major,S_Gradyear,"STUDENT")
      New_Student.Connect()
      New_Student.implement()
      New_Student.Disconnect()

    def unlink_link_T(self,CRN,new_T):
      Value="""UPDATE COURSE SET INSTRUCTOR_NAME=? WHERE CRN=? """
      self.cursor.execute(Value,(new_T,CRN))
      self.connect.commit()
    
    def unlink_S(self,CRN,student_n):
       Value="""SELECT ROSTER FROM COURSE WHERE CRN=?""" 
       self.cursor.execute(Value,(CRN,))
       List=self.cursor.fetchone()
       if List :
        New_list=List[0] .split('\n') 
        New_list.remove(student_n)
        for element in New_list:
          print(element)
        Old_list='\n'.join(New_list)
        Val="""UPDATE COURSE SET ROSTER WHERE CRN=?"""
        self.cursor.execute(Val,(Old_list,))
       else:
          print("Can't happen")
    def Course_info(self,CRN):
        Value="""SELECT * FROM COURSE WHERE CRN=?"""
        self.cursor.execute(Value,(CRN,))
        ELement=self.cursor.fetchall()
        for element in ELement:
          C_name=element[1]
          C_day=element[2]
          C_time=element[3]
          C_instructor=element[4]
        return f"[{C_name}|{C_day}|{C_time}|{C_instructor}]"
    def Remove_from_schedule(self,student_n,CRN):
       Val="""SELECT SCHEDULE FROM STUDENT WHERE NAME=?"""
       self.cursor.execute(Val,(student_n,))
       Old_schedule=self.cursor.fetchone()
       New_scheduled=Old_schedule[0].split(']|')
       New_scheduled.remove(self.Course_info(CRN))
       for element in New_scheduled:
        print(element)




         
       
    def Remove(self,CRN):
      Value ="""DELETE FROM COURSE WHERE CRN=?"""
      Values=(CRN,)
      
      
      self.cursor.execute(Value,Values)
      self.connect.commit()
      return True

