from tkinter import *

class Entry_Component:
    def entry(self, window, variable, type, row_, collumn_):
        if type == "password":
            entry = Entry(window, textvariable=variable, show = '*', width=15, font=('Arial 15'))
        else:
            entry = Entry(window, textvariable=variable, width=15, font=('Arial 15'))
        entry.grid(row = row_, column = collumn_)

        return entry
    
    def entry_place(self, window, variable, relx_, rely_, width_, disabled = False):
        if disabled == False:
            entry = Entry(window, textvariable=variable, width=width_, font=('Arial 15'), state= DISABLED)
        else:
            entry = Entry(window, textvariable=variable, width=width_, font=('Arial 15'))
        entry.place(relx=relx_, rely=rely_, anchor=CENTER)

        return entry