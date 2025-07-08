from tkinter import *
from view.components.frame.frame import Frame_Component

class Dashboard_Layouts:
    """! @class Dashboard_Layouts
         @brief Class contains attributes and functions to create layouts for dashboards
    """
    
    def __init__(self):
        self.frame = Frame_Component()

    def login_layout(window):
        #function to describe layout for window screen
        window.minsize(int(window.winfo_screenwidth() * 0.5), int(window.winfo_screenheight() * 0.5))
        window.title('HDAP')
        window.state('zoomed')
        x, y = 0, 0
        while x < 5:
            window.rowconfigure(x, weight= round(window.winfo_screenwidth() * 0.2))
            x = x + 1

        while y < 5:
            window.columnconfigure(y, weight= round(window.winfo_screenwidth() * 0.2))
            y = y + 1
        
        return window
    
    def general_layout(self, window):
        #function to describe general layout for dashboards
        top_frame = self.frame.welcome_frame(window, "#babfba", 1, 0.1, 0, 0.1)
        menu_frame = self.frame.welcome_frame(window, "#babfba", 0.15, 1, 0, 1)
        main_frame = self.frame.welcome_frame(window, "#e1e1e1", 0.85, 0.85, 0.15, 1)

        return window, top_frame, menu_frame, main_frame