from functools import partial
from tkinter import *
from tkinter import ttk
import tkinter.messagebox

#Backend controller
from app.controllers.create_new_data_source import *

#Components
from view.components.button.button import Button_Component
from view.components.entry.entry import Entry_Component
from view.components.label.label import Label_Component
from view.components.frame.frame import Frame_Component

#Layout, dashboards, widgets
from view.layouts.layouts import Dashboard_Layouts
from view.dashboards.widgets import  *

class New_Data_Source_Dashboard:
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

    def _create_attribute_frame(self, relx_, rely_):
        if rely_ < 0.9:
            frame = self.frame.frame(self.main_frame, self.relx_frame, rely_)
            self.rely_frame = self.rely_frame + 0.05
            label_opc_name = self.label.label(frame, 'Attribute name', 15, "#e1e1e1", 0.1, 0.5)
            name = StringVar()
            addressEntry = self.entry.entry_place(frame, name, 0.35, 0.5, 25, "enabled")
            label_opc_adress = self.label.label(frame, 'Attribute address', 20, "#e1e1e1", 0.6, 0.5)
            address = StringVar()
            addressEntry = self.entry.entry_place(frame, address, 0.85, 0.5, 25, "enabled")
            self.attributes.append([name, address])
        else:
            tkinter.messagebox.showerror("Max attributes",  "You have reached maximum count of attributes per 1 script")
        return None

    def _save_script(self, address, frequency, index_name, attributes, script_name):
        OK = False
        if address.lower().startswith('opc.tcp://') and len(address.split('.')) == 5 and len(address.split(':')) == 3:
            try:
                if index_name != "":
                    if script_name != "":
                        for attr in attributes:
                            if attr[0].get() != "" and attr[1].get().startswith("ns=") and len(attr[1].get().split(";")) >= 2 and len(attr[1].get().split("=")) >= 3:
                                OK = True
                            else:
                                OK = False
                                tkinter.messagebox.showerror("Bad input format",  "Check attributes. For more information click on INFO.")
                                break
                        if OK:
                            if tkinter.messagebox.askyesno("Service install", "Do you want to install new script as service?"):
                                save_new_script(address, frequency, index_name, attributes, script_name, True)
                            else:
                                save_new_script(address, frequency, index_name, attributes, script_name, False)
                    else: #script name
                        tkinter.messagebox.showerror("Bad input format",  "Check script name. For more information click on INFO.")
                else: #index name
                    tkinter.messagebox.showerror("Bad input format",  "Check index name. For more information click on INFO.")
            except: #frequency
                tkinter.messagebox.showerror("Bad input format",  "Check frequency. For more information click on INFO.")
        else: #address
            tkinter.messagebox.showerror("Bad input format",  "Check OPC TCP address. For more information click on INFO.")
        return None

    def _open_info_window(self):
        tkinter.messagebox.showinfo("New Data Source", \
"""
This window serves to set up new data source. All of the attributes listed below have to defined and in correct format. In one script you can add up to 15 attributes. 

OPC server address: address opc.tcp://address:port

Index name: name of index you want to save data in ES

Data loading frequency: frequency of data loading in ms (e.g. every 300 ms - 0.3s)

Script name: you can access settings to this script in "Change existing" under this name and delete it in "Delete Data Source"

Attribute name: what should the attribute be called

Attribute address: address to load attribute from (e.g. ns=1;s=name)
                
            """)
        return None        

    def get_widget_under_mouse(self):
        x,y = self.main_frame.winfo_pointerxy()
        self.widget = self.main_frame.winfo_containing(x,y)
        print(str(self.widget))
        if str(self.widget) == ".!frame4.!label5":
            None

        self.main_frame.after(100, self.get_widget_under_mouse)

    def new_data_source_dashboard(self, role):
        #label, dashboard name
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        for widget in self.top_frame.winfo_children():
            widget.destroy()
        
        name_label = self.label.label(self.top_frame, 'New data source', 30, "#babfba", 0.5, 0.5)

        label = self.label.label(self.main_frame, 'OPC server address', 15, "#e1e1e1", 0.15, 0.05)
        address = StringVar()
        addressEntry = self.entry.entry_place(self.main_frame, address, 0.4, 0.05, 30, "enabled")

        label = self.label.label(self.main_frame, 'Index name', 15, "#e1e1e1", 0.6, 0.05)
        index_name = StringVar()
        addressEntry = self.entry.entry_place(self.main_frame, index_name, 0.8, 0.05, 30, "enabled")

        label = self.label.label(self.main_frame, 'Data loading frequency', 15, "#e1e1e1", 0.15, 0.1)
        frequency = StringVar()
        addressEntry = self.entry.entry_place(self.main_frame, frequency, 0.4, 0.1, 30, "enabled")

        label = self.label.label(self.main_frame, 'Script name', 15, "#e1e1e1", 0.6, 0.1)
        script_name = StringVar()
        addressEntry = self.entry.entry_place(self.main_frame, script_name, 0.8, 0.1, 30, "enabled")

        attribute = self._create_attribute_frame(self.relx_frame, self.rely_frame)

        add_attribute = partial(self._create_attribute_frame)
        add_attribute_button = self.button.random_button(self.main_frame, "Add attribute", 0.03, 0.915,
                        lambda: add_attribute(self.relx_frame, self.rely_frame), self.main_frame.winfo_width())
        
        new_data_source = partial(self._save_script)
        add_attribute_button = self.button.random_button(self.main_frame, "Save script", 0.87, 0.915,
                        lambda: new_data_source(address.get(), frequency.get(), index_name.get(), self.attributes, script_name.get()), self.main_frame.winfo_width())

        open_info_window = partial(self._open_info_window)
        info_button = self.button.info_button(self.main_frame, "INFO", 0.95, 0.01,
                        lambda: open_info_window(), self.main_frame.winfo_width())

        #self.get_widget_under_mouse()