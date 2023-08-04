import sqlite3
import random
from user import User
class Teacher(User):
         def __init__(self,first_name,last_name,ID):
             super().__init__(first_name,last_name,ID) 
         
         def print_T_schedule(self):
            self.connect=sqlite3.connect("Database/tables.db")
            self.cursor=self.connect.cursor()
            Fetch="""SELECT * FROM COURSE WHERE T_NAME=?"""
            self.cursor.execute(Fetch,(self.first_name,))
            Schedule=self.cursor.fetchall()
            new_array=[]
            for element in Schedule:
                CRN=element[0]
                C_NAME=element[1]
                S_DAY=element[2]
                E_DAY=element[3]
                S_TIME=element[4]
                E_TIME=element[5]
                new_array.append(f"{CRN}|{C_NAME}|{S_DAY}|{E_DAY}|{S_TIME}|{E_TIME}")
            String_array='\n'.join(new_array)
            self.cursor.close()
            return String_array         

         def print_S_list(self, crn):
            self.connect=sqlite3.connect("Database/tables.db")
            self.cursor=self.connect.cursor()
            self.cursor.execute("SELECT 1 FROM SCHEDULE WHERE T_NAME =? AND CRN =?", (self.first_name,crn))
            exist = self.cursor.fetchone()
            if exist:
                Fetch=""" SELECT * FROM SCHEDULE WHERE T_NAME=? AND CRN=? """
                self.cursor.execute(Fetch,(self.first_name,crn))
                result=self.cursor.fetchall()
                new_list=[]
                for element in result:
                    new_list.append(element[1])
                String_List='\n'.join(new_list)
                self.connect.close()
                return String_List
            else:
                return False
        
        