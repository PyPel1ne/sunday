from tkinter import *
from functools import partial

class Button_Component:
    def confirm_button(self, window, label, command_, row_, collumn_):

        button = Button(window, text= label, command= command_, width= 15)
        button.grid(row = row_, column = collumn_)

        return button

    def menu_button(self, frame, label, relx_, rely_, command_, window_width):

        button = Button(frame, text= label, command= command_, font = ("Arial Black", 15))
        width = window_width * 0.01
        button.config(width=(int(width)))
        button.place(relx = relx_, rely = rely_, anchor = CENTER)

        return button

    def random_button(self, frame, label, relx_, rely_, command_, window_width):

        button = Button(frame, text= label, command= command_, font = ("Arial Black", 15))
        button.place(relx = relx_, rely = rely_)

        return button

    def info_button(self, frame, label, relx_, rely_, command_, window_width):

        button = Button(frame, text= label, command= command_, font = ("Arial Black", 10))
        button.place(relx = relx_, rely = rely_)

        return button