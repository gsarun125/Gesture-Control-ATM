import tkinter as tk

class Window:
    def __init__(self, width, height):
        self.__wnd=tk.Tk()
        self.__wnd.title("Ahan! ATM")
        #resolution shit
        self.__wnd.geometry(str(width)+"x"+str(height))
        #idk, something for layering
        self.__wnd.rowconfigure(0, weight=1)
        self.__wnd.columnconfigure(0, weight=1)
        self.is_closing = False
        self.__wnd.protocol('WM_DELETE_WINDOW', self.__set_close)

    def set_title(self, title):
        self.__wnd.title(title)

    def get_window(self):
        return self.__wnd
    
    def update_gui(self):
        self.__wnd.update_idletasks()
        self.__wnd.update()

    def __set_close(self):
        self.is_closing = True