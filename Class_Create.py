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
         FIRST_NAME TEXT NOT NULL,
         LAST_NAME TEXT NOT NULL,
         USER_NAME TEXT NOT NULL,
         PASSWORD TEXT NULL
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
        

   def Insert(self,Password,USER,ID):
      Value =f"""INSERT INTO  AUTHENTIFY VALUES((?),(?),(?));"""
      self.cursor.execute(Value,(Password,USER,ID))
      self.connect.commit()
    
   def delete(self):
     Value=""" DROP TABLE AUTHENTIFY"""
     self.cursor.execute(Value)
     self.connect.commit()

   def Alter(self,col,New_variable):
     Val=f""" ALTER TABLE {New_variable} ADD COLUMN {col};"""
     self.cursor.execute(Val)
     self.connect.commit()

# Database=Class_Creator("Leopard_web_project/Database/tables.db")
# Database.Connect()
# Database.Create()

Dict={}
Dict[45]="Dog"


# Database.Disconnect()

