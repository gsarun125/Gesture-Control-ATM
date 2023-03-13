import tkinter as tk
from window import Window
from bacc import BankAcc

DLY_MS = 1500
BCK_YELLOW = "#FFF87F"

class Atm:
    def __init__(self, window: Window):
        self.__acc=BankAcc()
        self.__win=window
        self.__wnd=window.get_window()
        self.__create_frames()
        self.__show_pinpg()

    def __set_title(self, title):
        self.__win.set_title(title)

    # deprecated; to be removed...
    def __create_frames(self):
        self.ftpg=tk.Frame(self.__wnd)
        self.mspg=tk.Frame(self.__wnd)
        self.cdpg=tk.Frame(self.__wnd)

        for frame in (self.ftpg, self.mspg, self.cdpg):
            frame.grid(row=0, column=0, sticky='nsew')

    # pin input & verification page
    def __show_pinpg(self):
        self.__set_title("Enter Your PIN Number")
        self.__pinpg = tk.Frame(self.__wnd, background=BCK_YELLOW)

        self.__pinpg.grid(row=0, column=0, sticky='nsew')

        self.pin_label = tk.Label(self.__pinpg, text="Enter your PIN:", background=BCK_YELLOW)
        self.pin_label.pack()

        self.inp_entry = tk.Entry(self.__pinpg, font=('Arial', 14, 'bold'), justify='center')
        self.inp_entry.place(relx=0.40, rely=0.10, width=175, height=50)

        # displays the PIN verification result
        self.inp_result = tk.Label(self.__pinpg, text="", background=BCK_YELLOW)
        self.inp_result.pack()

        self.__place_keypad(self.__pinpg, self.__add_to_box, self.__verify_pin, self.__clear_entry)
        self.__show_frame(self.__pinpg)

    # verifies the PIN entered
    def __verify_pin(self):
        entered_pin=int(self.inp_entry.get()) # Get the PIN entered by the user

        # Replace this with your own PIN verification logic; Should I AG?
        if entered_pin == self.__acc.pnnum:
            self.__show_homepg()
        else:
            self.inp_result.config(text="Incorrect PIN!")

    # home page
    def __show_homepg(self):
        self.__set_title("Home Page")

        self.hmpg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        self.hmpg.grid(row=0, column=0, sticky='nsew')

        titl = tk.Label(self.hmpg, text="AHAN! Bank", background=BCK_YELLOW)
        titl.pack()
        # create a button widget
        ftBtn = tk.Button(self.hmpg, text="FUND TRANSFER", command=self.__show_frame(self.ftpg))
        ftBtn.place(x=0, y=100, height=60, width=200)

        beBtn = tk.Button(self.hmpg, text="BALANCE ENQUIRY", command=self.__show_balpg)
        beBtn.place(x=0, y=300, height=60, width=200)

        msBtn = tk.Button(self.hmpg, text="MINI STATEMENT", command=self.__show_frame(self.mspg))
        msBtn.place(x=0, y=500, height=60, width=200)

        fcBtn = tk.Button(self.hmpg, text="FAST CASH", command=self.__show_fcpg)
        fcBtn.place(x=600, y=100, height=60,width=200)

        wdBtn = tk.Button(self.hmpg, text="WITHDRAWAL", command=self.__show_wdpg)
        wdBtn.place(x=600, y=300, height=60, width=200)

        cdBtn = tk.Button(self.hmpg, text="CASH DEPOSIT", command=self.__show_cdpg)
        cdBtn.place(x=600, y=500, height=60, width=200)

        self.__show_frame(self.hmpg)

    # withdrawl page
    def __show_wdpg(self):
        self.__set_title("Withdrawal")

        self.wdpg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        self.wdpg.grid(row=0, column=0, sticky='nsew')

        wdrl = tk.Label(self.wdpg, text="WITHDRAWAL", font=("Arial", 30), background=BCK_YELLOW)
        wdrl.pack()
     
        sa_btn=tk.Button(self.wdpg, text="SAVINGS ACCOUNT", font=("Aria", 20), command=self.__show_sapg)
        sa_btn.place(x=250, y=200, height=100, width=300)

        ca_btn= tk.Button(self.wdpg, text="CURRENT ACCOUNT", font=("Arial", 20), command=lambda: self.__show_trdpg)
        ca_btn.place(x=250, y=400, height=100, width=300)
        
        self.__show_frame(self.wdpg)

    def __show_sapg(self):
        self.__set_title("Withdrawal")
        self.sapg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        self.sapg.grid(row=0, column=0, sticky='nsew')

        self.amt_label = tk.Label(self.sapg, text="Enter the amount (in terms of $500):", background=BCK_YELLOW)
        self.amt_label.pack()

        self.inp_entry = tk.Entry(self.sapg, font=('Arial', 14, 'bold'), justify='center')
        self.inp_entry.place(relx=0.40, rely=0.10, width=175, height=50)

        self.inp_result = tk.Label(self.sapg, text="", background=BCK_YELLOW)
        self.inp_result.pack()

        self.__place_keypad(self.sapg, self.__add_to_box, self.__debit_amt, self.__clear_entry)

        self.__show_frame(self.sapg)

    def __debit_amt(self):
        amt=int(self.inp_entry.get())

        if(amt % 500 == 0 and amt >= 500):
            self.__show_trdpg(amt)
        else:
            self.inp_result.config(text='Enter a Valid Amount')

    # cash deposit page
    def __show_cdpg(self):      
        self.__set_title("Cash Deposit")
        self.cdpg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        self.cdpg.grid(row=0, column=0, sticky='nsew')

        self.__show_frame(self.cdpg)

    # fast cash page
    def __show_fcpg(self):
        self.__set_title("Fast Cash")
        self.fcpg=tk.Frame(self.__wnd)
        self.fcpg.grid(row=0, column=0, sticky='nsew')
        self.fcpg.config(background=BCK_YELLOW) # page colour set pannum

        label = tk.Label(self.fcpg, text = "FAST CASH", font=("Arial", 30))
        label.pack()

        # buttons, so many buttons
        at_5h = tk.Button(self.fcpg, text="500", font=("Arial", 30), command=lambda: self.__show_trdpg(500))
        at_5h.place(x=0, y=50, height=60, width=200)

        at_1t = tk.Button(self.fcpg, text = "1000", font=("Arial", 30), command=lambda: self.__show_trdpg(1000))
        at_1t.place(x=0, y=200, height=60, width=200)

        at_2t = tk.Button(self.fcpg, text ="2000",font=("Arial", 30), command=lambda: self.__show_trdpg(2000))
        at_2t.place(x=0, y=350, height=60, width=200)
        
        at_3t = tk.Button(self.fcpg, text="3000", font=("Arial", 30), command=lambda: self.__show_trdpg(3000))
        at_3t.place(x=0, y=500, height=60, width=200)
        
        at_4t = tk.Button(self.fcpg, text="4000", font=("Arial", 30), command=lambda: self.__show_trdpg(4000))
        at_4t.place(x=600, y=50, height=60, width=200)

        at_5t = tk.Button(self.fcpg, text="5000",font=("Arial", 30), command=lambda: self.__show_trdpg(5000))
        at_5t.place(x=600, y=200, height=60, width=200)

        at_10t = tk.Button(self.fcpg, text = "10000",font=("Arial", 30), command=lambda: self.__show_trdpg(10000))
        at_10t.place(x=600, y=350, height=60, width=200)

        at_20t = tk.Button(self.fcpg, text="20000",font=("Arial", 30), command=lambda: self.__show_trdpg(20000))
        at_20t.place(x=600, y=500, height=60, width=200)

        self.__show_frame(self.fcpg)

    # transaction done page
    def __show_trdpg(self, deb_amt=0, dep_amt=0):
        self.__set_title("Please wait...")
        chpg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        chpg.grid(row=0, column=0, sticky='nsew')

        new_amt = self.__acc.acbal - deb_amt + dep_amt

        if(new_amt >= 0 and deb_amt <= 10000):
            self.col_ch=tk.Label(chpg, text='Please Wait...', font='times 35', background="#FFF87F")
            self.col_ch.pack(expand=True)

            self.__acc.update_bal(new_amt)

            self.tk_ch=tk.Label(chpg, text='', font='times 35', background="#FFF87F")
            self.tk_ch.pack(expand=True)

            self.col_ch.after(DLY_MS, self.__upd_trdpg)
        else:
            self.col_ch=tk.Label(chpg, text='Insufficient Balance...', font='times 35', background="#FFF87F")
            if(deb_amt > 10000):
                self.col_ch.config(text="Amount Exceeds Limit")
            self.col_ch.pack(expand=True)

            self.tk_ch=tk.Label(chpg, text='', font='times 35', background="#FFF87F")
            self.tk_ch.pack(expand=True)

            self.col_ch.after(500, self.__show_sapg)

        self.__show_frame(chpg)

    # updates the done page
    def __upd_trdpg(self):
        self.__set_title("Thank You")

        self.col_ch.config(text='Please Collect Your Cash')
        self.tk_ch.config(text='Thank You For Using Our ATM')

        self.tk_ch.after(2500, self.__show_pinpg)

    # balance page
    def __show_balpg(self):
        self.__set_title("Your Balance")

        self.bepg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        self.bepg.grid(row=0, column=0, sticky='nsew')

        bal_lbl=tk.Label(self.bepg, text="Balance")
        bal_lbl.config(background="#FFF87F", font=('Arial', 40, 'bold'))
        bal_lbl.place(relx=0.20, rely=0.10)

        bal_lbl=tk.Label(self.bepg, text=f"$: {self.__acc.acbal}", background=BCK_YELLOW)
        bal_lbl.config(font=('Arial', 20))
        bal_lbl.place(relx=0.40, rely=0.40)

        back_btn=tk.Button(self.bepg, text="<-", command=self.__show_homepg)
        back_btn.place(relx=0, rely=0.90, height=40, width=40)

        self.__show_frame(self.bepg)

    # show frame
    def __show_frame(self, frame):
        frame.tkraise()

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

    # adds a digit to text box
    def __add_to_box(self, symbol):
        num=""
        num+=str(symbol)
        self.inp_entry.insert(tk.END, num)

    # clears the total entry
    def __clear_entry(self):
        self.inp_entry.delete(0, tk.END)
        self.inp_result.config(text="")