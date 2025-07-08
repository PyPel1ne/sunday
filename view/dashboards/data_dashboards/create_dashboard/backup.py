from functools import partial
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox

#Components
from view.components.button.button import Button_Component
from view.components.entry.entry import Entry_Component
from view.components.label.label import Label_Component
from view.components.frame.frame import Frame_Component
from view.components.drag_n_drop.drag_n_drop import Drag_Drop_Widget

#Layout, dashboards, widgets
from view.layouts.layouts import Dashboard_Layouts
from view.dashboards.widgets import  *

#utils
from app.controllers.utils import get_all_saved_data_source_scripts, destroy_widgets

class Create_Dashboard:
    """! @class New_Data_Source_Dashboard
         @brief Class contains attributes and functions to draw Welcome Dashboard
    """

    def __init__(self, main_frame, top_frame):
        self.layout = Dashboard_Layouts()
        self.label = Label_Component()
        self.entry = Entry_Component()
        self.frame = Frame_Component()
        self.button = Button_Component()
        self.main_frame = main_frame
        self.top_frame = top_frame
        self.window_width = main_frame.winfo_screenwidth()
        self.window_height = main_frame.winfo_screenheight()
        self.relx_frame = 0
        self.rely_frame = 0.15
        self.attributes = []
        self.widget = ""


    def create_dashboard(self, role):

        for widget in self.main_frame.winfo_children():
            widget.destroy()
        for widget in self.top_frame.winfo_children():
            widget.destroy()

        list_of_charts = ["Line chart", "Bar chart", "Numeric value", "Table"]

        name_label = self.label.label(self.top_frame, 'Create data dashboard', 30, "#babfba", 0.5, 0.5)

        drop_area = tk.Frame(self.main_frame, bg='lightgray', width=int(self.main_frame.winfo_width() * 0.995),
                             height=int(self.main_frame.winfo_height() * 0.85))
        drop_area.place(x=self.relx_frame , y=self.rely_frame )

        dnd_widget = Drag_Drop_Widget(self.main_frame, text='Line chart', bg="#babfba",
                                      width=int(self.main_frame.winfo_width() * 0.01),
                                      height=5)
        for chart in list_of_charts:
            dnd_widget = Drag_Drop_Widget(self.main_frame, text=chart, bg="#babfba",
                                          width= int(self.main_frame.winfo_width() * 0.02),
                                          height=5)
            x_start = self.relx_frame + int(self.main_frame.winfo_width() / 3.775) * (list_of_charts.index(chart) + 1) - int(self.window_width * 0.2)
            dnd_widget.place(x= x_start, y=int(self.main_frame.winfo_height() * 0.875))

    def get_widget_under_mouse(self):
        x,y = self.main_frame.winfo_pointerxy()
        self.widget = self.main_frame.winfo_containing(x,y)
        if str(self.widget) == ".!frame4.!label5":
            None

        self.main_frame.after(100, self.get_widget_under_mouse)



