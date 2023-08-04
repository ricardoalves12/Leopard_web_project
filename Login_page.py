from tkinter import *
import tkinter 
#pip install pillow
from PIL import ImageTk, Image 
from tkinter import PhotoImage, messagebox
from tkinter.messagebox import *
import sqlite3
import student
from student import *
import Teacher
from Teacher import *
import Admin
import user
from user import *

global UserId

class MainPage(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.user_id = None
        self.user = User(" ", " ", 0)        
        self.user_name = None
        self.title("Leopard Web") 
        #setting page geometry to the size of the user's screen
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.geometry("%dx%d" % (width_screen, height_screen))
        self.iconphoto(False, PhotoImage(file = 'Images_for_Gui/images.png'))
        self.login_frame = LoginFrame(self)
        self.student_frame = StudenthomeFrame(self)
        self.Instructor_frame = InstructorhomeFrame(self)
        self.Admin_frame = AdminFrame(self)
        self.student_search_class_frame = StudentSearchClassFrame(self)
        self.instructor_search_class_frame = InstructorSearchClassFrame(self)
        self.instructor_Print_Class_Frame = InstructorPrintFrame(self)
        self.admin_search_class_frame = AdminSearchClassFrame(self) 
        self.student_add_course_frame = StudentAddCourseFrame(self)
        self.admin_add_class_frame = AdminAddClassFrame(self)
        self.student_remove_course_frame = StudentDropCourseFrame(self)
        self.ShowLoginFrame()

    def updateLoginpage(self):
        self.title(f"{self.user.printInfo()}")
        self.login_frame = LoginFrame(self)
        self.student_frame = StudenthomeFrame(self)
        self.Instructor_frame = InstructorhomeFrame(self)
        self.Admin_frame = AdminFrame(self)
        self.student_search_class_frame = StudentSearchClassFrame(self)
        self.instructor_search_class_frame = InstructorSearchClassFrame(self)
        self.instructor_Print_Class_Frame = InstructorPrintFrame(self)
        self.admin_search_class_frame = AdminSearchClassFrame(self) 
        self.student_add_course_frame = StudentAddCourseFrame(self)
        self.admin_add_class_frame = AdminAddClassFrame(self)
        self.student_remove_course_frame = StudentDropCourseFrame(self)
        

    def ShowLoginFrame(self):
        #setting page geometry to the size of the user's screen
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.admin_search_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()

    def show_student_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.student_search_class_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.admin_search_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
    
    def show_Instructor_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.Instructor_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.Admin_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.admin_search_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.instructor_Print_Class_Frame.place_forget()
     
    def show_instructor_Print_Class_List_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_Print_Class_Frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.Admin_frame.place_forget()
        self.admin_search_class_frame.place_forget()


    def show_Admin_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.Admin_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.admin_search_class_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.admin_add_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        
    def show_student_search_Class_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.admin_search_class_frame.place_forget()
        self.admin_add_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()

    def show_instructor_search_Class_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.admin_search_class_frame.place_forget()
        self.admin_add_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()

    def show_admin_search_Class_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.admin_search_class_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()

    def show_student_add_Course_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_search_class_frame.place_forget()
        self.admin_add_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()

    def show_admin_add_Class_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.admin_add_class_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.student_add_course_frame.place_forget()
        self.student_remove_course_frame.place_forget()
    
    def show_student_drop_course_frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.admin_add_class_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.student_remove_course_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))

class LoginFrame (tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tkinter.Label(self, text="Enter Username & Password", font=('Times',14), bg="white")
        self.label.place(x=20, y=40)
        
        self.username_label = tkinter.Label(self, text="Username:", font=('Times',12), bg="white")
        self.username_label.place(x=20, y=80)
        self.username_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.username_entry.place(x=20, y=110)
        
        self.password_label = tkinter.Label(self, text="Password:", font=('Times',12), bg="white")
        self.password_label.place(x=20, y=140)
        self.password_entry = tkinter.Entry(self, show="*", highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.password_entry.place(x=20, y=170)
        
        self.login_button = tkinter.Button(self, text="Login", bg="red", fg="white", width=17, font=('Times',24), bd=0, command= self.login)
        self.login_button.place(x=20, y=210)
    def login(self):
        username = self.username_entry.get() 
        password = self.password_entry.get()
        self.username_entry.delete(0, END)
        self.password_entry.delete(0, END)
        DbConnect = sqlite3.connect("Database/tables.db")
        db= DbConnect.cursor()         
        if user.User.CheckLoginCredentials(self,username,password):
            for row in db.execute("SELECT * FROM AUTHENTIFY  WHERE USER_NAME = ? and PASSWORD = ? ", (username, password)):
                if row[1] == 'STUDENT': 
                    self.master.user.setUserInfo(str(row[2]), str(row[3]), int(row[0]))
                    self.master.updateLoginpage()
                    self.master.show_student_Frame()  
                elif row[1] == 'ADMIN':
                    self.master.user.setUserInfo(str(row[2]), str(row[3]), int(row[0]))
                    self.master.updateLoginpage()
                    self.master.show_Admin_Frame()
                elif row[1] == 'INSTRUCTOR':
                    self.master.user.setUserInfo(str(row[2]), str(row[3]), int(row[0]))
                    self.master.updateLoginpage()
                    self.master.show_Instructor_Frame()
                else:
                    messagebox.showerror("User type failed", "Invalid User type.")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
                
class StudenthomeFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        self.logout_button = tkinter.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=20)
       
        self.label = tkinter.Label(self, text="Student Home Page", font=('Times',12), bg="white")
        self.label.place(x=100, y=40)

        self.logout_button = tkinter.Button(self, text="Search Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.SearchClass)
        self.logout_button.place(x=20, y=120)

        self.logout_button = tkinter.Button(self, text="Add Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddCourse)
        self.logout_button.place(x=20, y=160)

        self.logout_button = tkinter.Button(self, text="Drop Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.DropCourse)
        self.logout_button.place(x=20, y=200)

        self.logout_button = tkinter.Button(self, text="Print schedule", font=('Times',12),  bg="black", fg="white", bd=0, command=self.PrintSchedule)
        self.logout_button.place(x=20, y=240)
    
    def PrintSchedule(self):
        self.student = Student(self.master.user.first_name, self.master.user.last_name, self.master.user.ID)
        schedule = "\n".join(self.student.display_schedule())
        messagebox.showinfo("Schedule", schedule)
        
    def SearchClass(self):
        tkinter.Listbox(self.master.show_student_search_Class_Frame())
    
    def DropCourse(self):
        self.master.show_student_drop_course_frame()

    def AddCourse(self):
        self.master.show_student_add_Course_Frame()

    def logout(self):
        self.master.title("Leopard Web") 
        self.master.ShowLoginFrame()

class InstructorhomeFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Instructor Home Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=30)

        self.PrintSchedule_button = tkinter.Button(self, text="Print Schedule", font=('Times',12),  bg="black", fg="white", bd=0, command = self.printSchedule)
        self.PrintSchedule_button.place(x=25, y=100)

        self.PrintClassList_button = tkinter.Button(self, text="Print Class List", font=('Times',12),  bg="black", fg="white", bd=0, command=self.PrintClassList)
        self.PrintClassList_button.place(x=25, y=150)

        self.SearchCourses_button = tkinter.Button(self, text="Search Courses", font=('Times',12),  bg="black", fg="white", bd=0, command=self.SearchClass)
        self.SearchCourses_button.place(x=25, y=200)

    def logout(self):
        self.master.title("Leopard Web") 
        self.master.ShowLoginFrame()

    def printSchedule(self):
        self.teacher = Teacher(self.master.user.first_name, self.master.user.last_name, self.master.user.ID)
        messagebox.showinfo("Schedule", self.teacher.print_T_schedule())

    def SearchClass(self):
        self.master.show_instructor_search_Class_Frame()

    def PrintClassList(self):
        self.master.show_instructor_Print_Class_List_Frame()

class InstructorPrintFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tkinter.Label(self, text="Print Class List Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.CRN_label = tkinter.Label(self, text="Enter CRN:", font=('Times',12), bg="white")
        self.CRN_label.place(x=20, y=70)
        self.CRN_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.CRN_entry.place(x=20, y=110)

        self.PrintClassList_button = tkinter.Button(self, text="Print Class List", font=('Times',12),  bg="black", fg="white", bd=0, command=self.PrintClassList)
        self.PrintClassList_button.place(x=25, y=150)
       
    def PrintClassList(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
        self.teacher = Teacher(self.master.user.first_name, self.master.user.last_name, self.master.user.ID)

        if self.teacher.print_S_list(CRN) != False:
            messagebox.showinfo("Class List",self.teacher.print_S_list(CRN))
        else:
            messagebox.showerror("Class List",f"Teacher not teaching course {CRN}, course does not exist, or no student is taking the course.")
        
    def Back(self):
        self.master.show_Instructor_Frame()
  



class AdminFrame (tkinter.Frame):
     def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Admin Main Menu", font=('Times',14), bg="white")
        self.label.place(x=20, y=40)

        self.logout_button = tkinter.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=30)
        
        self.Search_button = tkinter.Button(self, text="Search Courses", bg="black", fg="white", width=12, font=('Times',12), bd=0, command=self.SearchClass)
        self.Search_button.place(x=20, y=80)
        
        self.Add_button = tkinter.Button(self, text="Add Courses To System", bg="black", fg="white", width=10, font=('Times',12), bd=0, command=self.AddCoursetosystem)
        self.Add_button.place(x=20, y=120)
        
        self.Drop_button = tkinter.Button(self, text="Remove Courses From System", bg="black", fg="white", width=10, font=('Times',12), bd=0, command=self.logout)
        self.Drop_button.place(x=20, y=160)

        self.Print_button = tkinter.Button(self, text="Print Schedule", bg="black", fg="white", width=13, font=('Times',12), bd=0, command=self.logout)
        self.Print_button.place(x=20, y=200)

        self.Search_button = tkinter.Button(self, text="Search Schedule", bg="black", fg="white", width=13, font=('Times',12), bd=0, command=self.logout)
        self.Search_button.place(x=20, y=240)

        self.Add_button = tkinter.Button(self, text="Add Users ", bg="black", fg="white", width=10, font=('Times',12), bd=0, command=self.logout)
        self.Add_button.place(x=20, y=200)

        self.Remove_button = tkinter.Button(self, text="Remove Users ", bg="black", fg="white", width=10, font=('Times',12), bd=0, command=self.logout)
        self.Remove_button.place(x=20, y=320)

        self.add_button = tkinter.Button(self, text="Link Student To Courses", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.logout)
        self.add_button.place(x=20, y=360)

        self.remove_button = tkinter.Button(self, text="Unlinking Student from courses", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.logout)
        self.remove_button.place(x=20, y=400)
        
     def view_profile(self):
        self.master.show_profile_frame()
        
     def logout(self):
        self.master.title("Leopard Web") 
        self.master.ShowLoginFrame()

     def SearchClass(self):
        self.master.show_admin_search_Class_Frame()

     def AddCoursetosystem(self):
         self.master.show_admin_add_Class_Frame()

class StudentSearchClassFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tkinter.Label(self, text="Search Course Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.CRN_label = tkinter.Label(self, text="Enter CRN:", font=('Times',12), bg="white")
        self.CRN_label.place(x=20, y=70)
        self.CRN_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.CRN_entry.place(x=20, y=110)

        self.search_button = tkinter.Button(self, text="Search Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.SearchCourse)
        self.search_button.place(x=20, y=151)
               
    def SearchCourse(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
       
        # call the Student class to print data base
        if user.User.search_Course(self,CRN) != False:
            tkinter.messagebox.showinfo("Course info", user.User.search_Course(self,CRN))
        else:
            tkinter.messagebox.showerror("Course info", f"Course Number {CRN} does not exist.")
    def Back(self):
        self.master.show_student_Frame()

class StudentDropCourseFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tkinter.Label(self, text="Drop Course Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.CRN_label = tkinter.Label(self, text="Enter CRN:", font=('Times',12), bg="white")
        self.CRN_label.place(x=20, y=70)
        self.CRN_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.CRN_entry.place(x=20, y=110)

        self.search_button = tkinter.Button(self, text="Drop Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.DropCourse)
        self.search_button.place(x=20, y=151)
               
    def DropCourse(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
        self.student = Student(self.master.user.first_name, self.master.user.last_name, self.master.user.ID)
        if self.student.Remove(CRN) != False:
           tkinter.messagebox.showinfo("Drop Course",f"Successfully Dropped Course {CRN}!")
        else:
             tkinter.messagebox.showerror("Add Course",f"Unable To Drop Course {CRN}!")
        

        
    def Back(self):
        self.master.show_student_Frame()

class StudentAddCourseFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tkinter.Label(self, text="ADD Course Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.CRN_label = tkinter.Label(self, text="Enter CRN:", font=('Times',12), bg="white")
        self.CRN_label.place(x=20, y=70)
        self.CRN_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.CRN_entry.place(x=20, y=110)

        self.search_button = tkinter.Button(self, text="ADD Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddCourse)
        self.search_button.place(x=20, y=151)
               
    def AddCourse(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
       
        # call the Student class to print data base
        self.student = Student(self.master.user.first_name, self.master.user.last_name, self.master.user.ID)
        if self.student.Add_Course(CRN) != False:
             tkinter.messagebox.showinfo("Add Course",f"Successfully Added Course {CRN}!")
        else:
            tkinter.messagebox.showerror("Add Course",f"Unable to add course {CRN}.")


        
    def Back(self):
        self.master.show_student_Frame()

class InstructorSearchClassFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tkinter.Label(self, text="Search Course Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.CRN_label = tkinter.Label(self, text="Enter CRN:", font=('Times',12), bg="white")
        self.CRN_label.place(x=20, y=70)
        self.CRN_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.CRN_entry.place(x=20, y=110)

        self.search_button = tkinter.Button(self, text="Search Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.SearchCourse)
        self.search_button.place(x=20, y=151)
               
    def SearchCourse(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
       
        if user.User.search_Course(self,CRN) != False:
            tkinter.messagebox.showinfo("Course info", user.User.search_Course(self,CRN))
        else:
            tkinter.messagebox.showerror("Course info", f"Course Number {CRN} does not exist.")
        
    def Back(self):
        self.master.show_Instructor_Frame()

class AdminSearchClassFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tkinter.Label(self, text="Search Course Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.CRN_label = tkinter.Label(self, text="Enter CRN:", font=('Times',12), bg="white")
        self.CRN_label.place(x=20, y=70)
        self.CRN_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.CRN_entry.place(x=20, y=110)

        self.search_button = tkinter.Button(self, text="Search Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.SearchCourse)
        self.search_button.place(x=20, y=151)
               
    def SearchCourse(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
       
        if user.User.search_Course(self,CRN) != False:
            tkinter.messagebox.showinfo("Course info", user.User.search_Course(self,CRN))
        else:
            tkinter.messagebox.showerror("Course info", f"Course Number {CRN} does not exist.")
        
    def Back(self):
        self.master.show_Admin_Frame()


class AdminAddClassFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tkinter.Label(self, text="Add Course Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.CRN_label = tkinter.Label(self, text="Enter CRN:", font=('Times',12), bg="white")
        self.CRN_label.place(x=20, y=70)
        self.CRN_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.CRN_entry.place(x=20, y=110)

        self.CRN_label = tkinter.Label(self, text="Enter Course Name:", font=('Times',12), bg="white")
        self.CRN_label.place(x=20, y=150)
        self.CRN_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.CRN_entry.place(x=20, y=190)

        self.CRN_label = tkinter.Label(self, text="Enter Course Day:", font=('Times',12), bg="white")
        self.CRN_label.place(x=20, y=230)
        self.CRN_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.CRN_entry.place(x=20, y=270)

        self.CRN_label = tkinter.Label(self, text="Enter Course Time:", font=('Times',12), bg="white")
        self.CRN_label.place(x=20, y=310)
        self.CRN_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.CRN_entry.place(x=20, y=350)

        self.CRN_label = tkinter.Label(self, text="Enter Instructor Name:", font=('Times',12), bg="white")
        self.CRN_label.place(x=20, y=390)
        self.CRN_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.CRN_entry.place(x=20, y=430)

        self.add_button = tkinter.Button(self, text="Add Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddCourse)
        self.add_button.place(x=20, y=470)
               
    def AddCourse(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
       
        # call the Teacher class to print data base
        Admin.Admin.add_Course(self, CRN)
        
    def Back(self):
        self.master.show_Admin_Frame()


if __name__ == "__main__":
    app = MainPage()
    app.mainloop()