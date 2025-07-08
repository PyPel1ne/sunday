from functools import partial
from tkinter import *
from tkinter import ttk, messagebox
import tkinter as tk

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
        drop_area.place(x=self.relx_frame, y=self.rely_frame)

        dnd_widget = Drag_Drop_Widget(self.main_frame, text='Line chart', bg="#babfba",
                                      width=int(self.main_frame.winfo_width() * 0.01),
                                      height=5)
        for chart in list_of_charts:
            dnd_widget = Drag_Drop_Widget(self.main_frame, text=chart, bg="#babfba",
                                          width=int(self.main_frame.winfo_width() * 0.02),
                                          height=5)
            x_start = self.relx_frame + int(self.main_frame.winfo_width() / 3.775) * (
                        list_of_charts.index(chart) + 1) - int(self.window_width * 0.2)
            dnd_widget.place(x=x_start, y=int(self.main_frame.winfo_height() * 0.875))

            is_dragging = False  # Flag to track if a widget is being dragged

            def on_drag_start(event):
                nonlocal is_dragging
                is_dragging = True
                self.widget = event.widget
                self.widget.startX = event.x
                self.widget.startY = event.y

            def on_drag_motion(event):
                if is_dragging:
                    x, y = event.x_root - self.widget.startX, event.y_root - self.widget.startY
                    self.widget.place(x=x, y=y)

            def on_drag_end(event):
                nonlocal is_dragging
                is_dragging = False
                if self.widget.winfo_rootx() > drop_area.winfo_rootx() and self.widget.winfo_rootx() < (
                        drop_area.winfo_rootx() + drop_area.winfo_width()) \
                        and self.widget.winfo_rooty() > drop_area.winfo_rooty() and self.widget.winfo_rooty() < (
                        drop_area.winfo_rooty() + drop_area.winfo_height()):

                    messagebox.showinfo("Widget Dropped", "Widget dropped in the drop area!")

                    # Destroy the original widget
                    self.widget.destroy()

            for chart in list_of_charts:
                dnd_widget = Label(self.main_frame, text=chart, bg="#babfba",
                                   width=int(self.main_frame.winfo_width() * 0.02), height=5)
                x_start = self.relx_frame + int(self.main_frame.winfo_width() / 3.775) * (
                            list_of_charts.index(chart) + 1) - int(self.window_width * 0.2)
                dnd_widget.place(x=x_start, y=int(self.main_frame.winfo_height() * 0.875))
                dnd_widget.bind("<ButtonPress-1>", on_drag_start)
                dnd_widget.bind("<B1-Motion>", on_drag_motion)
                dnd_widget.bind("<ButtonRelease-1>", on_drag_end)

        def get_widget_under_mouse(self):
            x, y = self.main_frame.winfo_pointerxy()
            self.widget = self.main_frame.winfo_containing(x, y)
            if str(self.widget) == ".!frame4.!label5":
                None

            self.main_frame.after(100, self.get_widget_under_mouse)
