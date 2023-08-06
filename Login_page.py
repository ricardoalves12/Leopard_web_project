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
from Admin import *
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
        self.iconphoto(False,PhotoImage(file = 'Images_for_Gui\images.png'))
        #setting page geometry to the size of the user's screen        
        self.geometry("%dx%d" % (width_screen, height_screen))
        # Define image
        self.bg = ImageTk.PhotoImage(file="Images_for_Gui\WIT_thumb.png")
        #Create canvas
        my_canvas = Canvas(self, width = width_screen, height = height_screen)
        my_canvas.pack(fill="both", expand=True)

        #set image in canvas
        my_canvas.create_image(0,0,image=self.bg, anchor="nw")

        def resizer(e):
            global bg1, resized_bg, new_bg
            # Open Image
            bg1= Image.open("wit-background.png")
            #resize Image
            resized_bg = bg1.resized((e.width, e.height), Image.ANTIALIAS)
            #define the image
            new_bg = ImageTk.PhotoImage(resized_bg)
            #add it back to canvas
            my_canvas.create_image(0,0, image=new_bg, anchor='nw')
        #create a label
        self.my_label = Label(self, image=self.bg, bg='black').place(x=0, y=0, relwidth=1, relheight=1)
        self.bind('<Return>', resizer)
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
        self.Admin_AddUserFrame = AdminAddUserFrame(self)
        self.Add_TeachertosystemFrame = AddTeachertosystemFrame(self)
        self.AddStudenttosystemFrame = AddStudenttosystemFrame(self)
        self.AdminUnlinkTeacherfromCourseFrame = AdminUnlinkTeacherfromCourseFrame(self)
        self.Admin_linkTeachertoCourse = AdminLinkTeachertoCourseFrame(self)
        self.ShowLoginFrame()

    def reloadFrames(self):
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
        self.admin_remove_class_frame = AdminRemoveClassFrame(self)
        self.student_remove_course_frame = StudentDropCourseFrame(self)
        self.adminlinkstudenttocourseframe = AdminLinkStudenttoCourseFrame(self)
        self.AdminUnlinkStudentfromCourseFrame = AdminUnlinkStudentfromCourseFrame(self)
        self.Admin_AddUserFrame = AdminAddUserFrame(self)
        self.AddStudenttosystemFrame = AddStudenttosystemFrame(self)
        self.Add_TeachertosystemFrame = AddTeachertosystemFrame(self)
        self.Admin_linkTeachertoCourse = AdminLinkTeachertoCourseFrame(self)


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
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
        self.Admin_linkTeachertoCourse.place_forget()
        
       

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
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()       
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
        self.Admin_linkTeachertoCourse.place_forget()
        
    
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
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()       
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
        self.Admin_linkTeachertoCourse.place_forget()
       
     
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
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
        self.Admin_linkTeachertoCourse.place_forget()
        


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
        self.Admin_AddUserFrame.place_forget()
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
        self.Admin_linkTeachertoCourse.place_forget()
       
        
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
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
        self.Admin_linkTeachertoCourse.place_forget()
        

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
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()       
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
        self.Admin_linkTeachertoCourse.place_forget()
       

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
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
        self.Admin_linkTeachertoCourse.place_forget()

    def show_AdminLinkTeachertoCourseFrame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.Admin_linkTeachertoCourse.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
        
        

    def show_AdminUnlinkTeacherfromCourseFrame(self): #########################
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Admin_frame.place_forget()
        self.student_add_course_frame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.adminlinkstudenttocourseframe.place_forget()       
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        
        

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
        self.AdminUnlinkStudentfromCourseFrame.place_forget()
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
        

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
        self.adminlinkstudenttocourseframe.place_forget() 
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
                            
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
        self.Admin_AddUserFrame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
        
        
        
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
        self.Add_TeachertosystemFrame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.admin_add_class_frame.place_forget()
        self.admin_remove_class_frame.place_forget()
        self.student_remove_course_frame.place_forget()
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()
        self.Admin_AddUserFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()

        
        
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
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()   
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
        

        

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
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()       
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
        

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
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()
       
    
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
        self.adminlinkstudenttocourseframe.place_forget()
        self.AdminUnlinkStudentfromCourseFrame.place_forget()
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()      
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()

    
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
        self.adminlinkstudenttocourseframe.place_forget()
        self.student_remove_course_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.AdminUnlinkStudentfromCourseFrame.place_forget()
        self.Admin_AddUserFrame.place_forget()
        self.Add_TeachertosystemFrame.place_forget()
        self.AddStudenttosystemFrame.place_forget()
        self.AdminUnlinkTeacherfromCourseFrame.place_forget()

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
                    self.master.reloadFrames()
                    self.master.show_student_Frame()  
                elif row[1] == 'ADMIN':
                    self.master.user.setUserInfo(str(row[2]), str(row[3]), int(row[0]))
                    self.master.reloadFrames()
                    self.master.show_Admin_Frame()
                elif row[1] == 'INSTRUCTOR':
                    self.master.user.setUserInfo(str(row[2]), str(row[3]), int(row[0]))
                    self.master.reloadFrames()
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
        self.label.place(x=120, y=70)

        self.logout_button = tkinter.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=30)

        self.PrintSchedule_button = tkinter.Button(self, text="Print Schedule", font=('Times',12),  bg="black", fg="white", bd=0, command = self.printSchedule)
        self.PrintSchedule_button.place(x=25, y=100)

        self.PrintClassList_button = tkinter.Button(self, text="Print Class List", font=('Times',12),  bg="black", fg="white", bd=0, command=self.PrintClassList)
        self.PrintClassList_button.place(x=25, y=160)

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
        self.label.place(x=120, y=70)

        self.logout_button = tkinter.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=30)
        
        self.Search_button = tkinter.Button(self, text="Search Courses", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.SearchClass)
        self.Search_button.place(x=20, y=120)
        
        self.Add_button = tkinter.Button(self, text="Add Courses To System", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.AddCoursetosystem)
        self.Add_button.place(x=20, y=160)
        
        self.Drop_button = tkinter.Button(self, text="Remove Courses From System", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.RemoveCoursefromsystem)
        self.Drop_button.place(x=20, y=200)

        self.Add_button = tkinter.Button(self, text="Add Users", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.AdminAddUserFrame)
        self.Add_button.place(x=20, y=240)

        self.add_button = tkinter.Button(self, text="Link Student To Courses", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.AdminLinkStudenttoCourse) #ask for student id
        self.add_button.place(x=20, y=280)

        self.remove_button = tkinter.Button(self, text="Unlinking Student from courses", bg="black", fg="white", width=22, font=('Times',12), bd=0, command=self.AdminUnlinkStudentfromCourse)  #ask for student id
        self.remove_button.place(x=20, y=320)

        self.linkTeacher_button = tkinter.Button(self, text="Link Teacher To courses", bg="black", fg="white", width=22, font=('Times',12), bd=0, command= self.linkTeacher)  #ask for student id
        self.linkTeacher_button.place(x=20, y=360)

        self.linkTeacher_button = tkinter.Button(self, text="unlinking Teacher From courses", bg="black", fg="white", width=22, font=('Times',12), bd=0, command= self.unlinkTeacher)  #ask for student id
        self.linkTeacher_button.place(x=20, y=400)
     def view_profile(self):
        self.master.show_profile_frame()

     def linkTeacher(self):
         self.master.show_AdminLinkTeachertoCourseFrame()
     
     def unlinkTeacher(self):
         self.master.show_AdminUnlinkTeacherfromCourseFrame()
        
     def logout(self):
        self.master.title("Leopard Web") 
        self.master.ShowLoginFrame()

     def SearchClass(self):
        self.master.show_admin_search_Class_Frame()

     def AddCoursetosystem(self):
         self.master.show_admin_add_Class_Frame()

     def RemoveCoursefromsystem(self):
         self.master.show_admin_remove_Class_Frame()

     def AdminAddUserFrame(self):
         self.master.show_AdminAddUserFrame()

     def AdminLinkStudenttoCourse(self):
         self.master.show_AdminLinkStudenttoCourseFrame()

     def AdminUnlinkStudentfromCourse(self):
         self.master.show_AdminUnlinkStudentfromCourseFrame()

class AdminLinkTeachertoCourseFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Link Teacher To Courses Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.name_label = tkinter.Label(self, text="Enter Name:", font=('Times',12), bg="white")
        self.name_label.place(x=20, y=100)
        self.name_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.name_entry.place(x=20, y=130)

        self.crn_label = tkinter.Label(self, text="Enter CRN:", font=('Times',12), bg="white")
        self.crn_label.place(x=20, y=160)
        self.crn_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.crn_entry.place(x=20, y=190)

        self.remove_button = tkinter.Button(self, text="Link Teacher", font=('Times',12),  bg="black", fg="white", bd=0, command=self.LinkTeacher)
        self.remove_button.place(x=20, y=240)
            
    def LinkTeacher(self):
        tname = self.name_entry.get()
        CRN = self.crn_entry.get()
        self.crn_entry.delete(0, END)
        self.name_entry.delete(0, END)
       
        self.Admin = Admin(self.master.user.first_name, self.master.user.last_name, self.master.user.ID)
        if self.Admin.link_T(CRN,tname) != False:
            messagebox.showinfo("Link Teacher to course", f"Succefully Linked teacher to course {CRN}.")
        else:
            messagebox.showerror("Link Teacher to course", f"Unable to Link teacher to course {CRN}. Make sure CRN exists.")

    def Back(self):
        self.master.show_Admin_Frame()


class AdminUnlinkTeacherfromCourseFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Unlink Teacher From Courses Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.crn_label = tkinter.Label(self, text="Enter CRN:", font=('Times',12), bg="white")
        self.crn_label.place(x=20, y=100)
        self.crn_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.crn_entry.place(x=20, y=130)

        self.name_label = tkinter.Label(self, text="Enter Teacher Name:", font=('Times',12), bg="white")
        self.name_label.place(x=20, y=160)
        self.name_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.name_entry.place(x=20, y=190)

        self.remove_button = tkinter.Button(self, text="Unlink Teacher", font=('Times',12),  bg="black", fg="white", bd=0, command=self.UnlinkTeacher)
        self.remove_button.place(x=20, y=230)
            
    def UnlinkTeacher(self):
        CRN = self.crn_entry.get()
        Tname = self.name_entry.get()
        self.crn_entry.delete(0, END)
        self.name_entry.delete(0, END)
       
        self.Admin = Admin(self.master.user.first_name, self.master.user.last_name, self.master.user.ID)
        if self.Admin.unlink_T(CRN, Tname) != False:
            messagebox.showinfo("Unlinking Teacher", f"Succefully unlinked teacher for course {CRN}")
        else:
            messagebox.showerror("Unlinking Teacher", f"Unable to unlinked teacher for course {CRN}. Make sure teacher is teaching course and crn exists.")

    def Back(self):
        self.master.show_Admin_Frame()
        ##############

class AdminLinkStudenttoCourseFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Link Student To Courses Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.crn_label = tkinter.Label(self, text="Enter CRN:", font=('Times',12), bg="white")
        self.crn_label.place(x=20, y=100)
        self.crn_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.crn_entry.place(x=20, y=130)

        self.id_label = tkinter.Label(self, text="Enter Student ID:", font=('Times',12), bg="white")
        self.id_label.place(x=20, y=160)
        self.id_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.id_entry.place(x=20, y=190)

        self.remove_button = tkinter.Button(self, text="Link Student", font=('Times',12),  bg="black", fg="white", bd=0, command=self.LinkStudent)
        self.remove_button.place(x=20, y=230)
            
    def LinkStudent(self):
        CRN = self.crn_entry.get()
        studentId = self.id_entry.get()
        self.crn_entry.delete(0, END)
        self.id_entry.delete(0, END)
        self.Admin = Admin(self.master.user.first_name, self.master.user.last_name, self.master.user.ID)
        if self.Admin.Link_S(CRN,studentId) != False:
            messagebox.showinfo("Link Student to Course", f"Succefully Linked Student to course {CRN}.")
        else:
            messagebox.showerror("Link Student to Course", f"Unable to link Student to course {CRN}. Please check if CRN exist and if no conflicts exist.")


    def Back(self):
        self.master.show_Admin_Frame()


class AdminUnlinkStudentfromCourseFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")

        self.label = tkinter.Label(self, text="Unlink Student From Courses Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.crn_label = tkinter.Label(self, text="Enter CRN:", font=('Times',12), bg="white")
        self.crn_label.place(x=20, y=100)
        self.crn_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.crn_entry.place(x=20, y=130)

        self.id_label = tkinter.Label(self, text="Enter Student ID:", font=('Times',12), bg="white")
        self.id_label.place(x=20, y=160)
        self.id_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), bg="white")
        self.id_entry.place(x=20, y=190)

        self.remove_button = tkinter.Button(self, text="Unlink Student", font=('Times',12),  bg="black", fg="white", bd=0, command=self.UnlinkStudent)
        self.remove_button.place(x=20, y=230)
            
    def UnlinkStudent(self):
         crn = self.crn_entry.get()
         ID = self.id_entry.get()
         self.crn_entry.delete(0, END)
         self.id_entry.delete(0, END)
         self.Admin = Admin(self.master.user.first_name, self.master.user.last_name, self.master.user.ID)
         if self.Admin.unlink_S(crn,ID) != False:
             messagebox.showinfo("Unlinking Student form Course",f"Succefully unlinked student from Course {crn}")
         else:
             messagebox.showerror("Unlinking Student from Course",f"Unable to unlink student from Course {crn} check if course exist and if student is taking course")

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
         self.master.show_AddStudenttosystemFrame()

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
        self.title_label.place(x=20, y=230)
        self.title_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.title_entry.place(x=20, y=260)

        self.department_label = tkinter.Label(self, text="Department:", font=('Times',12), bg="white")
        self.department_label.place(x=20, y=290)
        self.department_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.department_entry.place(x=20, y=320)

        self.hire_year_label = tkinter.Label(self, text="Enter Hire Year:", font=('Times',12), bg="white")
        self.hire_year_label.place(x=20, y=350)
        self.hire_year_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.hire_year_entry.place(x=20, y=380)

        self.add_button = tkinter.Button(self, text="Add Teacher", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddTeacher)
        self.add_button.place(x=20, y=420)
               
     def AddTeacher(self):
        firstname = self.teacher_first_name_entry.get()
        lastname = self.teacher_Last_name_entry.get()
        title = self.title_entry.get()
        department = self.department_entry.get()
        hire = self.hire_year_entry.get()
        self.teacher_first_name_entry.delete(0, END)
        self.teacher_Last_name_entry.delete(0, END)
        self.title_entry.delete(0, END)
        self.department_entry.delete(0, END)
        self.hire_year_entry.delete(0, END)
       
        self.Admin = Admin(self.master.user.first_name, self.master.user.last_name, self.master.user.ID)
        if self.Admin.Add_Teacher(firstname,lastname,title,hire,department) != False:
            messagebox.showinfo("Admin add Teacher", f"Added Teacher {firstname},{lastname}")
        else:
            messagebox.showerror("Admin add Teacher", "Unable to add teacher, make sure all the box are completed.")

     def Back(self):
        self.master.show_AdminAddUserFrame()

       
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
        self.grad_year_label.place(x=20, y=230)
        self.grad_year_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.grad_year_entry.place(x=20, y=260)

        self.major_label = tkinter.Label(self, text="Enter Major:", font=('Times',12), bg="white")
        self.major_label.place(x=20, y=290)
        self.major_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.major_entry.place(x=20, y=320)

        self.add_button = tkinter.Button(self, text="Add Student", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddStudent)
        self.add_button.place(x=20, y=350)
               
     def AddStudent(self):
        firstname = self.student_first_name_entry.get()
        lastname = self.student_Last_name_entry.get()
        gradyear = self.grad_year_entry.get()
        major = self.major_entry.get()
        self.student_first_name_entry.delete(0, END)
        self.student_Last_name_entry.delete(0, END)
        self.grad_year_entry.delete(0, END)
        self.major_entry.delete(0, END)
        self.Admin = Admin(self.master.user.first_name, self.master.user.last_name, self.master.user.ID)
        if self.Admin.Add_student(firstname,lastname, gradyear, major) != False:
            messagebox.showinfo("Admin add Student", f"Succefully added {firstname},{lastname} to the system")
        else:
            messagebox.showerror("Admin add Student", "Unable to add student to the system, make sure all the boxes are completed")

     def Back(self):
        self.master.show_AdminAddUserFrame()

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
        self.remove_button.place(x=20, y=150)

    def RemoveCourse(self):
      CRN = self.CRN_entry.get()
      self.CRN_entry.delete(0, END)
      self.Admin = Admin(self.master.user.first_name, self.master.user.last_name, self.master.user.ID)
      if self.Admin.Remove_Course(CRN) != False:
          messagebox.showinfo("Admin Remove course",f"Succefully removed course {CRN}")
      else:
          messagebox.showerror("Admin Remove course",f"Unable to remove course {CRN}, make sure the course CRN exist")
 
        
    def Back(self):
        self.master.show_Admin_Frame()

class AdminAddClassFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 650, bg="white")
        
        self.label = tkinter.Label(self, text="Add Course Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Back", font=('Times',12),  bg="red", fg="white", bd=0, command=self.Back)
        self.logout_button.place(x=285, y=30)

        self.CRN_label = tkinter.Label(self, text="Enter CRN:", font=('Times',12), bg="white")
        self.CRN_label.place(x=20, y=70)
        self.CRN_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.CRN_entry.place(x=20, y=110)

        self.Course_label = tkinter.Label(self, text="Enter Course Name:", font=('Times',12), bg="white")
        self.Course_label.place(x=20, y=150)
        self.Course_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.Course_entry.place(x=20, y=190)

        self.startDay_label = tkinter.Label(self, text="Enter Course First week Day:", font=('Times',12), bg="white")
        self.startDay_label.place(x=20, y=230)
        self.startDay_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.startDay_entry.place(x=20, y=270)

        self.endDay_label = tkinter.Label(self, text="Enter Course second week Day:", font=('Times',12), bg="white")
        self.endDay_label.place(x=20, y=310)
        self.endDay_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.endDay_entry.place(x=20, y=340)

        self.startTime_label = tkinter.Label(self, text="Enter Start Time:", font=('Times',12), bg="white")
        self.startTime_label.place(x=20, y=380)
        self.startTime_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.startTime_entry.place(x=20, y=420)

        self.endTime_label = tkinter.Label(self, text="Enter End Time:", font=('Times',12), bg="white")
        self.endTime_label.place(x=20, y=460)
        self.endTime_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.endTime_entry.place(x=20, y=490)

        self.Instructor_label = tkinter.Label(self, text="Enter Instructor Name:", font=('Times',12), bg="white")
        self.Instructor_label.place(x=20, y=530)
        self.Instructor_entry = tkinter.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.Instructor_entry.place(x=20, y=560)

        self.add_button = tkinter.Button(self, text="Add Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.AddCourse)
        self.add_button.place(x=20, y=590)
               
    def AddCourse(self):
        CRN = self.CRN_entry.get()
        course = self.Course_entry.get()
        instructor = self.Instructor_entry.get()
        startday = self.startDay_entry.get()
        endday =  self.endDay_entry.get()
        starttime = self.startTime_entry.get()
        endtime = self.endTime_entry.get()
        self.CRN_entry.delete(0, END)
        self.Course_entry.delete(0, END)
        self.Instructor_entry.delete(0, END)
        self.startDay_entry.delete(0, END)
        self.endDay_entry.delete(0, END)
        self.startTime_entry.delete(0, END)
        self.endTime_entry.delete(0, END)
       
        # call the Teacher class to print data base
        self.Admin = Admin(self.master.user.first_name, self.master.user.last_name, self.master.user.ID)
        if self.Admin.Add_Course(CRN, course, startday, endday, starttime, endtime, instructor) != False:
            messagebox.showinfo("Add Course To system", f"Succefully added course")
        else:
            messagebox.showerror("Add Course To system", f"Unable to add course to system. Make sure all the atributes are completed.")
        
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
            tkinter.messagebox.showerror("Add Course",f"Unable to add course {CRN}. Please check if no course conflicts in you schedule or Crn not exist")


        
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

if __name__ == "__main__":
    app = MainPage()
    app.mainloop()