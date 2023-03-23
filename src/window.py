import tkinter as tk
import win32gui

class Window:
    def __init__(self, width, height):
        self.__wnd=tk.Tk(className='ATMWin')
        self.__wnd.title("Ahan! ATM")
        self.__wnd.geometry(str(width)+"x"+str(height)) #resolution shit
        #idk, something for layering
        self.__wnd.rowconfigure(0, weight=1)
        self.__wnd.columnconfigure(0, weight=1)
        self.is_closing=False
        self.update_gui()
        self.__win=win32gui.FindWindow(None, "Ahan! ATM")
        self.__wnd.protocol('WM_DELETE_WINDOW', self.__set_close)
        self.__wnd.bind("<Configure>", self.__resize)

    def set_title(self, title):
        self.__wnd.title(title)

    def __resize(self, event):
        self.__rect=list(win32gui.GetWindowRect(self.__win))
        print(self.__rect)

    def get_window(self):
        return self.__wnd
    
    def get_winrect(self):
        return self.__rect
    
    def update_gui(self):
        self.__wnd.update_idletasks()
        self.__wnd.update()

    def __set_close(self):
        self.is_closing = True