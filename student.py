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
          self.connect=sqlite3.connect("Leopard_web_project/Database/tables.db")
          self.cursor=self.connect.cursor()
        
       def Disconnect(self):
          if self.connect:
            self.cursor.close()
       def implement(self):
            
            Update="""INSERT INTO STUDENT VALUES(?,?,?,?,?,?)"""
            Values=(self.ID,self.first_name,self.last_name,self.graduate,self.Major,self.Email)
            self.cursor.execute(Update,Values)
            self.connect.commit()
            

  
            
       def Add_Course(self,crn):
         Fetch="""SELECT * FROM COURSE WHERE CRN =? """
         course_crn=crn
         self.cursor.execute(Fetch,(course_crn,))
         result= self.cursor.fetchall()
         for row in result:
           CRN=row[0]
           Course_name=row[1]
           Course_day=row[2]
           Course_time=row[3]
           Instructor_name=row[4]
           Added=f"[{Course_name}|{Course_day}|{Course_time}|{Instructor_name}]"
         return Added
        
       def update(self,crn,student_name):
            self.connect=sqlite3.connect("Leopard_web_project/Database/tables.db")
            self.cursor=self.connect.cursor()
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
                 for element in New_roster:
                   if student_name not in New_roster:
                        New_roster.append(student_name)

                 Update_roster='\n'.join(New_roster)
                 Update="""UPDATE COURSE SET ROSTER=? WHERE CRN=? """
                 self.cursor.execute(Update,(str(Update_roster),course_crn))


            self.connect.commit()
     
       def Append(self,Course_number):
          self.schedule[Course_number]= self.Add_Course(Course_number)
          self.update_schedule(Course_number)
          self.update(Course_number,self.first_name)

       def Remove(self,Course_number):
         del self.schedule[Course_number]
        
       def update_schedule(self,CRN):
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
        if Result[0] is None:
            Schedule_data=[]
            Schedule_data.append(Update)
            schedule_data= '\n'.join(Schedule_data)
            Function="UPDATE STUDENT SET SCHEDULE=? WHERE NAME=?"
            self.cursor.execute(Function,(schedule_data,self.first_name))
            self.connect.commit()
        else:
            imported=Result[0]
            Schedule_data=imported.split('\n')
            Schedule_data.append(Update)
            schedule_data= '\n'.join(Schedule_data)
            Function="UPDATE STUDENT SET SCHEDULE=? WHERE NAME=?"
            self.cursor.execute(Function(schedule_data,self.first_name))
            self.connect.commit()      
      
       def display_schedule(self):
         for row in self.schedule:
            print(row)


         

      



         
        
        



