import sqlite3
import random
from user import User


class Admin(User):
    def __init__(self,first_name,last_name,ID):
       super().__init__(self,first_name,last_name,ID)
       

    def Add_Course(self,id,C_Name,S_day,E_day,S_time,E_time,T_name):
        if (id != " " and C_Name != " " and S_day!= " " and E_day != " " and S_time!= " " and E_time!= " " and T_name!= " "):
          self.connect=sqlite3.connect("Database/tables.db")
          self.cursor=self.connect.cursor()
          Value ="""INSERT INTO COURSE(CRN,C_NAME,S_DAY,E_DAY,S_TIME,E_TIME,T_NAME) VALUES(?,?,?,?,?,?,?)"""
          Values=(id,C_Name,S_day,E_day,S_time,E_time,T_name)
          self.cursor.execute(Value,Values)
          self.connect.commit()
          self.connect.close()
        else:
            return False
    
    def Remove_Course(self,CRN):
      self.connect=sqlite3.connect("Database/tables.db")
      self.cursor=self.connect.cursor()
      self.cursor.execute("SELECT 1 FROM SCHEDULE WHERE CRN =? AND ID =? ", (CRN, self.ID))
      crn_exist = self.cursor.fetchone()
      if crn_exist:
          Value ="""DELETE FROM COURSE WHERE CRN=?"""
          Values=(CRN,)           
          self.cursor.execute(Value,Values)
          self.connect.commit()
          self.connect.close()
      else:
          return False

    def Add_Teacher(self,T_name,T_last_name,T_title,T_hyear,T_department):
        if (T_name != " " and T_last_name != " " and T_title!= " " and T_hyear!= " " and T_department!= " "):
          self.connect=sqlite3.connect("Database/tables.db")
          self.cursor=self.connect.cursor()
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
          self.connect.close()
        else:
            return False

    def Add_student(self,S_name,S_last_name,S_Gradyear, S_Major):
        if (S_name != " " and S_last_name != " " and S_Gradyear != " " and S_Major != " "):
          self.connect=sqlite3.connect("Database/tables.db")
          self.cursor=self.connect.cursor()
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
        else:
            return False

    def unlink_T(self,CRN):
      
      self.connect=sqlite3.connect("Database/tables.db")
      self.cursor=self.connect.cursor()
      self.cursor.execute("SELECT 1 FROM COURSE WHERE CRN =?", (CRN,))
      crn_exist = self.cursor.fetchone()
      if crn_exist:
          Value="""UPDATE COURSE SET T_NAME=? WHERE CRN=? """
          self.cursor.execute(Value,(" ",CRN))
          self.connect.commit()
          Value1="""UPDATE SCHEDULE SET T_NAME=? WHERE CRN=? """
          self.cursor.execute(Value1(" ",CRN,))
      else:
          return False

    def link_T(self,CRN,new_T):
      self.connect=sqlite3.connect("Database/tables.db")
      self.cursor=self.connect.cursor()
      self.cursor.execute("SELECT 1 FROM COURSE WHERE CRN =?", (CRN,))
      crn_exist = self.cursor.fetchone()
      if crn_exist and new_T != " ":
          Value="""UPDATE COURSE SET T_NAME=? WHERE CRN=? """
          self.cursor.execute(Value,(new_T,CRN))
          self.connect.commit()
          Value1="""UPDATE SCHEDULE SET T_NAME=? WHERE CRN=? """
          self.cursor.execute(Value1(new_T,CRN,))
      else:
          return False

    def unlink_S(self,CRN,ID):
      self.connect=sqlite3.connect("Database/tables.db")
      self.cursor=self.connect.cursor()
      self.cursor.execute("SELECT 1 FROM COURSE WHERE CRN =? AND ID=?", (CRN,ID))
      id_crn_exist = self.cursor.fetchone()
      if id_crn_exist:
          Value="""DELETE FROM SCHEDULE WHERE ID=? AND CRN=?"""
          self.cursor.execute(Value,(CRN,ID,))
          self.connect.commit()
          self.connect.close()
      else:
          return False



