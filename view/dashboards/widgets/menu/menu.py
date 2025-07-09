from tkinter import *
from functools import partial
from PIL import Image, ImageTk
import tkinter.messagebox
import time

#Components
from view.components.button.button import Button_Component
from view.components.frame.frame import Frame_Component

from view.dashboards.data_dashboards import New_Data_Source_Dashboard, Change_Data_Source_Dashboard, Create_Dashboard



class Menu_Widget:
    """! @class Menu_Widget
         @brief Class contains attributes and functions to draw Menu
    """

    def __init__(self):
        self.button = Button_Component()
        self.frame = Frame_Component()
        self.image = Image.open("./view/images/back_arrow.png")
        self.img_copy= self.image.copy()
        self.button_image = ImageTk.PhotoImage(self.image)

    def menu_button_pushed(self, old_frame, window_width, return_value, frame, main_frame, top_frame, previous = ""):
        from view.dashboards.system_dashboards import Welcome_Dashboard
        if return_value == 'Back button':
            old_frame.destroy()
            newMenu = self.main_menu_widget(frame, window_width, role_, main_frame, top_frame)
        elif return_value == 'Data loading':
            old_frame.destroy()
            newMenu = self.loading_data_menu_widget(frame, window_width, main_frame, top_frame)
        elif return_value == 'New data source':
            newWindow = New_Data_Source_Dashboard(main_frame, top_frame)
            newWindow.new_data_source_dashboard(role_)
        elif return_value == 'Change data source':
            newWindow = Change_Data_Source_Dashboard(main_frame, top_frame)
            newWindow.pick_data_source_dashboard(role_)
        elif return_value == 'About':
            newWindow = Welcome_Dashboard(main_frame)
            newWindow.welcome_dashboard(role_)
        elif return_value == 'Create dashboard':
            newWindow = Create_Dashboard(main_frame, top_frame)
            newWindow.create_dashboard(role_)

        return None

    def main_menu_widget(self, original_frame, window_width, role, main_frame, top_frame):
        #buttons for menu
        x, y = 0.5, 0.025
        global role_ 
        role_ = role
        new_menu_frame = self.frame.welcome_frame(original_frame, "#babfba", 1, 1, x, 0.145, N)
        new_menu_frame.focus_set()
        perform_command = partial(self.menu_button_pushed)
        if role_ == 'admin':
            button = (self.button.menu_button(new_menu_frame, 'Data loading', x, y, lambda: perform_command(new_menu_frame, window_width, "Data loading", original_frame, main_frame, top_frame), window_width))
            button = (self.button.menu_button(new_menu_frame, 'Create dashboard', x, y + 0.05, lambda: perform_command(new_menu_frame, window_width, "Create dashboard", original_frame, main_frame, top_frame), window_width))
            button = (self.button.menu_button(new_menu_frame, 'Data dashboards', x, y + 0.1, lambda: perform_command(new_menu_frame, window_width, "Data dashboards", original_frame, main_frame, top_frame), window_width))
            button = (self.button.menu_button(new_menu_frame, 'OPC Server', x, y + 0.15, lambda: perform_command(new_menu_frame, window_width, "OPC Server", original_frame, main_frame, top_frame), window_width))
            button = (self.button.menu_button(new_menu_frame, 'About', x, y + 0.20, lambda: perform_command(new_menu_frame, window_width, "About", original_frame, main_frame, top_frame), window_width))
        if role_ == 'view':
            button = (self.button.menu_button(new_menu_frame, 'Data dashboards', x, y, lambda: perform_command(original_frame, window_width, main_frame, top_frame), window_width))
            button = (self.button.menu_button(new_menu_frame, 'About', x, y, lambda: perform_command(original_frame, window_width, main_frame, top_frame), window_width))
            
        return 
    
    def loading_data_menu_widget(self, original_frame, window_width, main_frame, top_frame):
        #buttons for menu
        x, y = 0.5, 0.025
        perform_command = partial(self.menu_button_pushed)
        new_menu_frame1 = self.frame.welcome_frame(original_frame, "#babfba", 1, 1, x, 0.145, N)
        new_menu_frame1.focus_set()

        button = (self.button.menu_button(new_menu_frame1, 'New data source', x, y, lambda: perform_command(new_menu_frame1, window_width, 'New data source', original_frame, main_frame, top_frame, "nds"), window_width))
        button = (self.button.menu_button(new_menu_frame1, 'Change existing', x, y + 0.05, lambda: perform_command(new_menu_frame1, window_width, "Change data source", original_frame, main_frame, top_frame, "che"), window_width))
        button = (self.button.menu_button(new_menu_frame1, 'Back', x, 0.80, lambda: perform_command(new_menu_frame1, window_width, "Back button", original_frame, main_frame, top_frame), window_width))
        
        return