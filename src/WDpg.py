

import tkinter as tk
#import cv2

class WDpg:
    def __init__(self, width, height):
        #window handle created by tinder or whatever tk is
        self.wnd = tk.Tk()
        #resolution shit
        self.wnd.geometry(str(width)+"x"+str(height))
        #idk, something for layering
        self.wnd.rowconfigure(0, weight=1)
        self.wnd.columnconfigure(0, weight=1)

        self.__create_frames()
        self.__setup_wdpg()

    def __create_frames(self):

        #self.homepg = tk.Frame(self.wnd)
        
        self.cashpg = tk.Frame(self.wnd)

        self.wdpg = tk.Frame(self.wnd)
        

        for frame in (self.cashpg,self.wdpg):
            frame.grid(row = 0, column = 0, sticky = 'nsew')
        
        frame1_title=  tk.Label(self.cashpg, text='Please collect your cash', font='times 35')
        frame1_title.pack(fill='both', expand=True)
        
        frame2_title=  tk.Label(self.cashpg, text='Thankyou Using Our ATM ', font='times 35')
        frame2_title.pack(fill='both', expand=True)

    def __setup_wdpg(self):
        #lemme set the page colour
        self.wdpg.config(background="#FFF87F")
        label = tk.Label(self.wdpg, text = "WITHDRAWAL",font=("Arial", 30))
        label.pack()
        # create a button widget
     
        SA_A = tk.Button(self.wdpg, text = "SAVINGS ACCOUNT",font=("Aria", 20), command =lambda: self.__show_frame(self.cashpg))
        SA_A.place(x = 500, y = 200, height = 60, width = 300)

        CU_A = tk.Button(self.wdpg, text = "CURRENT ACCOUNT",font=("Arial", 20), command =lambda: self.__show_frame(self.cashpg))
        CU_A.place(x = 500, y = 300, height = 60,width = 300)

        DE_A = tk.Button(self.wdpg, text = "DEPOSIT ACCOUNT",font=("Arial", 20), command =lambda: self.__show_frame(self.cashpg))
        DE_A.place(x = 500, y = 400, height = 60, width = 300)
        
        self.__show_frame(self.wdpg)

    #show frame
    def __show_frame(self, frame):
        frame.tkraise()

    def show_gui(self):
        self.wnd.update_idletasks()
        self.wnd.update()


home = WDpg(800, 600)

while True:
    home.show_gui()