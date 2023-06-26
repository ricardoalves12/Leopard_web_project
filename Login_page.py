from tkinter import *
import tkinter 
#pip install pillow
from PIL import ImageTk, Image 
from tkinter import PhotoImage, messagebox


class MainPage(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login") 
        #setting page geometry to the size of the user's screen
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.geometry("%dx%d" % (width_screen, height_screen))
        self.iconphoto(False, PhotoImage(file = 'Images_for_Gui/images.png'))
        # Define image
        bg = ImageTk.PhotoImage(file="Images_for_Gui\wit-background.png")
        #Create canvas
        my_canvas = Canvas(self, width = width_screen, height = height_screen)
        my_canvas.pack(fill="both", expand=True)
        #set image in canvas
        my_canvas.create_image(0,0,image=bg, anchor="nw")
        tkinter.Label(self, image= bg).place(x=0, y=0,relwidth=1, relheight=1)
        self.bind('<Return>', self.resizer)
        self.login_frame = LoginFrame(self)
        self.ShowLoginFrame()
    def resizer(self, e):
        global bg1, resized_bg, new_bg
        # Open Image
        bg1= Image.open("Images_for_Gui\wit-background.png")
        #resize Image
        resized_bg = bg1.resize((e.width, e.height), Image.ANTIALIAS)
        #define the image
        new_bg = ImageTk.PhotoImage(resized_bg)
        #add it back to canvas
        self.my_canvas.create_image(0,0, image=new_bg, anchor='nw')

    def ShowLoginFrame(self):
        #setting page geometry to the size of the user's screen
        width_screen= self.winfo_screenwidth()
        height_screen= self.winfo_screenheight()
        self.login_frame.place(x=((width_screen/2) -200),y=((height_screen/2) -380))

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
        
        self.login_button = tkinter.Button(self, text="Login", bg="red", fg="white", width=17, font=('Times',24), bd=0, command=self.login)
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

if __name__ == "__main__":
    app = MainPage()
    app.mainloop()