from functools import partial
from tkinter import *

#Backend controller

#Components
from view.components.button.button import Button_Component
from view.components.entry.entry import Entry_Component
from view.components.label.label import Label_Component
from view.components.frame.frame import Frame_Component

#Layout, dashboards, widgets
from view.layouts.layouts import Dashboard_Layouts
from view.dashboards.widgets import *


class Welcome_Dashboard:
    """! @class Welcome_Dashboard
         @brief Class contains attributes and functions to draw Welcome Dashboard
    """

    def __init__(self, window):
        self.layout = Dashboard_Layouts()
        self.window, self.top_frame, self.menu_frame, self.main_frame = self.layout.general_layout(window)
        self.label = Label_Component()
        self.window_width = self.window.winfo_screenwidth()
        self.window_height = self.window.winfo_screenheight()
        self.menu = Menu_Widget()

    def welcome_dashboard(self, role):
        #label, dashboard name
        label_name = self.label.label(self.top_frame, "Welcome", 20, "#babfba", 0.5, 0.5)
        menu = self.menu.main_menu_widget(self.menu_frame, self.window_width, role, self.main_frame, self.top_frame)
        with open(r'.\config\welcome\welcome.txt') as f:
            lines = f.readlines()
        x, y = 0.5, 0.5
        for line in lines:
            lorem_label = self.label.label(self.main_frame, line, 15, "#e1e1e1", x, y)
            y = y + 0.02