import sqlite3
import random
class User:
    
    def __init__(self,F_mame,L_name,Id,status):
      self.first_name=F_mame
      self.last_name=L_name
      self.ID=Id
      self.status=status
      
    
    def Connect(self):
         
        self.connect=sqlite3.connect("Leopard_web_project/Database/tables.db")
        self.cursor=self.connect.cursor()
    
    def Disconnect(self):
       if self.connect:
        self.cursor.close()
    
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
           print (f"CRN: {CRN} \n Course name: {Course_name}\n Course day : {Course_day}\n Course time: {Course_time}\n Teacher: {Instructor_name}")
          else:
            print("Course doesn't exist ")
    def implement(self):
        Value="""INSERT INTO AUTHENTIFY(USER_ID,STATUS,FIRST_NAME,LAST_NAME,USER_NAME) VALUES (?,?,?,?,?)"""
        User_name= self.last_name + self.first_name[0]
        Values=(self.ID,self.status,self.first_name,self.last_name,User_name)
        self.cursor.execute(Value,Values)
        self.connect.commit()

    def print_all_course(self):
      self.cursor.execute("SELECT * FROM COURSE ")
      result=self.cursor.fetchall()
      for row in result:
        print(row)
    