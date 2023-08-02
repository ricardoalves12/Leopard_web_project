from user import User 
import sqlite3
import random 
class Student(User):
       def __init__(self,first_name,last_name,id,major,grad_year,status):
          super().__init__(first_name,last_name,id,status)
          
          
          self.Major=major
          self.graduate=grad_year
          self.Email= self.first_name + self.last_name[0] + " @wit.edu"
          self.schedule={}
          self.cursor=None
          self.connect=None
     
       def Connect(self):
          self.connect=sqlite3.connect("Documents/LeoRepo/Leopard_web_project/Database/tables.db")
          self.cursor=self.connect.cursor()
        
       def Disconnect(self):
          if self.connect:
            self.cursor.close()
       def implement(self):
            
            Update="""INSERT INTO STUDENT VALUES(?,?,?,?,?,?)"""
            Values=(self.ID,self.first_name,self.last_name,self.graduate,self.Major,self.Email)
            self.cursor.execute(Update,Values)
            self.connect.commit()
            

            

       def search_Course(self,crn):
          
          Fetch="""SELECT * FROM COURSE WHERE CRN =? """
          course_crn=crn
          self.cursor.execute(Fetch,(course_crn,))
          result= self.cursor.fetchall()
          if result:
           for row in result:
             CRN=row[0]
             Course_name=row[1]
             Course_day=row[2]
             Course_time=row[3]
             Instructor_name=row[4]
           print(f"CRN: {CRN}\n Course name: {Course_name}\n Course day : {Course_day}\n Course time: {Course_time}\n Teacher: {Instructor_name}")
          else:
            print("Course doesn't exist ")
            
       def Add_Course(self,crn):
          Value="""SELECT * FROM  COURSE WHERE CRN=?"""
          self.cursor.execute(Value,(crn,))
          Schedule=self.cursor.fetchall()
          for element in Schedule:
            CRN=element[0]
            C_NAME=element[1]
            S_DAY=element[2]
            E_DAY=element[3]
            S_TIME=element[4]
            E_TIME=element[5]
            T_NAME=element[6]
          Value="""INSERT INTO SCHEDULE(ID,ST_NAME,CRN,COURSE,S_DAY,E_DAY,S_TIME,E_TIME,T_NAME) VALUES(?,?,?,?,?,?,?,?,?)"""  
          Val=(self.ID,self.first_name,CRN,C_NAME,S_DAY,E_DAY,S_TIME,E_TIME,T_NAME)
          self.cursor.execute(Value,(Val))
          self.connect.commit()

            

           
        
       def update(self,crn,student_name):
            Fetch="""SELECT ROSTER FROM COURSE WHERE CRN =? """
            course_crn=crn
            self.cursor.execute(Fetch,(course_crn,))
            result=self.cursor.fetchone()
            
            if result[0] is None:
                
                Array=[]
                Array.append(student_name)
                New_roster='\n'.join(Array)
                Update="""UPDATE COURSE SET ROSTER=? WHERE CRN=? """
                self.cursor.execute(Update,(str(New_roster),course_crn))
            else:
                 New=result[0]
                 New_roster=New.split('\n')
                 New_roster.append(student_name)
                 Update_roster='\n'.join(New_roster)
                 Update="""UPDATE COURSE SET ROSTER=? WHERE CRN=? """
                 self.cursor.execute(Update,(str(Update_roster),course_crn))


            self.connect.commit()
            
                
          
           
           

       
       def Append(self,Course_number):
         self.schedule[Course_number]= self.Add_Course(Course_number)
         Fetch="""SELECT ROSTER FROM COURSE WHERE CRN =? """
         course_crn=Course_number
         self.cursor.execute(Fetch,(course_crn,))
         result=self.cursor.fetchone()
            
         if result[0] is None:
                
           Array=[]
           Array.append(self.first_name)
           New_roster='\n'.join(Array)
           Update="""UPDATE COURSE SET ROSTER=? WHERE CRN=? """
           self.cursor.execute(Update,(str(New_roster),course_crn))
         else:
            New=result[0]
            New_roster=New.split('\n')
            New_roster.append(self.first_name)
            Update_roster='\n'.join(New_roster)
            Update="""UPDATE COURSE SET ROSTER=? WHERE CRN=? """
            self.cursor.execute(Update,(str(Update_roster),course_crn))
       
       def Remove(self,Course_number):
         del self.schedule[Course_number]
         Fetch="""SELECT ROSTER FROM COURSE WHERE CRN =? """
         course_crn=Course_number
         self.cursor.execute(Fetch,(course_crn,))
         result=self.cursor.fetchone()
         New=result[0]
         
         New_roster=New.split('\n')
         New_roster.remove(self.first_name)
         Update_roster='\n'.join(New_roster)
         Update="""UPDATE COURSE SET ROSTER=? WHERE CRN=? """
         self.cursor.execute(Update,(Update_roster,course_crn))
         self.connect.commit()
         print(Update_roster)
        
       def update_schedule(self,CRN):
        Update_array=[]
        for key ,elemement in self.schedule.items:
            Update_array.append(self.schedule[elemement])

        Value="SELECT * FROM COURSE WHERE CRN=? "
        Vals=(CRN,)
        self.cursor.execute(Value,Vals)
        result=self.cursor.fetchall()
        for row in result:
            CRN=row[0]
            Course_name=row[1]
            Course_day=row[2]
            Course_time=row[3]
            Instructor=row[4]
        Update=(f"CRN: {CRN} |Course name : {Course_name} |Course day: {Course_day}| Course time: {Course_time} | Instructor: {Instructor}")
        value="SELECT SCHEDULE FROM STUDENT WHERE NAME=? "
        vals=(self.first_name,)
        self.cursor.execute(value,vals)
        Result=self.cursor.fetchone()
        if Result is None:
            Schedule_data=[]
            Schedule_data.append(Update)
            schedule_data= '\n'.join(Schedule_data)
            Function="UPDATE STUDENT SET SCHEDULE=? WHERE NAME=?"
            self.cursor.execute(Function,(schedule_data,self.first_name))
            self.connect.commit()
        else:
            imported=Result[0]
            Schedule_data=imported.split('|')
            Schedule_data.append(Update)
            schedule_data= '\n'.join(Schedule_data)
            Function="UPDATE STUDENT SET SCHEDULE=? WHERE NAME=?"
            self.cursor.execute(Function(schedule_data,self.first_name))
            self.connect.commit()



        

       
       def display_schedule(self):
         for row, element in self.schedule.items():
            print(row,element)

       def UPDATE(self):
         
         Update_array=[]
         for key,element in self.schedule.items():
            Update_array.append(element)
            Upd='|'.join(Update_array)
            Up="""UPDATE STUDENT SET SCHEDULE=? WHERE NAME=? """
            self.cursor.execute(Up,(Upd,self.first_name),)
            self.connect.commit()
            print(Upd)

            