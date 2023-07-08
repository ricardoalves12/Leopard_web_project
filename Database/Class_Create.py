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
        USER_ID INTERGER NOT NULL,
        STATUS TEXT NOT NULL,
        FIRST NAME TEXT NOT NULL,
        LAST NAME TEXT  NOT NULL,
        USERNAME TEXT NOT NULL,
        PASSWORD TEXT NOT NULL
         
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
    
   def Alter_name(self,table,old_name,new_name):
     Valu=f"ALTER TABLE {table} RENAME COLUMN {old_name} TO  {new_name};"
     self.cursor.execute(Valu)
   def Alter_delete(self,Variable):
     Value=f"DROP TABLE {Variable};"
     self.cursor.execute(Value)
     

Database= Class_Creator("Leopard_web_project/Database/tables.db")
Database.Connect()

# Database.Alter_delete("AUTHENTIFY","PASSWORD")
# Database.Alter_delete("AUTHENTIFY","USERNAME")

# Database.Alter_delete("AUTHENTIFY","Description")

# Database.Alter("ID","AUTHENTIFY")
# Database.Alter("USER NAME","AUTHENTIFY")
# Database.Alter("PASSWORD","AUTHENTIFY")
# Database.Alter("STATUS","AUTHENTIFY")

# Database.Alter_name("AUTHENTIFY","STATUS","NONE")
#Database.Alter_delete("AUTHENTIFY","NONE")
#Database.Alter_name("AUTHENTIFY","Description","STATUS")
#Database.Alter_delete("AUTHENTIFY","ID")
#Database.Alter_delete("AUTHENTIFY")
Database.Create()
Database.Disconnect()

