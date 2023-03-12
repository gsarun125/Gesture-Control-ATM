import tkinter as tk

class Window:
    def __init__(self, width, height):
        self.wnd=tk.Tk()
        self.wnd.title("Ahan! ATM")
        #resolution shit
        self.wnd.geometry(str(width)+"x"+str(height))
        #idk, something for layering
        self.wnd.rowconfigure(0, weight=1)
        self.wnd.columnconfigure(0, weight=1)

    def set_title(self, title):
        self.wnd.title(title)

    def get_window(self):
        return self.wnd
    
    def update_gui(self):
        self.wnd.update_idletasks()
        self.wnd.update()