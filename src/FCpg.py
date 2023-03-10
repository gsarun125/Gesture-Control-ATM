import tkinter as tk
#import cv2

class FCpg:
    def __init__(self, width, height):
        #window handle created by tinder or whatever tk is
        self.wnd = tk.Tk()
        #resolution shit
        self.wnd.geometry(str(width)+"x"+str(height))
        #idk, something for layering
        self.wnd.rowconfigure(0, weight=1)
        self.wnd.columnconfigure(0, weight=1)

        self.__create_frames()
        self.__setup_fcpg()

    def __create_frames(self):

        #self.homepg = tk.Frame(self.wnd)
        
        self.cashpg = tk.Frame(self.wnd)

        self.fcpg = tk.Frame(self.wnd)
        

        for frame in (self.cashpg,self.fcpg):
            frame.grid(row = 0, column = 0, sticky = 'nsew')
        
        frame1_title=  tk.Label(self.cashpg, text='Please collect your cash', font='times 35')
        frame1_title.pack(fill='both', expand=True)
        
        frame2_title=  tk.Label(self.cashpg, text='Thank you for using our ATM ', font='times 35')
        frame2_title.pack(fill='both', expand=True)

    def __setup_fcpg(self):
        #lemme set the page colour
        self.fcpg.config(background="#FFF87F")
        label = tk.Label(self.fcpg, text = "FAST CASH",font=("Arial", 30))
        label.pack()
        # create a button widget
        At_5h = tk.Button(self.fcpg, text = "500",font=("Arial", 30), command =lambda: self.__show_frame(self.cashpg))
        At_5h.place(x = 0, y = 50, height = 60, width = 200)

        AT_1t = tk.Button(self.fcpg, text = "1000",font=("Arial", 30), command =lambda: self.__show_frame(self.cashpg))
        AT_1t.place(x = 0, y = 200, height = 60, width = 200)

        AT_2t = tk.Button(self.fcpg, text = "2000",font=("Arial", 30), command =lambda: self.__show_frame(self.cashpg))
        AT_2t.place(x = 0, y = 350, height = 60, width = 200)
        
        AT_3t = tk.Button(self.fcpg, text = "3000", font=("Arial", 30), command =lambda: self.__show_frame(self.cashpg))
        AT_3t.place(x = 0, y = 500, height = 60, width = 200)
        
        AT_4t = tk.Button(self.fcpg, text = "4000",font=("Arial", 30), command =lambda: self.__show_frame(self.cashpg))
        AT_4t.place(x = 600, y = 50, height = 60, width = 200)

        AT_5t = tk.Button(self.fcpg, text = "5000",font=("Arial", 30), command =lambda: self.__show_frame(self.cashpg))
        AT_5t.place(x = 600, y = 200, height = 60,width = 200)

        AT_10t = tk.Button(self.fcpg, text = "10000",font=("Arial", 30), command =lambda: self.__show_frame(self.cashpg))
        AT_10t.place(x = 600, y = 350, height = 60, width = 200)

        AT_15t = tk.Button(self.fcpg, text = "20000",font=("Arial", 30), command =lambda: self.__show_frame(self.cashpg))
        AT_15t.place(x = 600, y = 500, height = 60, width = 200)
        
        self.__show_frame(self.fcpg)

    #show frame
    def __show_frame(self, frame):
        frame.tkraise()

    def show_gui(self):
        self.wnd.update_idletasks()
        self.wnd.update()


home = FCpg(800, 600)

while True:
    home.show_gui()