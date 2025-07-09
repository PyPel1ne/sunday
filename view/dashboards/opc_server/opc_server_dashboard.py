from functools import partial
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import json

#Backend controller
from app.controllers.opc_server import *

#Components
from view.components.button.button import Button_Component
from view.components.entry.entry import Entry_Component
from view.components.label.label import Label_Component
from view.components.frame.frame import Frame_Component

#Layout, dashboards, widgets
from view.layouts.layouts import Dashboard_Layouts
from view.dashboards.widgets import  *

#utils
from app.controllers.utils import get_all_saved_data_source_scripts, destroy_widgets

class OPC_Server_Dashboard:
    """! @class OPC_Server_Dashboard
         @brief Class contains attributes and functions draw dashboard for opc server
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

    def _create_attribute_frame(self, relx_, rely_):
        if rely_ < 0.9:
            frame = self.frame.frame(self.main_frame, self.relx_frame, rely_)
            self.rely_frame = self.rely_frame + 0.05
            label_opc_name = self.label.label(frame, 'Attribute name', 15, "#e1e1e1", 0.1, 0.5)
            name = StringVar()
            addressEntry = self.entry.entry_place(frame, name, 0.35, 0.5, 25)
            label_opc_adress = self.label.label(frame, 'Attribute address', 20, "#e1e1e1", 0.6, 0.5)
            address = StringVar()
            addressEntry = self.entry.entry_place(frame, address, 0.85, 0.5, 25)
            self.attributes.append([name, address])
        else:
            tkinter.messagebox.showerror("Max attributes",  "You have reached maximum count of attributes per 1 script")
        return None

    def _save_script(self, address, frequency, index_name, attributes, script_name):
        change_saved_script(address, frequency, index_name, attributes, script_name)
        return None        

    def get_widget_under_mouse(self):
        x,y = self.main_frame.winfo_pointerxy()
        self.widget = self.main_frame.winfo_containing(x,y)
        print(str(self.widget))
        if str(self.widget) == ".!frame4.!label5":
            None

        self.main_frame.after(100, self.get_widget_under_mouse)

    def pick_data_source_dashboard(self, role):
        #destroy all widgets from previous screen
        destroy_widgets([self.main_frame, self.top_frame])

        #build new screen
        name_label =  self.label.label(self.top_frame, 'Change data source', 30, "#babfba", 0.5, 0.5)

        label = self.label.label(self.main_frame, 'Choose data source', 15, "#e1e1e1", 0.15, 0.05)
        source_scripts = get_all_saved_data_source_scripts()

        y_pos = 0.1
        for source in source_scripts:
            clickable_label = self.label.clickable_label(self.main_frame, source.replace("_", " ").split(".")[0], 15, "#e1e1e1", 0.05, y_pos)
            clickable_label.bind("<Button-1>", lambda event, source = source: self.change_data_source_dashboard(role, source))
            y_pos = y_pos + 0.05

    def change_data_source_dashboard(self, role, source):
        # destroy all widgets from previous screen
        destroy_widgets([self.main_frame])
        print(source)
        with open(f".\\config\\data_loading_scripts\\{source}\\{source}.json") as json_file:
            info = json.load(json_file)

        label = self.label.label(self.main_frame, 'OPC server address', 15, "#e1e1e1", 0.15, 0.05)
        address = StringVar(value = info['url'])
        addressEntry = self.entry.entry_place(self.main_frame, address, 0.4, 0.05, 30)

        label = self.label.label(self.main_frame, 'Index name', 15, "#e1e1e1", 0.6, 0.05)
        index_name = StringVar(value = info['index_name'])
        addressEntry = self.entry.entry_place(self.main_frame, index_name, 0.8, 0.05, 30)

        label = self.label.label(self.main_frame, 'Script name', 15, "#e1e1e1", 0.6, 0.1)
        script_name = StringVar(value=source)
        addressEntry = self.entry.entry_place(self.main_frame, script_name, 0.8, 0.1, 30)

        label = self.label.label(self.main_frame, 'Data loading frequency', 15, "#e1e1e1", 0.15, 0.1)
        frequency = StringVar(value = info["frequency"])
        addressEntry = self.entry.entry_place(self.main_frame, frequency, 0.4, 0.1, 30)

        label = self.label.label(self.main_frame, 'Nodes', 15, "#e1e1e1", 0.15, 0.2)

        i = 0

        while i < len(info['names']):
            label = self.label.label(self.main_frame, 'Node name', 15, "#e1e1e1", 0.15, 0.3 + i*0.1)
            frequency = StringVar(value=info['names'][i])
            addressEntry = self.entry.entry_place(self.main_frame, frequency, 0.4, 0.3 + i*0.1, 30)

            label = self.label.label(self.main_frame, 'Node address', 15, "#e1e1e1", 0.6, 0.3 + i*0.1)
            index_name = StringVar(value=info['nodes'][i])
            addressEntry = self.entry.entry_place(self.main_frame, index_name, 0.8, 0.3 + i*0.1, 30, "enabled")

            i = i + 1

        change_source = partial(self._save_script)
        add_attribute_button = self.button.random_button(self.main_frame, "Save changes", 0.87, 0.915,
                                                         lambda: change_source(address.get(), frequency.get(),
                                                                               index_name.get(), self.attributes,
                                                                               script_name.get()),
                                                         self.main_frame.winfo_width())