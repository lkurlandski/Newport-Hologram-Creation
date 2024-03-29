### Python libraries ###
# Monitor packages
from screeninfo import get_monitors # Screen Information (screeninfo) is a package to fetch location and size of physical screens.
# Window packages 
from tkinter import Toplevel, Tk, Label # Graphical User Interface (GUI) package
from PIL import Image, ImageTk # Python Imaging Librarier (PIL) package
# Processing packages
import re # Regular Expression (re) is a package to check, if a string contains the specified search pattern.
import numpy as np # Scientific computing package (NumPy)

class SLM_window():

    def __init__(self, master, grating = None):
        ### Monitor controlling 
        # Finds the resolution of all monitors that are connected.
        active_monitors = get_monitors() # "monitor(screenwidth x screenheight + startpixel x + startpixel y)"
        
        for monitor in active_monitors:
            print(monitor)


        # Assign the separated x and y start values to variables
        begin_monitor_horizontal = active_monitors[0].x
        begin_monitor_vertical = active_monitors[0].y
        begin_slm_horizontal = active_monitors[1].x
        begin_slm_vertical = active_monitors[1].y

        width = 1920
        height = 1152

        if not grating:
            array = np.zeros((height, width), dtype = np.uint16)
            image = Image.fromarray(array)
            image = image.convert('L')
            grating = ImageTk.PhotoImage(image)

        # self.image_window = Tk()
        self.image_window = master
        

        # Create a window on the screen of the SLM monitor
        self.window_slm = Toplevel(self.image_window, bg='blue')
        self.window_slm_geometry = str("{:}".format(width) + 'x' + "{:}".format(height) + '+' + "{:}".format(begin_slm_horizontal) + '+' + "{:}".format(begin_slm_vertical))
        
        self.window_slm.geometry(self.window_slm_geometry)
        self.window_slm.overrideredirect(1)
        
        

        # Load the opened image into the window of the SLM monitor
        self.window_slm_label = Label(self.window_slm, image=grating)
        self.window_slm_label.pack()
        print(self.window_slm_geometry, "\n", grating.height(), grating.width())
        # Termination command for the code
        self.window_slm.bind("<Escape>", lambda e: self.window_slm.destroy())
       
    
    def display(self,grating):
        self.window_slm_label.config(image=grating)
        self.window_slm_label.image = grating
        print("display")
        
    def change_text(self, words):
        self.window_slm_label.config(text=words)

    def close_window(self):
        print("pressed")
        self.window_slm.destroy()
        self.window_slm.update()




