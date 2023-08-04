from tkinter import *
import tkinter 
#pip install pillow
from PIL import ImageTk, Image 
from tkinter import PhotoImage, messagebox
from tkinter.messagebox import *
import sqlite3
import student
import Teacher
import Admin
import user
from user import *

global UserId

class MainPage(tkinter.Tk):
    def __init__(self):
        super().__init__()

        self.user_id = None
        self.user = User()
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
        self.admin_remove_class_frame = AdminRemoveClassFrame(self)
        self.student_remove_course_frame = StudentDropCourseFrame(self)
        self.adminlinkstudenttocourseframe = AdminLinkStudenttoCourseFrame(self)
        self.AdminUnlinkStudentfromCourseFrame = AdminUnlinkStudentfromCourseFrame(self)
        self.AdminRemoveUserFrame = AdminRemoveUserFrame(self)
        self.RemoveStudentfromsystemFrame = RemoveStudentfromsystemFrame(self)
        self.RemoveTeacherfromsystemFrame = RemoveTeacherfromsystemFrame(self)
        self.AdminAddUserFrame = AdminAddUserFrame(self)
        self.AddTeachertosystemFrame = AddTeachertosystemFrame(self)
        self.AddStudenttosystemFrame = AddStudenttosystemFrame(self)
        self.ShowLoginFrame()

    def updateLoginpage(self):
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
        self.admin_remove_class_frame = AdminRemoveClassFrame(self)
        self.student_remove_course_frame = StudentDropCourseFrame(self)
        self.adminlinkstudenttocourseframe = AdminLinkStudenttoCourseFrame(self)
        self.AdminUnlinkStudentfromCourseFrame = AdminUnlinkStudentfromCourseFrame(self)
        self.AdminRemoveUserFrame = AdminRemoveUserFrame(self)
        self.RemoveTeacherfromsystemFrame = RemoveTeacherfromsystemFrame(self)
        self.RemoveStudentfromsystemFrame = RemoveStudentfromsystemFrame(self)
        self.AdminAddUserFrame = AdminAddUserFrame(self)
        self.AddStudenttosystemFrame = AddStudenttosystemFrame(self)



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
        self.adminlinkstudenttocourseframe.place.forget()
        self.AdminUnlinkStudentfromCourseFrame.place.forget()
        self.AdminRemoveUserFrame.place.forget()
        self.RemoveTeacherfromsystemFrame.place.forget()
        self.RemoveStudentfromsystemFrame.place.forget()
        self.AdminAddUserFrame.place.forget()
        self.AddTeachertosystemFrame.place.forget()
        self.AddStudenttosystemFrame.place.forget()
    
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
        self.adminlinkstudenttocourseframe.place.forget()
        self.AdminUnlinkStudentfromCourseFrame.place.forget()
        self.AdminRemoveUserFrame.place.forget()
        self.RemoveTeacherfromsystemFrame.place.forget()
        self.RemoveStudentfromsystemFrame.place.forget()
        self.AdminAddUserFrame.place.forget()
        self.AddTeachertosystemFrame.place.forget()
        self.AddStudenttosystemFrame.place.forget()
     
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
        self.adminlinkstudenttocourseframe.place.forget()
        self.AdminUnlinkStudentfromCourseFrame.place.forget()
        self.AdminRemoveUserFrame.place.forget()
        self.RemoveTeacherfromsystemFrame.place.forget()
        self.RemoveStudentfromsystemFrame.place.forget()
        self.AdminAddUserFrame.place.forget()
        self.AddTeachertosystemFrame.place.forget()
        self.AddStudenttosystemFrame.place.forget()


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
        self.admin_remove_class_frame.place_forget()
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
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.adminlinkstudenttocourseframe.place.forget()
        self.AdminUnlinkStudentfromCourseFrame.place.forget()
        self.AdminRemoveUserFrame.place.forget()
        self.RemoveTeacherfromsystemFrame.place.forget()
        self.RemoveStudentfromsystemFrame.place.forget()
        self.AdminAddUserFrame.place.forget()
        self.AddTeachertosystemFrame.place.forget()
        self.AddStudenttosystemFrame.place.forget()

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
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.adminlinkstudenttocourseframe.place.forget()
        self.AdminUnlinkStudentfromCourseFrame.place.forget()
        self.AdminRemoveUserFrame.place.forget()
        self.RemoveTeacherfromsystemFrame.place.forget()
        self.RemoveStudentfromsystemFrame.place.forget()
        self.AdminAddUserFrame.place.forget()
        self.AddTeachertosystemFrame.place.forget()
        self.AddStudenttosystemFrame.place.forget()

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
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        

    def show_AdminLinkStudenttoCourseFrame(self): #########################
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.adminlinkstudenttocourseframe.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        

    def show_AdminUnlinkStudentfromCourseFrame(self): #########################
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.adminlinkstudenttocourseframe.place.forget() 
        self.AdminRemoveUserFrame.place.forget()
        self.RemoveTeacherfromsystemFrame.place.forget()
        self.RemoveStudentfromsystemFrame.place.forget()
        self.AdminAddUserFrame.place.forget()
        self.AddTeachertosystemFrame.place.forget()
        self.AddStudenttosystemFrame.place.forget()

        
    def show_AdminRemoveUserFrame(self): #########################
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.AdminRemoveUserFrame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.adminlinkstudenttocourseframe.place.forget()
        self.AdminUnlinkStudentfromCourseFrame.place.forget()
        self.RemoveTeacherfromsystemFrame.place.forget()
        self.RemoveStudentfromsystemFrame.place.forget()
        self.AdminAddUserFrame.place.forget()
        self.AddTeachertosystemFrame.place.forget()
        self.AddStudenttosystemFrame.place.forget()

    def show_RemoveTeacherfromsystemFrame(self): #########################
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.RemoveTeacherfromsystemFrame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.adminlinkstudenttocourseframe.place.forget()
        self.AdminUnlinkStudentfromCourseFrame.place.forget()
        self.RemoveStudentfromsystemFrame.place.forget()
        self.AdminAddUserFrame.place.forget()
        self.AddTeachertosystemFrame.place.forget()
        self.AddStudenttosystemFrame.place.forget()

    def show_RemoveStudentfromsystemFrame(self): #########################
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.RemoveStudentfromsystemFrame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.adminlinkstudenttocourseframe.place.forget()
        self.AdminUnlinkStudentfromCourseFrame.place.forget()
        self.AdminAddUserFrame.place.forget()
        self.AddTeachertosystemFrame.place.forget()
        self.AddStudenttosystemFrame.place.forget()

        
    def show_AdminAddUserFrame(self): #########################
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.AdminAddUserFrame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        #self.adminlinkstudenttocourseframe.place.forget()
        #self.AdminUnlinkStudentfromCourseFrame.place.forget()
        #self.AddTeachertosystemFrame.place.forget()
        #self.AddStudenttosystemFrame.place.forget()
        
        
    def show_AddTeachertosystemFrame(self): #########################
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.AddTeachertosystemFrame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.adminlinkstudenttocourseframe.place.forget()
        self.AdminUnlinkStudentfromCourseFrame.place.forget()
        self.AddStudenttosystemFrame.place.forget()

        
        
    def show_AddStudenttosystemFrame(self): #########################
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.AddStudenttosystemFrame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.adminlinkstudenttocourseframe.place.forget()
        self.AdminUnlinkStudentfromCourseFrame.place.forget()   

        

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
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.adminlinkstudenttocourseframe.place.forget()
        self.AdminUnlinkStudentfromCourseFrame.place.forget()
        self.AdminRemoveUserFrame.place.forget()
        self.RemoveTeacherfromsystemFrame.place.forget()
        self.RemoveStudentfromsystemFrame.place.forget()
        self.AdminAddUserFrame.place.forget()
        self.AddTeachertosystemFrame.place.forget()
        self.AddStudenttosystemFrame.place.forget()

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
        self.admin_remove_class_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.student_remove_course_frame.place_forget()
       
    
    def show_admin_remove_Class_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.admin_remove_class_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
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
        self.admin_remove_class_frame.place_forget()
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

        self.label = tkinter.Label(self, text=f"{self.master.user.printInfo()}", font=('Times',12), bg="white")
        self.label.place(x=20, y=20)

        self.logout_button = tkinter.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=20)
       
        self.label = tkinter.Label(self, text="Student Home Page", font=('Times',12), bg="white")
        self.label.place(x=120, y=70)

        self.logout_button = tkinter.Button(self, text="Search Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.SearchClass)
        self.logout_button.place(x=20, y=120)

        self.logout_button = tkinter.Button(self, text="Add Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddCourse)
        self.logout_button.place(x=20, y=160)

        self.logout_button = tkinter.Button(self, text="Drop Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.DropCourse)
        self.logout_button.place(x=20, y=200)

        self.logout_button = tkinter.Button(self, text="Print schedule", font=('Times',12),  bg="black", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=20, y=240)
        
        
    def SearchClass(self):
        tkinter.Listbox(self.master.show_student_search_Class_Frame())
    
    def DropCourse(self):
        self.master.show_student_drop_course_frame()

    def AddCourse(self):
        self.master.show_student_add_Course_Frame()

    def logout(self):
        self.master.ShowLoginFrame()

class InstructorhomeFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tkinter.Label(self, text=f"{self.master.user.printInfo()}", font=('Times',12), bg="white")
        self.label.place(x=20, y=20)

        self.label = tkinter.Label(self, text="Instructor Home Page", font=('Times',12), bg="white")
        self.label.place(x=120, y=70)

        self.logout_button = tkinter.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=30)

        self.PrintSchedule_button = tkinter.Button(self, text="Print Schedule", font=('Times',12),  bg="black", fg="white", bd=0)
        self.PrintSchedule_button.place(x=25, y=120)

        self.PrintClassList_button = tkinter.Button(self, text="Print Class List", font=('Times',12),  bg="black", fg="white", bd=0, command=self.PrintClassList)
        self.PrintClassList_button.place(x=25, y=160)

        self.SearchCourses_button = tkinter.Button(self, text="Search Courses", font=('Times',12),  bg="black", fg="white", bd=0, command=self.SearchClass)
        self.SearchCourses_button.place(x=25, y=200)

    def logout(self):
        self.master.ShowLoginFrame()

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
       
        # call the Teacher class to print data base
        Teacher.Teacher.Print_Class_List(self, CRN,self.master.user_name)
        
    def Back(self):
        self.master.show_Instructor_Frame()
  



class AdminFrame (tkinter.Frame):
     def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text=f"{self.master.user.printInfo()}", font=('Times',12), bg="white")
        self.label.place(x=20, y=20)

        self.label = tkinter.Label(self, text="Admin Main Menu", font=('Times',14), bg="white")
        self.label.place(x=120, y=70)

        self.logout_button = tkinter.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=30)
        
        self.Search_button = tkinter.Button(self, text="Search Courses", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.SearchClass)
        self.Search_button.place(x=20, y=120)
        
        self.Add_button = tkinter.Button(self, text="Add Courses To System", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.AddCoursetosystem)
        self.Add_button.place(x=20, y=160)
        
        self.Drop_button = tkinter.Button(self, text="Remove Courses From System", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.RemoveCoursefromsystem)
        self.Drop_button.place(x=20, y=200)

        self.Add_button = tkinter.Button(self, text="Add Users", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.master.show_AdminAddUserFrame)
        self.Add_button.place(x=20, y=240)

        self.Remove_button = tkinter.Button(self, text="Remove Users ", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.AdminRemoveUserFrame) #
        self.Remove_button.place(x=20, y=280)

        self.add_button = tkinter.Button(self, text="Link Student To Courses", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.AdminLinkStudenttoCourse) #ask for student id
        self.add_button.place(x=20, y=320)

        self.remove_button = tkinter.Button(self, text="Unlinking Student from courses", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.AdminUnlinkStudentfromCourse)  #ask for student id
        self.remove_button.place(x=20, y=360)
        
     def view_profile(self):
        self.master.show_profile_frame()
        
     def logout(self):
        self.master.ShowLoginFrame()

     def SearchClass(self):
        self.master.show_admin_search_Class_Frame()

     def AddCoursetosystem(self):
         self.master.show_admin_add_Class_Frame()

     def RemoveCoursefromsystem(self):
         self.master.show_admin_remove_Class_Frame()

     def AdminAddUserFrame(self):
         self.master.show_admin_add_Class_Frame()

     def AdminRemoveUserFrame(self):
         self.master.show_admin_remove_Class_Frame()

     def AdminLinkStudenttoCourse(self):
         self.master.show_AdminLinkStudenttoCourseFrame()

     def AdminUnlinkStudentfromCourse(self):
         self.master.show_AdminUnlinkStudentfromCourseFrame()

     


         ##########################################3333

class AdminLinkStudenttoCourseFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Link Student To Courses Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.teacher_id_label = tkinter.Label(self, text="Enter ID:", font=('Times',12), bg="white")
        self.teacher_id_label.place(x=20, y=100)
        self.teacher_id_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.teacher_id_entry.place(x=20, y=130)

        self.remove_button = tkinter.Button(self, text="Link Student", font=('Times',12),  bg="black", fg="white", bd=0, command=self.LinkStudent)
        self.remove_button.place(x=20, y=470)
            
    def LinkStudent(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
       
        # call the Teacher class to print data base
        Admin.Admin.link_student(self, CRN)

    def Back(self):
        self.master.show_Admin_Frame()


class AdminUnlinkStudentfromCourseFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Unlink Student From Courses Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.teacher_id_label = tkinter.Label(self, text="Enter ID:", font=('Times',12), bg="white")
        self.teacher_id_label.place(x=20, y=100)
        self.teacher_id_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.teacher_id_entry.place(x=20, y=130)

        self.remove_button = tkinter.Button(self, text="Unlink Student", font=('Times',12),  bg="black", fg="white", bd=0, command=self.UnlinkStudent)
        self.remove_button.place(x=20, y=470)
            
    def UnlinkStudent(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
       
        # call the Teacher class to print data base
        Admin.Admin.unlink_student(self, CRN)

    def Back(self):
        self.master.show_Admin_Frame()



class AdminRemoveUserFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Remove User Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.add_button = tkinter.Button(self, text="Remove Teacher", font=('Times',12),  bg="black", fg="white", bd=0, command=self.RemoveTeacherfromsystem)
        self.add_button.place(x=20, y=120)

        self.add_button = tkinter.Button(self, text="Remove Student", font=('Times',12),  bg="black", fg="white", bd=0, command=self.RemoveStudentfromsystem)
        self.add_button.place(x=20, y=160)

    def Back(self):
        self.master.show_Admin_Frame()

    def RemoveTeacherfromsystem(self):
         self.master.show_AdminRemoveTeacherPage()


    def RemoveStudentfromsystem(self):
         self.master.show_AdminRemoveStudentPage()

class RemoveTeacherfromsystemFrame(tkinter.Frame):
     def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Remove Teacher", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.teacher_id_label = tkinter.Label(self, text="Enter ID:", font=('Times',12), bg="white")
        self.teacher_id_label.place(x=20, y=100)
        self.teacher_id_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.teacher_id_entry.place(x=20, y=130)

        self.remove_button = tkinter.Button(self, text="Remove Teacher", font=('Times',12),  bg="black", fg="white", bd=0, command=self.RemoveTeacher)
        self.remove_button.place(x=20, y=200)
            
     def RemoveTeacher(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
       
        # call the Teacher class to print data base
        Admin.Admin.remove_teacher(self, CRN)

     def Back(self):
        self.master.show_Admin_Frame()

       
class RemoveStudentfromsystemFrame(tkinter.Frame):
     def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Remove Student", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.student_id_label = tkinter.Label(self, text="Enter ID:", font=('Times',12), bg="white")
        self.student_id_label.place(x=20, y=100)
        self.student_id_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.student_id_entry.place(x=20, y=130)

        self.remove_button = tkinter.Button(self, text="Remove Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.RemoveStudent)
        self.remove_button.place(x=20, y=470)
               
     def RemoveStudent(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
       
        # call the  class to print data base
        Admin.Admin.remove_student(self, CRN)

     def Back(self):
        self.master.show_Admin_Frame()

class AdminAddUserFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Add User Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.add_button = tkinter.Button(self, text="Add Teacher", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddTeachertosystem)
        self.add_button.place(x=20, y=120)

        self.add_button = tkinter.Button(self, text="Add Student", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddStudenttosystem)
        self.add_button.place(x=20, y=160)

    def Back(self):
        self.master.show_Admin_Frame()

    def AddTeachertosystem(self):
         self.master.show_AddTeachertosystemFrame()


    def AddStudenttosystem(self):
         self.master.show_AdminAddStudentPage()

class AddTeachertosystemFrame(tkinter.Frame):
     def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Add Teacher", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.teacher_first_name_label = tkinter.Label(self, text="First Name:", font=('Times',12), bg="white")
        self.teacher_first_name_label.place(x=20, y=100)
        self.teacher_first_name_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.teacher_first_name_entry.place(x=20, y=130)

        self.teacher_Last_name_label = tkinter.Label(self, text="Last Name:", font=('Times',12), bg="white")
        self.teacher_Last_name_label.place(x=20, y=170)
        self.teacher_Last_name_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.teacher_Last_name_entry.place(x=20, y=200)

        self.title_label = tkinter.Label(self, text="Title:", font=('Times',12), bg="white")
        self.title_label.place(x=20, y=70)
        self.title_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.title_entry.place(x=20, y=110)

        self.department_label = tkinter.Label(self, text="Department:", font=('Times',12), bg="white")
        self.department_label.place(x=20, y=70)
        self.department_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.department_entry.place(x=20, y=110)

        self.hire_year_label = tkinter.Label(self, text="Enter Hire Year:", font=('Times',12), bg="white")
        self.hire_year_label.place(x=20, y=70)
        self.hire_year_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.hire_year_entry.place(x=20, y=110)

        self.add_button = tkinter.Button(self, text="Add Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddTeacher)
        self.add_button.place(x=20, y=470)
               
     def AddTeacher(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
       
        # call the Teacher class to print data base
        Admin.Admin.add_teacher(self, CRN)

     def Back(self):
        self.master.show_Admin_Frame()

       
class AddStudenttosystemFrame(tkinter.Frame):
     def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Add Student", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.student_first_name_label = tkinter.Label(self, text="First Name:", font=('Times',12), bg="white")
        self.student_first_name_label.place(x=20, y=100)
        self.student_first_name_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.student_first_name_entry.place(x=20, y=130)

        self.student_Last_name_label = tkinter.Label(self, text="Last Name:", font=('Times',12), bg="white")
        self.student_Last_name_label.place(x=20, y=170)
        self.student_Last_name_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.student_Last_name_entry.place(x=20, y=200)

        self.grad_year_label = tkinter.Label(self, text="Enter Grad Year", font=('Times',12), bg="white")
        self.grad_year_label.place(x=20, y=70)
        self.grad_year_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.grad_year_entry.place(x=20, y=110)

        self.major_label = tkinter.Label(self, text="Enter Major:", font=('Times',12), bg="white")
        self.major_label.place(x=20, y=70)
        self.major_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.major_entry.place(x=20, y=110)

        self.add_button = tkinter.Button(self, text="Add Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddStudent)
        self.add_button.place(x=20, y=470)
               
     def AddStudent(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
       
        # call the  class to print data base
        Admin.Admin.add_student(self, CRN)

     def Back(self):
        self.master.show_Admin_Frame()

        ########################################3
class AdminRemoveClassFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

         
        self.label = tkinter.Label(self, text="Remove Course Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.CRN_label = tkinter.Label(self, text="Enter CRN:", font=('Times',12), bg="white")
        self.CRN_label.place(x=20, y=70)
        self.CRN_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.CRN_entry.place(x=20, y=110)

        self.remove_button = tkinter.Button(self, text="Remove Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.RemoveCourse)
        self.remove_button.place(x=20, y=470)

    def RemoveCourse(self):
      CRN = self.CRN_entry.get()
      self.CRN_entry.delete(0, END)
       
        # call the Teacher class to print data base
      Admin.Admin.remove_Course(self, CRN)
        
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
        tkinter.messagebox.showinfo("Course info",user.User.search_Course(self,CRN))
        
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

        self.search_button = tkinter.Button(self, text="Drop Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.SearchCourse)
        self.search_button.place(x=20, y=151)
               
    def SearchCourse(self):
        CRN = self.CRN_entry.get()
        self.CRN_entry.delete(0, END)
       
        # call the Student class to print data base
        student.Student.search_Course(self,CRN)
        
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
        student.Student.search_Course(self,CRN)
        
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
       
        # call the Teacher class to print data base
        tkinter.messagebox.showinfo("Course info",user.User.search_Course(self,CRN))
        
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
       
        # call the Teacher class to print data base
        tkinter.messagebox.showinfo("Course info",user.User.search_Course(self,CRN))
        
    def Back(self):
        self.master.show_Admin_Frame()

if __name__ == "__main__":
    app = MainPage()
    app.mainloop()