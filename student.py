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
            Values=(self.ID,self.first_name,self.last_name,self.Major,self.graduate,self.Email)
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
           print(f"CRN: {CRN}\n Course day : {Course_day}\n Course time: {Course_time}\n Teacher: {Instructor_name}")
          else:
            print("Course doesn't exist ")
            
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

print(" Hello new user ")
Name=input("Can you please enter your first name: ")
Name2=input("Can you please enter your last name: ")
id = random.randint(1000,3000)
status=input("Please enter your status at the school :")
New_User=User(Name,Name2,id,"STUDENT")
New_User.Connect()
#New_User.implement()

if New_User.status=="STUDENT":
     Major=input(" Please enter your major: ")
     Gradyear=input(" when do you expect to gradute: ")
     Grad=int(Gradyear)
     New_student=Student(Name,Name2,id,Major,Grad,status)
     New_student.Connect()
     command=input(" Enter a command: ")

     #New_student.implement()
     if command=="1":
      New_student.search_Course(234)
      print('\n')
     elif command=="2":
      print(New_student.Add_Course(234))
      New_student.Append(234)
      New_student.Append(205)
      New_student.Add_Course(120)
      New_student.update(35,New_student.first_name)
      for key,value in New_student.schedule.items():
         print(f"{key} : {value}")
      New_student.Remove(205)
      print("\n")
      for key,value in New_student.schedule.items():
         print(f"{key} : {value}")
      New_student.Disconnect()

New_student.Disconnect()
         

      



         
        
        



