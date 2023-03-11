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

class AtmHome:
    def __init__(self, window: Window):
        self.wnd = window.wnd
        self.__create_frames()
        self.__setup_homepg()

    def __create_frames(self):
        self.homepg = tk.Frame(self.wnd)
        self.ftpg = tk.Frame(self.wnd)
        self.bepg = tk.Frame(self.wnd)
        self.mspg = tk.Frame(self.wnd)
        self.fcpg = tk.Frame(self.wnd)
        self.wdpg = tk.Frame(self.wnd)
        self.cdpg = tk.Frame(self.wnd)

        for frame in (self.homepg, self.ftpg, self.bepg, self.mspg, self.fcpg, self.wdpg, self.cdpg):
            frame.grid(row = 0, column=0, sticky='nsew')

    def __setup_homepg(self):
        #lemme set the page colour
        self.homepg.config(background="#FFF87F")
        label = tk.Label(self.homepg, text="AHAN! Bank")
        label.pack()
        # create a button widget
        ftBtn = tk.Button(self.homepg, text="FUND TRANSFER", command=self.__show_frame(self.ftpg))
        ftBtn.place(x=0, y=100, height=60, width=200)

        beBtn = tk.Button(self.homepg, text="BALANCE ENQUIRY", command=self.__show_frame(self.bepg))
        beBtn.place(x=0, y=300, height=60, width=200)

        msBtn = tk.Button(self.homepg, text="MINI STATEMENT", command=self.__show_frame(self.mspg))
        msBtn.place(x=0, y=500, height=60, width=200)

        fcBtn = tk.Button(self.homepg, text="FAST CASH", command=self.__show_frame(self.fcpg))
        fcBtn.place(x=600, y=100, height=60,width=200)

        wdBtn = tk.Button(self.homepg, text="WITHDRAWAL", command=self.__show_frame(self.wdpg))
        wdBtn.place(x=600, y=300, height=60, width=200)

        cdBtn = tk.Button(self.homepg, text="CASH DEPOSIT", command=self.__show_frame(self.cdpg))
        cdBtn.place(x=600, y=500, height=60, width=200)
        
        self.__show_frame(self.homepg)

    #show frame
    def __show_frame(self, frame):
        frame.tkraise()

window = Window(800, 600)
home = AtmHome(window)

while True:
    window.update_gui()