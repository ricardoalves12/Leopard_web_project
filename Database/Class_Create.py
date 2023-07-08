import sqlite3
class Class_Creator:
   def  __init__(self,name):
       self.db_name=name
       self.cursor=None
       self.connect=None
    
   def Connect(self):
    self.connect = sqlite3.connect(self.db_name)
    self.cursor= self.connect.cursor()

   def Disconnect(self):
    if self.connect:
        self.cursor.close()
  
   def Create(self):
     self.cursor.execute(""" CREATE TABLE AUTHENTIFY(
        PASSWORD TEXT  NOT NULL,
         USERNAME TEXT NOT NULL,
         USER_ID INTERGER NOT NULL,
         USER_DESCRIPTION TEXT NOT NULL
         PRIMARY KEY 
          );"""

         )
    
     self.connect.commit()
    
   def Create_COURSE(self):
       self.cursor.execute(""" CREATE TABLE COURSE(
        CRN INTERGER NOT NULL,
        COURSE_NAME TEXT NOT NULL,
        COURSE_DAY TEXT NOT NULL,
        COURSE_TIME TEXT NOT NULL,
        INSTRUCTOR_NAME TEXT NOT NULL
        PRIMARY KEY
        );""")
       self.connect.commit()
        

   def Insert_USER(self,Password,USER,ID):
      Value =f"""INSERT INTO  AUTHENTIFY VALUES((?),(?),(?));"""
      self.cursor.execute(Value,(Password,USER,ID))
      self.connect.commit()
    
   def Insert_COURSE(self,crn,course_name,course_day,course_time,instructor_name):
      Value= f"""INSERT INTO COURSE VALUES((?),(?),(?),(?),(?));"""
      self.cursor.execute(Value,(crn,course_name,course_day,course_time,instructor_name))
      self.connect.commit()
    
   def Insert_STUDENT(self,Id,Name,Surname,Gradyear,Major,Email):
       Values=f"""INSERT INTO STUDENT VALUES((?),(?),(?),(?),(?),(?));"""
       self.cursor.execute(Values,(Id,Name,Surname,Gradyear,Major,Email))
       self.connect.commit()

   def Insert_INSTRUCTOR(self,Id,Name,Surname,Title,Hireyear,Department,Email):
      Values=f"""INSERT INTO INSTRUCTOR VALUES((?),(?)(?),(?),(?),(?),(?));"""
      self.cursor.execute(Values,(Id,Name,Surname,Title,Hireyear,Department,Email))
      self.connect.commit()

   def Alter(self,col,New_variable):
     Val=f""" ALTER TABLE {New_variable} ADD COLUMN {col};"""
     self.cursor.execute(Val)
     self.connect.commit()
    
   def Fetch(self):
     self.cursor.execute()

Database= Class_Creator("Leopard_web_project/Database/tables.db")
Database.Connect()

Database.Insert_STUDENT(123,"M","G",2023,"BSCE","GM")


Database.Disconnect()

