import tkinter as tk
from window import Window

class UI:
    def __init__(self, window: Window):
        self.__wnd=window.wnd
        self.__create_frames()
        self.__setup_pinpg()
        self.__setup_homepg()
        
        self.__show_frame(self.pinpg)

    def __create_frames(self):
        self.hmpg=tk.Frame(self.__wnd)
        self.ftpg=tk.Frame(self.__wnd)
        self.bepg=tk.Frame(self.__wnd)
        self.mspg=tk.Frame(self.__wnd)
        self.fcpg=tk.Frame(self.__wnd)
        self.wdpg=tk.Frame(self.__wnd)
        self.cdpg=tk.Frame(self.__wnd)

        for frame in (self.hmpg, self.ftpg, self.bepg, self.mspg, self.fcpg, self.wdpg, self.cdpg):
            frame.grid(row=0, column=0, sticky='nsew')

    def __setup_pinpg(self):
        self.pinpg = tk.Frame(self.__wnd)

        self.pinpg.grid(row=0, column=0, sticky='nsew')

        # Create a label and entry widget for the PIN
        self.pin_label = tk.Label(self.pinpg, text="Enter your PIN:")
        self.pin_label.pack()

        self.pin_entry = tk.Entry(self.pinpg)
        self.pin_entry.pack() 

        # Create a button widget to submit the PIN
        pin_button = tk.Button(self.pinpg, text="Verify PIN", command=self.__verify_pin)
        pin_button.pack()

        # Create a label widget to display the PIN verification result
        self.pin_result = tk.Label(self.pinpg, text="")
        self.pin_result.pack()

        btn_1 = tk.Button(self.pinpg, text="1", command=lambda: self.__add_to_pin(1))
        btn_1.place(x=0, y=300, height=60, width=150)


        btn_2 = tk.Button(self.pinpg, text="2", command=lambda: self.__add_to_pin(2))
        btn_2.place(x = 200, y = 300, height=60, width=150)

        btn_3 = tk.Button(self.pinpg, text="3", command=lambda: self.__add_to_pin(3))
        btn_3.place(x=400, y=300, height=60, width=150)

        btn_4 = tk.Button(self.pinpg, text="4", command=lambda: self.__add_to_pin(4))
        btn_4.place(x=0, y=400, height=60, width=150)

        btn_5 = tk.Button(self.pinpg, text="5", command=lambda: self.__add_to_pin(5))
        btn_5.place(x=200, y = 400, height = 60,width=150)

        btn_6 = tk.Button(self.pinpg, text="6", command=lambda: self.__add_to_pin(6))
        btn_6.place(x=400, y=400, height=60, width=150)

        btn_7 = tk.Button(self.pinpg, text="7", command=lambda: self.__add_to_pin(7))
        btn_7.place(x=0, y=500, height=60, width=150)

        btn_8 = tk.Button(self.pinpg, text="8", command=lambda: self.__add_to_pin(8))
        btn_8.place(x=200,y=500, height=60,width = 150)

        btn_9 = tk.Button(self.pinpg, text="9", command=lambda: self.__add_to_pin(9))
        btn_9.place(x=400, y=500, height=60, width=150)

        btn_0 = tk.Button(self.pinpg, text="0", command=lambda: self.__add_to_pin(0))
        btn_0.place(x=600, y=400, height=60, width=150)

        btn_enter = tk.Button(self.pinpg, text="ENTER", command=self.__verify_pin)
        btn_enter.place(x=600, y=500, height=60, width=150)

        btn_clear = tk.Button(self.pinpg, text="CLEAR", command=self.__clear_entry)
        btn_clear.place(x=600, y=300, height=60, width=150)

    def __setup_homepg(self):
        #lemme set the page colour
        self.hmpg.config(background="#FFF87F")
        label = tk.Label(self.hmpg, text="AHAN! Bank")
        label.pack()
        # create a button widget
        ftBtn = tk.Button(self.hmpg, text="FUND TRANSFER", command=self.__show_frame(self.ftpg))
        ftBtn.place(x=0, y=100, height=60, width=200)

        beBtn = tk.Button(self.hmpg, text="BALANCE ENQUIRY", command=self.__show_frame(self.bepg))
        beBtn.place(x=0, y=300, height=60, width=200)

        msBtn = tk.Button(self.hmpg, text="MINI STATEMENT", command=self.__show_frame(self.mspg))
        msBtn.place(x=0, y=500, height=60, width=200)

        fcBtn = tk.Button(self.hmpg, text="FAST CASH", command=self.__show_frame(self.fcpg))
        fcBtn.place(x=600, y=100, height=60,width=200)

        wdBtn = tk.Button(self.hmpg, text="WITHDRAWAL", command=self.__show_frame(self.wdpg))
        wdBtn.place(x=600, y=300, height=60, width=200)

        cdBtn = tk.Button(self.hmpg, text="CASH DEPOSIT", command=self.__show_frame(self.cdpg))
        cdBtn.place(x=600, y=500, height=60, width=200)

    #show frame
    def __show_frame(self, frame):
        frame.tkraise()

    def __verify_pin(self):
        # Get the PIN entered by the user
        entered_pin=self.pin_entry.get()

        # Replace this with your own PIN verification logic
        if entered_pin == "1234":
            self.__show_frame(self.hmpg)
        else:
            self.pin_result.config(text="Incorrect PIN!")

            
    def __add_to_pin(self, symbol):
        pin=""
        pin+=str(symbol)
        self.pin_entry.insert(tk.END, pin)

    def __clear_entry(self):
        self.pin_entry.delete(0, tk.END)
        self.pin_result.config(text="")

window = Window(800, 600)
gui = UI(window)

while True:
    window.update_gui()