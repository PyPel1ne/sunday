import tkinter as tk


class Drag_Drop_Widget(tk.Label):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.bind('<ButtonPress-1>', self.on_button_press)
        self.bind('<ButtonRelease-1>', self.on_button_release)
        self.bind('<B1-Motion>', self.on_button_motion)
        self.is_dragging = False

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.is_dragging = True

    def on_button_release(self, event):
        self.is_dragging = False

    def on_button_motion(self, event):
        if self.is_dragging:
            delta_x = event.x - self.start_x
            delta_y = event.y - self.start_y
            self.place(x=self.winfo_x() + delta_x, y=self.winfo_y() + delta_y)