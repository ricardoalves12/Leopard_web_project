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
         USER_ID INTERGER NOT NULL
         PRIMARY KEY 
          );"""

         )
     self.connect.commit()

   def Insert(self,Password,USER,ID):
      Value =f"""INSERT INTO  AUTHENTIFY VALUES((?),(?),(?));"""
      self.cursor.execute(Value,(Password,USER,ID))
      self.connect.commit()

Database= Class_Creator("Database/tables.db")
Database.Connect()

Database.Insert('MamaGuevo','RicoA',10014)
Database.Disconnect()

