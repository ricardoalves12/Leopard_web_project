import sqlite3
import random
class User:
    
    def __init__(self,F_mame,L_name,Id,status):
      self.first_name=F_mame
      self.last_name=L_name
      self.ID=Id
      self.status=status
      
    
    def Connect(self):
         
        self.connect=sqlite3.connect("Documents/LeoRepo/Leopard_web_project/Database/tables.db")
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
             S_day=row[2]
             E_day=row[3]
             S_time=row[4]
             E_time=row[5]
             T_name=row[6]
             
           print (f"CRN: {CRN} \n Course name: {Course_name}\n Course day : {S_day}-{E_day}\n Course time: {S_time}-{E_time}\n Teacher: {T_name}")
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
    