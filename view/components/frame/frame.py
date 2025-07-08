from tkinter import *


class Frame_Component:    
    def welcome_frame(self, window, background, width, height, relx_, rely_, anchor_ = SW):
        frame_ = Frame(window, bg=background, borderwidth= 5, width= round(window.winfo_screenwidth()) * width, height=round(window.winfo_screenheight() * height))
        frame_.place(relx=relx_, rely=rely_, anchor = anchor_)

        return frame_

    def login_frame(self, window, row_, column_, background = "#dbdbdb"):
        frame_ = Frame(window, bg=background, borderwidth= 5, relief="raised", width= round(window.winfo_screenwidth() * 0.3), height=round(window.winfo_screenheight() * 0.3))
        frame_.grid(row= row_, column= column_)

        return frame_

    def login_form_frame(self, window):

        frame_ = Frame(window, bg = "#dbdbdb")
        frame_.place(relx=0.3, rely=0.5, anchor=W)

        return frame_

    def frame(self, window, relx_, rely_):
        frame_ = Frame(window, bg = "#e1e1e1", width = window.winfo_width(), height = 50)
        frame_.place(relx=relx_, rely=rely_)
        return frame_