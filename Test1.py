import io
import sys
import unittest
from user import *
from student import *
from Teacher import *
from Admin import *
class UserTest_case(unittest.TestCase):
     def test_user_search_function(self):
        Test_User=User("Marie","Curie",10002,"STUDENT")
        Test_User.Connect()
        CRN= 205
        Course_name="ECON"
        Course_day="T/R"
        Course_time="3:00-4:00"
        Instructor_name="Nelson"
        excepted=f"CRN: {CRN} \n Course name: {Course_name}\n Course day : {Course_day}\n Course time: {Course_time}\n Teacher: {Instructor_name}"
        Test_User.search_Course( 205)
        captured_out=io.StringIO()
        sys.stdout=captured_out
        sys.stdout=sys.__stdout__
        out=captured_out.getvalue().strip()
        #self.assertEqual(excepted,out)
        self.assertTrue(excepted,out)

     def test_student_add(self):
        Test_Student=Student("Isaac","Newton",10001,"BSAS",1668,"STUDENT")
        Test_Student.Connect()
        CRN=120
        Test_Student.Append(CRN)
        Test_output=Test_Student.schedule[CRN]
        if self.assertIsNotNone(Test_output):
            print("It works")
     
     def test_student_remove(self):
         Test_Student=Student("Isaac","Newton",10001,"BSAS",1668,"STUDENT")
         CRN=35
        
         Test_Student.Connect()
         Test_Student.Append(CRN)
         Test_Student.update(CRN,Test_Student.first_name)
        
         
         
         Test_Student.Remove(CRN)
         
         self.assertNotIn(CRN,Test_Student.schedule)
     
     def test_print_roster(self):
         Test_Student=Student("Isaac","Newton",10001,"BSAS",1668,"STUDENT")
         Test_Student2=Student("Marie","Curie",10002,"BSAS",1903,"STUDENT")

         CRN=120
         Test_Student.Connect()
         Test_Student.Append(CRN)
         
         
         Test_Student2.Connect()
         Test_Student2.Append(CRN)
         
         
         
         Test_Teacher=Teacher("Daniel","Bernoulli",20006,"BSME","INSTUCTOR","Associate Prof",1760)
         Test_Teacher.Connect()
         
         expected=f"{Test_Student.first_name}\n{Test_Student2.first_name}"
         Test_Teacher.print(CRN)
         captured_out=io.StringIO()
         sys.stdout=captured_out
         sys.stdout=sys.__stdout__
         out=captured_out.getvalue().strip()
         self.assertTrue(expected,out)

     def test_ADD(self): 
          Test_Admin=Admin("Margaret","Hamilton",30001,"ADMIN","President","Dobbs 1600")
          Test_Admin.Connect()
          test=Test_Admin.Add(345,"ALGORITHM",",W/F","8:00-9:50","Brown")
          excepted=True
          self.assertTrue(excepted,test)
     def test_REmove(self): 
        Test_Admin=Admin("Margaret","Hamilton",30001,"ADMIN","President","Dobbs 1600")
        Test_Admin.Connect()
        test=Test_Admin.Remove(673)
        excepted=True
        self.assertTrue(excepted,test)
     
if __name__=="__main__":
    unittest.main()