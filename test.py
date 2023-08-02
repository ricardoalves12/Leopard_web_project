import sqlite3
import random
from user import User
from student import Student
from Teacher import Teacher
from Admin import Admin
# Test_User=User("Marie","Curie",10002,"STUDENT")
# Test_User.Connect()


# Test_User.cursor.execute("SELECT 1 FROM AUTHENTIFY WHERE USER_ID=?",(Test_User.ID,))
# test1=Test_User.cursor.fetchone()
# if test1:
#      print("Test 1 implementation ")
#      Test_User.cursor.execute("SELECT * FROM AUTHENTIFY WHERE USER_ID=?",(Test_User.ID,))  
#      selected=Test_User.cursor.fetchall()
#      for element in selected:
#        print(element)
#        print('\t')
# else:
#       print("User not found ")
# Test_User.cursor.execute("SELECT * FROM COURSE ")
# test2=Test_User.cursor.fetchall()
# if test2:
#       print("Test 2 display course  ")
#       Test_User.print_all_course()
#       CRN=205
#       Test_User.cursor.execute("SELECT 1 FROM COURSE WHERE CRN=?",(CRN,))
#       print('\t')
# test3=Test_User.cursor.fetchone()
# if test3:
#       print("Test 3 display course information  ")
#       Test_User.search_Course(CRN)
# else:
#       print("Course not part of table ")



Test_Student=Student("Thomas","Edison",10004,"BSEE",1879,"STUDENT")
Test_Student.Connect()
Test_Student.cursor.execute("SELECT 1 FROM STUDENT WHERE ID=?",(Test_Student.ID,))
test1s=Test_Student.cursor.fetchone()
if test1s:
      print("Test 1 Add and Remove\t  ")
      CRN=363
      CRN2=120
      CRN3=478
      CRN4=35

      Test_Student.Add_Course(CRN)
      Test_Student.display_schedule()  

#       Test_Student.Append(CRN2)
#       Test_Student.update(CRN2,Test_Student.first_name)

#       Test_Student.Append(CRN3)
#       Test_Student.update(CRN3,Test_Student.first_name)

#       Test_Student.Append(CRN4)
#       Test_Student.update(CRN4,Test_Student.first_name)
#       print(
     
    

# else:
#        print('Add and remove failed\t ')
# test2=Test_Student.cursor.fetchone()
# if test1s:
#        print("Test 2 Add and Remove\t  ")
#        Test_Student.Remove(CRN)
#        Test_Student.UPDATE()
#        Test_Student.display_schedule()
# else:
#      print('Add and remove failed\t ')

Test_Teacher=Teacher("Galileo","Galilei",20003,"BSAS","INSTUCTOR","Full Prof",1600)
Test_Teacher.Connect()
Test_Teacher.cursor.execute("SELECT 1 FROM INSTRUCTOR WHERE ID=?",(Test_Teacher.ID,))  
test1t=Test_Teacher.cursor.fetchone()
if test1t:
  print("Test 1 print roster\t ")
  CRN=363
#  Test_Teacher.print(CRN)
# else:
#    print("print roster doesn't work\t")
Test_Admin=Admin("Margaret","Hamilton",30001,"ADMIN","President","Dobbs 1600")
Test_Admin.Connect()
Test_Admin.cursor.execute("SELECT 1 FROM ADMIN WHERE ID=?",(Test_Admin.ID,))  
test1a=Test_Admin.cursor.fetchone()

# if test1a:
#     CRN=random.randint(100,500)
#     test_case=Test_Admin.Add(CRN,"CALCULUS","M","W",11,12,"Zang")
#     CRN2=random.randint(100,500)
#     if CRN==CRN2:
#       CRN2=random.randint(100,500)
#     test_case=Test_Admin.Add(CRN2,"CHEMESTRY","T","R",9,10,"Lavoisse")
#     CRN3=random.randint(100,500)
#     test_case=Test_Admin.Add(CRN3,"ARCHITECTURE","M","F",2,3,"Trance")
#     CRN4=random.randint(100,500)
#     test_case=Test_Admin.Add(CRN4,"ECON","T","F",8,9,"Amir")
#     CRN5=random.randint(100,500)
#     test_case=Test_Admin.Add(CRN5,"PHYSICS","M","W",11,12,"Jean")
#     CRN6=random.randint(100,500)
#     test_case=Test_Admin.Add(CRN6,"INTRO TO CS","W","F",10,11,"Sara")
   
#if test_case:
        #print("Course has been added")
    #else:
        #print("Function Add course doesn't work")
# test_case1=Test_Admin.Remove(328)
# test_case1=Test_Admin.Remove(310)
# test_case1=Test_Admin.Remove(325)
# test_case1=Test_Admin.Remove(295)
# if test_case1:
#          print("Course has been removed+0")
# else:
#          print("Function remove course doesn't work")
#Test_Admin.Remove_from_schedule("Nikola",478)
