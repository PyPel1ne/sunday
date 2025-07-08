from functools import partial
from tkinter import *
import tkinter.messagebox
from PIL import Image, ImageTk
from time import sleep

#Backend controller
from app.controllers.authenticate import *

#Components
from view.components.button.button import Button_Component
from view.components.entry.entry import Entry_Component
from view.components.label.label import Label_Component
from view.components.frame.frame import Frame_Component
from view.components.progressbar.progressbar import Progressbar_Component
from view.dashboards.system_dashboards import Welcome_Dashboard

#Layout, dashboards
from view.layouts.layouts import Dashboard_Layouts
from view.dashboards.system_dashboards import Welcome_Dashboard


class Login_Dashboard:
    """! @class Login_Dashboard
         @brief Class contains attributes and functions to draw Login Dashboard
    """

    def __init__(self):
        self.window = Tk()
        self.window = Dashboard_Layouts.login_layout(self.window)
        self.login_frame = Frame_Component()
        self.button = Button_Component()
        self.label = Label_Component()
        self.entry = Entry_Component()
        self.progressbar = Progressbar_Component()
        self.window_width = self.window.winfo_screenwidth()
        self.window_height = self.window.winfo_screenheight()

        
        '''self.image = Image.open("./view/images/login_dashboard_bg.png")
        self.img_copy= self.image.copy()
        self.background_image = ImageTk.PhotoImage(self.image)'''

    def check_user(self, username, password, new_login_frame):
        if username.get() == "" or password.get() == "":
            tkinter.messagebox.showerror("Missing credential", "Fill both Username and Password")
        else:
            user, role = authentificate_user(username.get(), password.get())
            if user == True:
                self.window.bind("<Return>", "")
                new_login_frame.destroy()
                loading_progressbar = self.progressbar.loading_progressbar(self.window)
                welcome_label = self.label.label(self.window, f"Welcome {username.get()}!", 50, background_="#eeeeee")
                for i in range(100):                
                    loading_progressbar.step()
                    sleep(0.01)           
                    self.window.update()
                loading_progressbar.destroy()
                welcome_label.destroy()
                newWindow = Welcome_Dashboard(self.window)
                newWindow.welcome_dashboard(role)
            else:
                tkinter.messagebox.showerror("Not authenticated",  "Bad username or password")
        return None

    '''def _resize_image(self,window,background_label):

        new_width = window.winfo_screenwidth()
        new_height = window.winfo_screenheight()

        self.image = self.img_copy.resize((new_width, new_height))

        self.background_image = ImageTk.PhotoImage(self.image)
        background_label.configure(image = self.background_image)
        print(new_width, new_height)'''

    def login_dashboard(self):
        '''#background image
        background_label = Label(self.window, image=self.background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.window.bind('<Resize>', self._resize_image(window = self.window, background_label = background_label))'''

        #frame for user login
        new_login_frame = self.login_frame.login_frame(self.window, 2, 4)
        new_login_frame.focus_set()

        #frame for form for user login
        login_form_frame = self.login_frame.login_form_frame(new_login_frame)

        #username label and text entry box
        usernameLabel = self.label.login_label(login_form_frame, "Username", 0, 0)
        username = StringVar()
        usernameEntry = self.entry.entry(login_form_frame, username, 'username', 0, 1)  

        #password label and password entry box
        passwordLabel = self.label.login_label(login_form_frame, "Password", 1, 0)
        password = StringVar()
        passwordEntry = self.entry.entry(login_form_frame, password, 'password', 1, 1)

        validate_login = partial(self.check_user, username, password, new_login_frame)

        self.window.bind("<Return>", (lambda event: self.check_user(username, password, new_login_frame)))

        #login button
        loginButton = self.button.confirm_button(login_form_frame, "Login", validate_login, 2, 1)

        self.window.mainloop() 
