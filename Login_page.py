from tkinter import *
import tkinter 
#pip install pillow
from PIL import ImageTk, Image 
from tkinter import PhotoImage, messagebox
import sqlite3



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
        self.ShowLoginFrame()


    def ShowLoginFrame(self):
        #setting page geometry to the size of the user's screen
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))
        self.student_frame.place_forget()

    def show_student_Frame(self):
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place_forget()
        self.student_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))


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
        db.execute("SELECT 1 FROM AUTHENTIFY  WHERE USERNAME = ? and PASSWORD = ? ", (username, password))
        result = db.fetchone()
        if result:
            for row in db.execute("SELECT * FROM AUTHENTIFY  WHERE USERNAME = ? and PASSWORD = ? ", (username, password)):
                if row[3] == 'STUDENT':
                    self.master.show_student_Frame()
                elif row[3] == 'ADMIN':
                    self.master.show_home_frame()
                elif row[3] == 'INSTRUCTOR':
                    self.master.show_home_frame()
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
        
        
    def view_profile(self):
        self.master.show_profile_frame()
        
    def logout(self):
        self.master.ShowLoginFrame()

if __name__ == "__main__":
    app = MainPage()
    app.mainloop()