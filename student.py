from user import User 
import sqlite3
import random 
class Student(User):
       def __init__(self):
          super().__init__()

       def search_Course(self,crn):
          self.connect=sqlite3.connect("Database/tables.db")
          self.cursor=self.connect.cursor()
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
           return(f"CRN: {CRN}\n Course day : {Course_day}\n Course time: {Course_time}\n Teacher: {Instructor_name}")
          else:
            return("Course doesn't exist ")
            
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
            
                
          
            # New_roster.extend(student_name)
            # update_roster="\n".join(New_roster)
            # Update="""UPDATE COURSE SET ROASTER=? WHERE CRN=? """
            # self.cursor.execute(Update,(update_roster,course_crn))
            # self.connect.commit()

           

       
       def Append(self,Course_number):
         self.schedule[Course_number]= self.Add_Course(Course_number)
       
       def Remove(self,Course_number):
         del self.schedule[Course_number]

       
       def display_schedule(self):
         for row in self.schedule:
            print(row)



      



         
        
        



