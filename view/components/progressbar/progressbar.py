from tkinter import HORIZONTAL
from tkinter.ttk import Progressbar

class Progressbar_Component:
    def loading_progressbar(self, window):
        loading_progressbar = Progressbar(window,orient=HORIZONTAL,length=200,mode="determinate",takefocus=True,maximum=100)
        loading_progressbar.place(relx=0.5, rely=0.8, anchor = "center")

        return loading_progressbar    