import sqlite3

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
    
    def implement(self):
        Value="""INSERT INTO AUTHENTIFY(USER_ID,STATUS,FIRST_NAME,LAST_NAME,USER_NAME) VALUES (?,?,?,?,?)"""
        User_name= self.last_name + self.first_name[0]
        Values=(self.ID,self.status,self.first_name,self.last_name,User_name)
        self.cursor.execute(Value,Values)
        self.connect.commit()
     
# New_User=User("Tomasso","Verdignolet",2001,"STUDENT")
# New_User.Connect()
# New_User.implement()

# if New_User.status=="STUDENT":
#     New_student=Student("BCSO",2024)
#     New_student.implement()

#New_student.Disconnect()
       