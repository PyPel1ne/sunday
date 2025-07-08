from tkinter import CENTER, E
from tkinter.ttk import Label, Style

class Label_Component:
    def label(self, window, label_, font_, background_ = "#dbdbdb", relx_ = 0.5, rely_ = 0.2):
        login_style = Style()
        login_style.configure("TLabel", font = ('Arial Black', font_))
        label = Label(window, text=label_, style='login_style.TLabel', background= background_)
        label.place(relx=relx_, rely=rely_, anchor = CENTER)

        return label

    def image_label(self, window):
        background_label = Label(window, image=self.background_image, width = round(window.winfo_screenwidth()))
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.bind('<Configure>', self._resize_image(window = window, background_label = background_label))

        return background_label

    def login_label(self, window, label_, row_, collumn_):
        login_style = Style()
        login_style.configure("TLabel", font = ('Arial Black', 20))
        label = Label(window, text=label_, style='login_style.TLabel', background= "#dbdbdb")
        label.grid(row= row_, column= collumn_, sticky= "ew")

        return label

    def clickable_label(self, window, label_, font_, background_ = "#dbdbdb", relx_ = 0.5, rely_ = 0.2):
        login_style = Style()
        login_style.configure("TLabel", font=('Arial Black', font_))
        label = Label(window, text=label_, style='login_style.TLabel', background=background_)
        label.place(relx=relx_, rely=rely_, anchor="w")

        return label