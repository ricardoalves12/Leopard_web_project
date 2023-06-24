class Admin:
    def __init__(self,Name):
      self.name=Name
       
    def Data(self,name):
      self.Database=name
      self.connection=None
      self.cursor=None
    def Connect(self):
      import sqlite3
      self.connection=sqlite3.connect(self.Database)
      self.cursor=self.connection.cursor()
    
    def Disconnect(self):
        if self.connection:
           self.connection.close()
    
    def Add_Student():
        
        
        

    def modify(self):
        print(f'You can now modify the system ')





