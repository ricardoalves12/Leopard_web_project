import sqlite3
import random
from user import User


class Admin(User):
    def __init__(self,first_name,last_name,ID):
       super().__init__(first_name,last_name,ID)
       

    def Add_Course(self,CRN,C_Name,S_day,E_day,S_time,E_time,T_name):
        if (CRN != '' and C_Name != '' and S_day!= '' and E_day != '' and S_time!= '' and E_time!= '' and T_name!= ''):
          self.connect=sqlite3.connect("Database/tables.db")
          self.cursor=self.connect.cursor()
          Value ="""INSERT INTO COURSE(CRN,C_NAME,S_DAY,E_DAY,S_TIME,E_TIME,T_NAME) VALUES(?,?,?,?,?,?,?)"""
          Values=(CRN,C_Name,S_day,E_day,S_time,E_time,T_name)
          self.cursor.execute(Value,Values)
          self.connect.commit()
          self.connect.close()
        else:
            return False
    
    def Remove_Course(self,CRN):
      self.connect=sqlite3.connect("Database/tables.db")
      self.cursor=self.connect.cursor()
      self.cursor.execute("SELECT 1 FROM COURSE WHERE CRN =?", (CRN,))
      crn_exist = self.cursor.fetchone()
      if crn_exist:
          Value ="""DELETE FROM COURSE WHERE CRN=?"""
          Values=(CRN,)           
          self.cursor.execute(Value,Values)
          self.connect.commit()          
          Valu1="""DELETE FROM SCHEDULE WHERE CRN=?"""
          self.cursor.execute(Valu1,Values)
          self.connect.commit()
          self.connect.close()
      else:
          return False

    def Add_Teacher(self,T_name,T_last_name,T_title,T_hyear,T_department):
        if (T_name != '' and T_last_name != '' and T_title!= '' and T_hyear!= '' and T_department!= ''):
          self.connect=sqlite3.connect("Database/tables.db")
          self.cursor=self.connect.cursor()
          ID=random.randint(2007,3000)
          password = "123"
          Email=T_name + T_last_name[0]+ "@wit.edu"
          user_name=T_last_name+T_name[0]
          Value="""INSERT INTO INSTRUCTOR VALUES(?,?,?,?,?,?,?)"""
          Val=(ID,T_name,T_last_name,T_title,T_hyear,T_department,Email)
          self.cursor.execute(Value,(Val))
          self.connect.commit()
          Value1="""INSERT INTO AUTHENTIFY(USER_ID,STATUS,FIRST_NAME,LAST_NAME,USER_NAME,PASSWORD) VALUES (?,?,?,?,?,?)"""
          Val1=(ID,"INSTRUCTOR",T_name,T_last_name,user_name,password)
          self.cursor.execute(Value1,(Val1))
          self.connect.commit()
          self.connect.close()
        else:
            return False

    def Add_student(self,S_name,S_last_name,S_Gradyear, S_Major):
        if (S_name != '' and S_last_name != '' and S_Gradyear != '' and S_Major != ''):
          self.connect=sqlite3.connect("Database/tables.db")
          self.cursor=self.connect.cursor()
          ID=random.randint(10012,20000)
          password = "123"
          Email=S_name+S_last_name[0]+"@wit.edu"
          username=S_last_name+S_name[0]
          Value="""INSERT INTO STUDENT(ID,NAME,SURNAME,GRADYEAR,MAJOR,EMAIL) VALUES(?,?,?,?,?,?)"""
          Val=(ID,S_name,S_last_name,S_Gradyear,S_Major,Email)
          self.cursor.execute(Value,(Val))
          self.connect.commit()
          Value1="""INSERT INTO AUTHENTIFY(USER_ID,STATUS,FIRST_NAME,LAST_NAME,USER_NAME,PASSWORD) VALUES (?,?,?,?,?,?)"""
          Val1=(ID,"STUDENT",S_name,S_last_name,username,password)
          self.cursor.execute(Value1,(Val1))
          self.connect.commit()
        else:
            return False

    def unlink_T(self,CRN, T_name):      
      self.connect=sqlite3.connect("Database/tables.db")
      self.cursor=self.connect.cursor()
      self.cursor.execute("SELECT 1 FROM COURSE WHERE CRN =? AND T_NAME =? ", (CRN, T_name,))
      tname_crn_exist = self.cursor.fetchone()
      if tname_crn_exist:
          Value="""UPDATE COURSE SET T_NAME=? WHERE CRN=? """
          self.cursor.execute(Value,("Undefined ",CRN))
          self.connect.commit()
          Value1="""UPDATE SCHEDULE SET T_NAME=? WHERE CRN=? """
          self.cursor.execute(Value1,("No Teacher",CRN))
          self.connect.commit()
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
          self.cursor.execute(Value1,(new_T,CRN,))
          self.connect.commit()
      else:
          return False

    def unlink_S(self,CRN,ID):
        self.connect=sqlite3.connect("Database/tables.db")
        self.cursor=self.connect.cursor()
        if (CRN != '' and ID != '' ):
          self.cursor.execute("SELECT 1 FROM SCHEDULE WHERE CRN =? AND ID=?", (CRN,ID))
          id_crn_exist = self.cursor.fetchone()
          if id_crn_exist:
              Value="""DELETE FROM SCHEDULE WHERE ID=? AND CRN=?"""
              numb = (ID,CRN,)
              self.cursor.execute(Value,numb)
              self.connect.commit()
              self.connect.close()
          else:
              return False
        else:
            return False


    def Check_conflict(self,crn,ID):
          self.connect=sqlite3.connect("Database/tables.db")
          self.cursor=self.connect.cursor()
          Value1="""SELECT * FROM COURSE WHERE CRN=?"""
          self.cursor.execute(Value1,(crn,))
          Add_Course=self.cursor.fetchall()
          for C_info in Add_Course:
            S_DAY=C_info[2]
            E_DAY=C_info[3]
            S_TIME=C_info[4]
            E_TIME=C_info[5]

          Value=""" SELECT * FROM SCHEDULE WHERE ID=?"""  
          self.cursor.execute(Value,(ID,))
          Check_list=self.cursor.fetchall()
          Check_List_S_DAY=[]
          Check_List_E_DAY=[]
          Check_List_S_TIME=[]
          Check_List_E_TIME=[]
         
          for element in Check_list:
            Check_List_S_DAY.append(element[4])
            Check_List_E_DAY.append(element[5])
            Check_List_S_TIME.append(element[6])
            Check_List_E_TIME.append(element[7])
          if (Check_List_S_DAY !=[] and Check_List_E_DAY !=[] and Check_List_S_TIME !=[] and Check_List_E_TIME !=[]):
              if S_DAY in  Check_List_S_DAY or E_DAY in Check_List_E_DAY:
                  if S_TIME not in Check_List_S_TIME and S_TIME not in Check_List_E_TIME:
                   if E_TIME not in Check_List_E_TIME and E_TIME not in Check_List_S_TIME:
                     return True
              else: 
                  return True
          else:
              return True

    

    def Link_S(self,CRN,ID):
       self.connect=sqlite3.connect("Database/tables.db")
       self.cursor=self.connect.cursor()
       self.cursor.execute("SELECT 1 FROM COURSE WHERE CRN =? ", (CRN,))
       crn_exist = self.cursor.fetchone()
       self.cursor.execute("SELECT 1 FROM STUDENT WHERE ID =? ", (ID,))
       ID_exist = self.cursor.fetchone()
       if CRN != '' and ID != '' and crn_exist != None  and ID_exist != None:
           self.connect=sqlite3.connect("Database/tables.db")
           self.cursor=self.connect.cursor()
           Value="""SELECT * FROM COURSE WHERE CRN=?"""
           self.cursor.execute(Value,(CRN,))
           C_info=self.cursor.fetchall()
           if self.Check_conflict(CRN,ID):
            for element in C_info:
             CRN=element[0]
             C_NAME=element[1]
             S_DAY=element[2]
             E_DAY=element[3]
             S_TIME=element[4]
             E_TIME=element[5]
             T_NAME=element[6]
            Value1="""SELECT * FROM STUDENT WHERE ID=?"""
            self.cursor.execute(Value1,(ID,))
            S_INFO=self.cursor.fetchall()
            for info in S_INFO:
             S_ID=info[0]
             S_NAME=info[1]
             Valu1="""INSERT INTO SCHEDULE(ID,ST_NAME,CRN,COURSE,S_DAY,E_DAY,S_TIME,E_TIME,T_NAME) VALUES(?,?,?,?,?,?,?,?,?)"""
             Val1=(S_ID,S_NAME,CRN,C_NAME,S_DAY,E_DAY,S_TIME,E_TIME,T_NAME)  
             self.cursor.execute(Valu1,(Val1))
             self.connect.commit()
           else:
            return False
       else:
           return False
