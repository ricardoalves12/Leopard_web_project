from tkinter import *
import tkinter 
#pip install pillow
from PIL import ImageTk, Image 
from tkinter import PhotoImage, messagebox
import sqlite3
import student


class MainPage(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login") 
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
        #self.admin_search_class_frame = AdminSearchClassFrame(self) 
        self.ShowLoginFrame()


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

    def show_student_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.student_search_class_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.Admin_frame.place_forget()
    
    def show_Instructor_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.Instructor_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.Admin_frame.place_forget()
        self.instructor_search_class_frame.place_forget()
        self.student_search_class_frame.place_forget()
     
    def show_Admin_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.Admin_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.student_search_class_frame.place_forget()
        
    def show_student_search_Class_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.instructor_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.Admin_frame.place_forget()

    def show_instructor_search_Class_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place_forget()
        self.student_search_class_frame.place_forget()
        self.Instructor_frame.place_forget()
        self.instructor_search_class_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.Admin_frame.place_forget()

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
        db.execute("SELECT 1 FROM AUTHENTIFY  WHERE USER_NAME = ? and PASSWORD = ? ", (username, password))
        result = db.fetchone()
        if result:
            for row in db.execute("SELECT * FROM AUTHENTIFY  WHERE USER_NAME = ? and PASSWORD = ? ", (username, password)):
                if row[1] == 'STUDENT':
                    self.master.show_student_Frame()
                elif row[1] == 'ADMIN':
                    self.master.show_Admin_Frame()
                elif row[1] == 'INSTRUCTOR':
                    self.master.show_Instructor_Frame()
                else:
                    messagebox.showerror("User type failed", "Invalid User type.")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
                
class StudenthomeFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tkinter.Label(self, text="Student Home Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=30)

        self.logout_button = tkinter.Button(self, text="Search Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.SearchClass)
        self.logout_button.place(x=20, y=70)

        self.logout_button = tkinter.Button(self, text="Add Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=20, y=110)

        self.logout_button = tkinter.Button(self, text="Drop Course", font=('Times',12),  bg="black", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=20, y=150)

        self.logout_button = tkinter.Button(self, text="Print schedule", font=('Times',12),  bg="black", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=20, y=190)
        
        
    def SearchClass(self):
        self.master.show_student_search_Class_Frame()
        
    def logout(self):
        self.master.ShowLoginFrame()

class InstructorhomeFrame(tkinter.Frame):
    def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        
        self.label = tkinter.Label(self, text="Instructor Home Page", font=('Times',12), bg="white")
        self.label.place(x=20, y=30)

        self.logout_button = tkinter.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=30)

        self.PrintSchedule_button = tkinter.Button(self, text="Print Schedule", font=('Times',12),  bg="red", fg="white", bd=0)
        self.PrintSchedule_button.place(x=25, y=100)

        self.PrintClassList_button = tkinter.Button(self, text="Print Class List", font=('Times',12),  bg="red", fg="white", bd=0)
        self.PrintClassList_button.place(x=25, y=150)

        self.SearchCourses_button = tkinter.Button(self, text="Search Courses", font=('Times',12),  bg="red", fg="white", bd=0, command=self.SearchClass)
        self.SearchCourses_button.place(x=25, y=200)

    def logout(self):
        self.master.ShowLoginFrame()

    def SearchClass(self):
        self.master.show_instructor_search_Class_Frame()

class AdminFrame (tkinter.Frame):
     def __init__(self, master):
        super().__init__(master, width = 350, height = 500, bg="white")
        self.label = tkinter.Label(self, text="Admin Main Menu", font=('Times',14), bg="white")
        self.label.place(x=20, y=40)

        self.logout_button = tkinter.Button(self, text="Logout", font=('Times',12),  bg="red", fg="white", bd=0, command=self.logout)
        self.logout_button.place(x=285, y=30)
        
        self.Search_button = tkinter.Button(self, text="Search Courses", bg="red", fg="white", width=12, font=('Times',12), bd=0)
        self.Search_button.place(x=20, y=300)
        
        self.Add_button = tkinter.Button(self, text="Add Courses", bg="red", fg="white", width=10, font=('Times',12), bd=0)
        self.Add_button.place(x=20, y=80)
        
        self.Drop_button = tkinter.Button(self, text="Drop Courses", bg="red", fg="white", width=12, font=('Times',12), bd=0, command=self.logout)
        self.Drop_button.place(x=20, y=100)

        self.Print_button = tkinter.Button(self, text="Print Schedule", bg="red", fg="white", width=13, font=('Times',12), bd=0, command=self.logout)
        self.Print_button.place(x=20, y=180)

        self.Search_button = tkinter.Button(self, text="Search Schedule", bg="red", fg="white", width=13, font=('Times',12), bd=0, command=self.logout)
        self.Search_button.place(x=20, y=200)

        self.Add_button = tkinter.Button(self, text="Add Users ", bg="red", fg="white", width=10, font=('Times',12), bd=0, command=self.logout)
        self.Add_button.place(x=20, y=220)

        self.Remove_button = tkinter.Button(self, text="Remove Users ", bg="red", fg="white", width=10, font=('Times',12), bd=0, command=self.logout)
        self.Remove_button.place(x=20, y=270)

        self.add_button = tkinter.Button(self, text="Add Students from courses ", bg="red", fg="white", width=20, font=('Times',12), bd=0, command=self.logout)
        self.add_button.place(x=20, y=300)

        self.remove_button = tkinter.Button(self, text="Remove Students from courses ", bg="red", fg="white", width=22, font=('Times',12), bd=0, command=self.logout)
        self.remove_button.place(x=20, y=350)


        
     def view_profile(self):
        self.master.show_profile_frame()
        
     def logout(self):
        self.master.ShowLoginFrame()

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
       
        # call the Student class to print data base
        student.Student.search_Course(self,CRN)
        
    def Back(self):
        self.master.show_Instructor_Frame()


if __name__ == "__main__":
    app = MainPage()
    app.mainloop()