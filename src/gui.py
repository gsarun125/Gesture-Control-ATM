import tkinter as tk
from window import Window

class UI:
    def __init__(self, window: Window):
        self.win=window
        self.__wnd=window.get_window()
        self.__create_frames()
        self.__show_pinpg()

    def __create_frames(self):
        self.ftpg=tk.Frame(self.__wnd)
        self.bepg=tk.Frame(self.__wnd)
        self.mspg=tk.Frame(self.__wnd)
        self.wdpg=tk.Frame(self.__wnd)
        self.cdpg=tk.Frame(self.__wnd)

        for frame in (self.ftpg, self.bepg, self.mspg, self.wdpg, self.cdpg):
            frame.grid(row=0, column=0, sticky='nsew')

    def __show_pinpg(self):
        self.win.set_title("Enter Your PIN Number")
        self.__pinpg = tk.Frame(self.__wnd)

        self.__pinpg.grid(row=0, column=0, sticky='nsew')

        # Create a label and entry widget for the PIN
        self.pin_label = tk.Label(self.__pinpg, text="Enter your PIN:")
        self.pin_label.pack()

        self.pin_entry = tk.Entry(self.__pinpg)
        self.pin_entry.pack() 

        # Create a button widget to submit the PIN
        pin_button = tk.Button(self.__pinpg, text="Verify PIN", command=self.__verify_pin)
        pin_button.pack()

        # Create a label widget to display the PIN verification result
        self.pin_result = tk.Label(self.__pinpg, text="")
        self.pin_result.pack()

        self.__place_keypad(self.__pinpg, self.__add_to_pin, self.__verify_pin, self.__clear_entry)
        self.__show_frame(self.__pinpg)

    def __show_homepg(self):
        self.win.set_title("Home Page")

        self.hmpg=tk.Frame(self.__wnd)
        self.hmpg.grid(row=0, column=0, sticky='nsew')
        self.hmpg.config(background="#FFF87F")  #lemme set the page colour

        label = tk.Label(self.hmpg, text="AHAN! Bank")
        label.config(background="#FFF87F")
        label.pack()
        # create a button widget
        ftBtn = tk.Button(self.hmpg, text="FUND TRANSFER", command=self.__show_frame(self.ftpg))
        ftBtn.place(x=0, y=100, height=60, width=200)

        beBtn = tk.Button(self.hmpg, text="BALANCE ENQUIRY", command=self.__show_balpg)
        beBtn.place(x=0, y=300, height=60, width=200)

        msBtn = tk.Button(self.hmpg, text="MINI STATEMENT", command=self.__show_frame(self.mspg))
        msBtn.place(x=0, y=500, height=60, width=200)

        fcBtn = tk.Button(self.hmpg, text="FAST CASH", command=self.__show_fcpg)
        fcBtn.place(x=600, y=100, height=60,width=200)

        wdBtn = tk.Button(self.hmpg, text="WITHDRAWAL", command=self.__show_frame(self.wdpg))
        wdBtn.place(x=600, y=300, height=60, width=200)

        cdBtn = tk.Button(self.hmpg, text="CASH DEPOSIT", command=self.__show_frame(self.cdpg))
        cdBtn.place(x=600, y=500, height=60, width=200)

        self.__show_frame(self.hmpg)

    def __show_fcpg(self):
        self.fcpg=tk.Frame(self.__wnd)
        self.fcpg.grid(row=0, column=0, sticky='nsew')
        self.fcpg.config(background="#FFF87F") # page colour set pannum

        label = tk.Label(self.fcpg, text = "FAST CASH", font=("Arial", 30))
        label.pack()

        # buttons, so many buttons
        at_5h = tk.Button(self.fcpg, text="500", font=("Arial", 30), command=self.__show_trdpg)
        at_5h.place(x=0, y=50, height=60, width=200)

        at_1t = tk.Button(self.fcpg, text = "1000", font=("Arial", 30), command=self.__show_trdpg)
        at_1t.place(x=0, y=200, height=60, width=200)

        at_2t = tk.Button(self.fcpg, text ="2000",font=("Arial", 30), command=self.__show_trdpg)
        at_2t.place(x=0, y=350, height=60, width=200)
        
        at_3t = tk.Button(self.fcpg, text="3000", font=("Arial", 30), command=self.__show_trdpg)
        at_3t.place(x=0, y=500, height=60, width=200)
        
        at_4t = tk.Button(self.fcpg, text="4000", font=("Arial", 30), command=self.__show_trdpg)
        at_4t.place(x=600, y=50, height=60, width=200)

        at_5t = tk.Button(self.fcpg, text="5000",font=("Arial", 30), command=self.__show_trdpg)
        at_5t.place(x=600, y=200, height=60, width=200)

        at_10t = tk.Button(self.fcpg, text = "10000",font=("Arial", 30), command=self.__show_trdpg)
        at_10t.place(x=600, y=350, height=60, width=200)

        at_20t = tk.Button(self.fcpg, text="20000",font=("Arial", 30), command=self.__show_trdpg)
        at_20t.place(x=600, y=500, height=60, width=200)

        self.__show_frame(self.fcpg)

    def __show_trdpg(self):
        chpg=tk.Frame(self.__wnd)
        chpg.grid(row=0, column=0, sticky='nsew')
        chpg.config(background="#FFF87F") # mela ithe ithu irukke

        self.col_ch=tk.Label(chpg, text='Please wait...', font='times 35')
        self.col_ch.pack(fill='both', expand=True)

        self.tk_ch=tk.Label(chpg, text='', font='times 35')
        self.tk_ch.pack(fill='both', expand=True)

        self.col_ch.after(1500, self.__upd_trdpg)
        
        self.__show_frame(chpg)
    
    def __upd_trdpg(self):
        self.col_ch.config(text='Please Collect Your Cash')
        self.tk_ch.config(text='Thank You For Using Our ATM')

    def __show_balpg(self):
        self.win.set_title("Balance Enquiry")

        self.bepg=tk.Frame(self.__wnd)
        self.bepg.grid(row=0, column=0, sticky='nsew')
        self.bepg.config(background="#FFF87F")  #lemme set the page colour

        bal_lbl=tk.Label(self.bepg, text="Balance")
        bal_lbl.config(background="#FFF87F", font=('Arial', 40, 'bold'))
        bal_lbl.place(relx=0.15, rely=0.10)

        bal=7000
        bal_lbl=tk.Label(self.bepg, text=f"$: {bal}")
        bal_lbl.config(font=('Arial', 20))
        bal_lbl.place(relx=0.40, rely=0.40)

        back_btn=tk.Button(self.bepg, text="<-", command=self.__show_homepg)
        back_btn.place(relx=0, rely=0.90, height=40, width=40)

        self.__show_frame(self.bepg)

    #show frame
    def __show_frame(self, frame):
        frame.tkraise()

    # verifies the PIN entered
    def __verify_pin(self):
        entered_pin=self.pin_entry.get() # Get the PIN entered by the user

        # Replace this with your own PIN verification logic; Should I AG?
        if entered_pin == "1234":
            self.__show_homepg()
        else:
            self.pin_result.config(text="Incorrect PIN!")

    # places the keypad of the ATM on-screen
    def __place_keypad(self, frame, num_click, enter_btn, clear_btn):
        btn_1 = tk.Button(frame, text="1", command=lambda: num_click(1))
        btn_1.place(height=80, width=80)
        btn_1.place(relx=0.30, rely=0.30)

        btn_2 = tk.Button(frame, text="2", command=lambda: num_click(2))
        btn_2.place(height=80, width=80)
        btn_2.place(relx=0.45, rely=0.30)

        btn_3 = tk.Button(frame, text="3", command=lambda: num_click(3))
        btn_3.place(height=80, width=80)
        btn_3.place(relx=0.60, rely=0.30)

        btn_4 = tk.Button(frame, text="4", command=lambda: num_click(4))
        btn_4.place(height=80, width=80)
        btn_4.place(relx=0.30, rely=0.45)

        btn_5 = tk.Button(frame, text="5", command=lambda: num_click(5))
        btn_5.place(height=80, width=80)
        btn_5.place(relx=0.45, rely=0.45)

        btn_6 = tk.Button(frame, text="6", command=lambda: num_click(6))
        btn_6.place(height=80, width=80)
        btn_6.place(relx=0.60, rely=0.45)

        btn_7 = tk.Button(frame, text="7", command=lambda: num_click(7))
        btn_7.place(height=80, width=80)
        btn_7.place(relx=0.30, rely=0.60)

        btn_8 = tk.Button(frame, text="8", command=lambda: num_click(8))
        btn_8.place(height=80, width=80)
        btn_8.place(relx=0.45, rely=0.60)

        btn_9 = tk.Button(frame, text="9", command=lambda: num_click(9))
        btn_9.place(height=80, width=80)
        btn_9.place(relx=0.60, rely=0.60)
        
        btn_clr = tk.Button(frame, text="CLEAR", command=clear_btn)
        btn_clr.place(height=80, width=80)
        btn_clr.place(relx=0.30, rely=0.75)

        btn_0 = tk.Button(frame, text="0", command=lambda: num_click(0))
        btn_0.place(height=80, width=80)
        btn_0.place(relx=0.45, rely=0.75)

        btn_ent = tk.Button(frame, text="ENTER", command=enter_btn)
        btn_ent.place(height=80, width=80)
        btn_ent.place(relx=0.60, rely=0.75)

    def __add_to_pin(self, symbol):
        pin=""
        pin+=str(symbol)
        self.pin_entry.insert(tk.END, pin)

    def __clear_entry(self):
        self.pin_entry.delete(0, tk.END)
        self.pin_result.config(text="")



window=Window(800, 600)
gui=UI(window)
while True:
    window.update_gui()
    if(window.is_closing):
        break