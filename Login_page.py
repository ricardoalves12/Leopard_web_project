from tkinter import *
import tkinter as tk
from tkinter import PhotoImage, messagebox


class MainPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login") 
        #setting page geometry to the size of the user's screen
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.geometry("%dx%d" % (width_screen, height_screen))
        self.iconphoto(False, PhotoImage(file = 'Images_for_Gui/images.png'))
        self.login_frame = LoginFrame(self, width = 350, height = 500, bg="white")
        self.ShowLoginFrame()

    def ShowLoginFrame(self):
        #setting page geometry to the size of the user's screen
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))

class LoginFrame (tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        
        self.label = tk.Label(self, text="Enter Username & Password", font=('Times',14), bg="white")
        self.label.place(x=20, y=40)
        
        self.username_label = tk.Label(self, text="Username:", font=('Times',12), bg="white")
        self.username_label.place(x=20, y=80)
        self.username_entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14))
        self.username_entry.place(x=20, y=110)
        
        self.password_label = tk.Label(self, text="Password:", font=('Times',12), bg="white")
        self.password_label.place(x=20, y=140)
        self.password_entry = tk.Entry(self, highlightbackground='black', highlightthickness=1,bd=0,width=34,font=('Times',14), show="*")
        self.password_entry.place(x=20, y=1700)
        
        self.login_button = tk.Button(self, ext="Login", bg="red", fg="white", width=17, font=('Times',24), bd=0, command=self.login)
        self.login_button.place(x=20, y=210)
    def login(self):
        username = self.username_entry.get() 
        password = self.password_entry.get()
        
        # Perform login validation here (e.g., check against a database)
        # For simplicity, we'll use a dummy check
        if username == "admin" and password == "password":
            self.master.show_home_frame()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

if __name__ == "main":
    app = MainPage()
    app.mainloop()