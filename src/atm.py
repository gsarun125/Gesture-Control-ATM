import tkinter as tk
from tkinter import PhotoImage
from window import Window
from bacc import *

DLY_MS = 1500
BCK_COL = "#87F1FF"
BCK_IMG = "rsc/back.png"


class Atm:
    def __init__(self, window: Window):
        self.__acc=BankAcc()
        self.__trns=TranDet()
        self.__sh=4321
        self.__win=window
        self.__wnd=window.get_window()
        self.__show_pinpg()

    #window title maathum
    def __set_title(self, title):
        self.__win.set_title(title)

    def __show_calpg(self):
        self.__set_title("Calibrate hand")
        calpg=tk.Frame(self.__wnd, background=BCK_COL)
        self.__show_frame(calpg)

    #pin input & verification page
    def __show_pinpg(self):
        self.__set_title("Enter Your PIN Number")
        img = PhotoImage(file = BCK_IMG)
        pinpg = tk.Frame(self.__wnd)

        pinpg.grid(row=0, column=0, sticky='nsew')

        img_lbl = tk.Label(pinpg, image = img)
        img_lbl.place(x=0, y=0)
        self.pin_label = tk.Label(pinpg, text="Enter your PIN:")#background=BCK_COL)
        self.pin_label.pack()

        self.__inp_entry = tk.Entry(pinpg, font=('Arial', 14, 'bold'), justify='center', show='*')
        self.__inp_entry.place(relx=0.40, rely=0.10, width=175, height=50)

        # displays the PIN verification result
        self.__inp_result = tk.Label(pinpg, text="", background=BCK_COL)
        self.__inp_result.pack()

        self.__place_keypad(pinpg, self.__verify_pin)
        self.__show_frame(pinpg)

    #verifies the PIN entered
    def __verify_pin(self):
        entered_pin=int(self.__inp_entry.get()) # Get the PIN entered by the user

        # Replace this with your own PIN verification logic; Should I AG?
        if entered_pin == self.__acc.pnnum:
            self.__show_hmpg()
        else:
            self.__inp_result.config(text="Incorrect PIN!")

    #home page
    def __show_hmpg(self):
        self.__set_title("Home Page")

        hmpg=tk.Frame(self.__wnd, background=BCK_COL)
        hmpg.grid(row=0, column=0, sticky='nsew')

        titl = tk.Label(hmpg, text="AHAN! Bank", background=BCK_COL)
        titl.pack()
        # create a button widget
        ftBtn = tk.Button(hmpg, text="FUND TRANSFER", command=self.__show_ftpg)
        ftBtn.place(x=0, y=100, height=60, width=200)

        beBtn = tk.Button(hmpg, text="BALANCE ENQUIRY", command=self.__show_balpg)
        beBtn.place(x=0, y=300, height=60, width=200)

        msBtn = tk.Button(hmpg, text="MINI STATEMENT", command=self.__show_mspg)
        msBtn.place(x=0, y=500, height=60, width=200)

        fcBtn = tk.Button(hmpg, text="FAST CASH", command=self.__show_fcpg)
        fcBtn.place(x=600, y=100, height=60,width=200)

        wdBtn = tk.Button(hmpg, text="WITHDRAWAL", command=self.__show_wdpg)
        wdBtn.place(x=600, y=300, height=60, width=200)

        cdBtn = tk.Button(hmpg, text="CASH DEPOSIT", command=self.__show_cdpg)
        cdBtn.place(x=600, y=500, height=60, width=200)

        self.__show_frame(hmpg)

    #fund transfer
    def __show_ftpg(self):
        self.__set_title("Fund Transfer")

        self.__ftpg=tk.Frame(self.__wnd, background=BCK_COL)
        self.__ftpg.grid(row=0, column=0, sticky='nsew')

        acc_label = tk.Label(self.__ftpg, text="Enter account number:", font=('Arial', 8, 'bold'), background=BCK_COL)
        acc_label.place(relx=0.25, rely=0.050)

        amt_label = tk.Label(self.__ftpg, text="Enter amount to transfer:", font=('Arial', 8, 'bold'), background=BCK_COL)
        amt_label.place(relx=0.25, rely=0.150)
        
        self.__acc_entry = tk.Entry(self.__ftpg, font=('Arial', 14, 'bold'), justify='center')
        self.__acc_entry.place(relx=0.45, rely=0.025, width=225, height=50)
        self.__acc_entry.bind("<ButtonRelease-1>", self.__hndl_rls)
        self.__acc_entry.bind("<Key>", self.__key_prs)

        self.__amt_entry = tk.Entry(self.__ftpg, font=('Arial', 14, 'bold'), justify='center')
        self.__amt_entry.place(relx=0.45, rely=0.125, width=225, height=50)
        self.__amt_entry.bind("<ButtonRelease-1>", self.__hndl_rls)

        self.__ft_result = tk.Label(self.__ftpg, text='', background=BCK_COL)
        self.__ft_result.place(relx=0.40, rely=0.20, width=200, height=35)

        back_btn=tk.Button(self.__ftpg, text="<-", command=self.__show_hmpg)
        back_btn.place(relx=0, rely=0.90, height=40, width=40)

        self.__inp_entry = self.__acc_entry

        self.__place_keypad(self.__ftpg, self.__upd_ftpg, self.__key_prs)

    def __key_prs(self, event):
        print(len(self.__acc_entry.get()))
        if(len(self.__acc_entry.get()) == 16):
            self.__inp_entry = self.__amt_entry

    def __hndl_rls(self, event):
        foc_gt = self.__ftpg.focus_get()
        if(type(foc_gt) == type(self.__inp_entry)):
            self.__inp_entry = foc_gt

    #update pannum fund transfer pageah
    def __upd_ftpg(self):
        self.__inp_entry=self.__amt_entry
        acc_en = self.__acc_entry.get()
        if(acc_en != '' and self.__amt_entry.get() != ''):
            amt=int(self.__amt_entry.get())
            new_amt=self.__acc.acbal - amt
            if(len(acc_en) < 16):
                self.__ft_result.config(text="Enter a Valid Account Number!")
                self.__clear_entry()
                self.__inp_entry=self.__acc_entry
                self.__clear_entry()
            elif new_amt >= 0:
                self.__sh=-4    #amount transfer
                self.__trns.transact("Transfer", amt)
                self.__acc.update_bal(new_amt)
                self.__show_trdpg()
            else:
                self.__sh=-2    #insufficient fund for transfer
                self.__show_trdpg()

    # withdrawal page
    def __show_wdpg(self):
        self.__set_title("Withdrawal")

        wdpg=tk.Frame(self.__wnd, background=BCK_COL)
        wdpg.grid(row=0, column=0, sticky='nsew')

        wdrl = tk.Label(wdpg, text="WITHDRAWAL", font=("Arial", 30), background=BCK_COL)
        wdrl.pack()
     
        sa_btn=tk.Button(wdpg, text="SAVINGS ACCOUNT", font=("Aria", 20), command=self.__show_scpg)
        sa_btn.place(x=250, y=200, height=100, width=300)

        ca_btn= tk.Button(wdpg, text="CURRENT ACCOUNT", font=("Arial", 20), command=self.__show_scpg)
        ca_btn.place(x=250, y=400, height=100, width=300)

        back_btn=tk.Button(wdpg, text="<-", command=self.__show_hmpg)
        back_btn.place(relx=0, rely=0.90, height=40, width=40)
        
        self.__show_frame(wdpg)

    # savings and current account page
    def __show_scpg(self):
        self.__set_title("Withdrawal")
        sapg=tk.Frame(self.__wnd, background=BCK_COL)
        sapg.grid(row=0, column=0, sticky='nsew')

        amt_label = tk.Label(sapg, text="Enter amount to withdraw (in terms of ₹500):", background=BCK_COL)
        amt_label.pack()

        self.__inp_entry = tk.Entry(sapg, font=('Arial', 14, 'bold'), justify='center')
        self.__inp_entry.place(relx=0.40, rely=0.10, width=175, height=50)

        self.__inp_result = tk.Label(sapg, text="", background=BCK_COL)
        self.__inp_result.pack()

        self.__place_keypad(sapg, self.__debit_amt)

        self.__show_frame(sapg)

    #amount aataiya poda
    def __debit_amt(self, amt=0):
        if amt == 0:
            amt=int(self.__inp_entry.get())

        if amt % 500 == 0 and amt >= 500:
            
            new_bal = self.__acc.acbal - amt

            if new_bal >= 0:
                self.__sh=0 #amount withdrawal
                self.__trns.transact("Withdraw", amt)
                self.__acc.update_bal(new_bal)
            elif amt > 20000:
                self.__sh=1 #amount limit exceed
            else:
                self.__sh=2 #invalid amount
        else:
            self.__sh=2 
            self.__inp_result.config(text='Enter a Valid Amount')
            
        self.__show_trdpg()

    #cash deposit page
    def __show_cdpg(self):      
        self.__set_title("Cash Deposit")
        cdpg=tk.Frame(self.__wnd, background=BCK_COL)
        cdpg.grid(row=0, column=0, sticky='nsew')

        cd_label = tk.Label(cdpg, text = "CASH DEPOSIT", font='times 35', background=BCK_COL)
        cd_label.pack()

        inst=tk.Label(cdpg, text='Please deposit your cash...', font='times 35', background=BCK_COL)
        inst.pack(expand=True)

        inst.after(DLY_MS, self.__depos_amt)

        self.__show_frame(cdpg)

    #amount deposit 
    def __depos_amt(self):
        new_bal = self.__acc.acbal + 10000
        self.__trns.transact("Deposit", 10000)
        self.__acc.update_bal(new_bal)
        self.__sh=-1    #amount deposition
        self.__show_trdpg()

    def __show_mspg(self):
        self.__set_title("MINI STATEMENT")
        mspg=tk.Frame(self.__wnd, background=BCK_COL)
        mspg.grid(row=0, column=0, sticky='nsew')

        # create labels for header and account balance
        ms_label = tk.Label(mspg, text="Mini Statement", font=('Arial', 16, 'bold'), background=BCK_COL)
        bal_label = tk.Label(mspg, text=f"Account Balance: ₹ {self.__acc.acbal}", font=('Arial', 12), background=BCK_COL)

        back_btn=tk.Button(mspg, text="<-", command=self.__show_hmpg)
        back_btn.place(relx=0, rely=0.90, height=40, width=40)

        # create a listbox to display transaction history
        transactions_listbox = tk.Listbox(mspg, width=40, height=5, font=('Arial', 18), justify='center')

        # add some sample transactions to the listbox
        transactions = self.__trns.get_details()
        for transaction in transactions:
            transactions_listbox.insert(tk.END, transaction)

        # pack the widgets into the window
        ms_label.pack(pady=10)
        bal_label.pack(pady=5)
        transactions_listbox.pack(padx=5, pady=5)

    #fast cash page
    def __show_fcpg(self):
        self.__set_title("Fast Cash")
        fcpg=tk.Frame(self.__wnd)
        fcpg.grid(row=0, column=0, sticky='nsew')
        fcpg.config(background=BCK_COL) 

        ft_label = tk.Label(fcpg, text = "FAST CASH", font=("Arial", 30), background=BCK_COL)
        ft_label.pack()

        # buttons
        at_5h = tk.Button(fcpg, text="500", font=("Arial", 30), command=lambda: self.__debit_amt(500))
        at_5h.place(x=0, y=50, height=60, width=200)

        at_1t = tk.Button(fcpg, text = "1000", font=("Arial", 30), command=lambda: self.__debit_amt(1000))
        at_1t.place(x=0, y=200, height=60, width=200)

        at_2t = tk.Button(fcpg, text ="2000",font=("Arial", 30), command=lambda: self.__debit_amt(2000))
        at_2t.place(x=0, y=350, height=60, width=200)
        
        at_3t = tk.Button(fcpg, text="3000", font=("Arial", 30), command=lambda: self.__debit_amt(3000))
        at_3t.place(x=0, y=500, height=60, width=200)
        
        at_4t = tk.Button(fcpg, text="4000", font=("Arial", 30), command=lambda: self.__debit_amt(4000))
        at_4t.place(x=600, y=50, height=60, width=200)

        at_5t = tk.Button(fcpg, text="5000",font=("Arial", 30), command=lambda: self.__debit_amt(5000))
        at_5t.place(x=600, y=200, height=60, width=200)

        at_10t = tk.Button(fcpg, text = "10000",font=("Arial", 30), command=lambda: self.__debit_amt(10000))
        at_10t.place(x=600, y=350, height=60, width=200)

        at_20t = tk.Button(fcpg, text="20000",font=("Arial", 30), command=lambda: self.__debit_amt(20000))
        at_20t.place(x=600, y=500, height=60, width=200)

        self.__show_frame(fcpg)

    #transaction done page
    def __show_trdpg(self):
        self.__set_title("Please wait...")
        chpg=tk.Frame(self.__wnd, background=BCK_COL)
        chpg.grid(row=0, column=0, sticky='nsew')

        self.col_ch=tk.Label(chpg, text='', font='times 35', background=BCK_COL)
        self.col_ch.pack(expand=True)

        self.tk_ch=tk.Label(chpg, text='', font='times 35', background=BCK_COL)
        self.tk_ch.pack(expand=True)

        if self.__sh == 0:
            self.col_ch.config(text="Please Wait...")
            self.col_ch.after(DLY_MS, self.__upd_trdpg)

        elif self.__sh == 1:
            self.col_ch.config(text="Amount Exceed!")
            self.tk_ch.config(text="Enter amount less than 20000")
            self.col_ch.after(DLY_MS, self.__show_scpg)

        elif self.__sh == -1 or self.__sh == -4:
            self.col_ch.config(text="Please Wait...")
            self.col_ch.after(DLY_MS, self.__upd_trdpg)

        else:
            self.col_ch.config(text='Insufficient Balance...')
            if(self.__sh != -2):
                self.col_ch.after(DLY_MS, self.__show_scpg)
            else:
                self.col_ch.after(DLY_MS, self.__show_ftpg)

        self.__show_frame(chpg)

    # updates the done page
    def __upd_trdpg(self):
        self.__set_title("Thank You")

        if self.__sh == 0:
            self.tk_ch.config(text='Please Collect Your Cash')
        elif self.__sh == -4:
            self.tk_ch.config(text='Amount Transferred Successfully!')
        else:
            self.tk_ch.config(text='')
        
        self.col_ch.config(text='Thank You For Using Our ATM')

        self.tk_ch.after(DLY_MS, self.__show_pinpg)

    #balance page
    def __show_balpg(self):
        self.__set_title("Your Balance")

        bepg=tk.Frame(self.__wnd, background=BCK_COL)
        bepg.grid(row=0, column=0, sticky='nsew')

        bal_lbl=tk.Label(bepg, text="BALANCE")
        bal_lbl.config(background=BCK_COL, font=('Arial', 56, 'bold'))
        bal_lbl.pack()

        bal_lbl=tk.Label(bepg, text=f"₹ {self.__acc.acbal}", background=BCK_COL)
        bal_lbl.config(font=('Arial', 28))
        bal_lbl.pack(fill="none", expand=True)

        back_btn=tk.Button(bepg, text="<-", command=self.__show_hmpg)
        back_btn.place(relx=0, rely=0.90, height=40, width=40)

        self.__show_frame(bepg)

    #show frame
    def __show_frame(self, frame):
        frame.tkraise()

    #places the keypad of the ATM on-screen
    def __place_keypad(self, frame, enter_btn, btn_clk=None):
        btn_1 = tk.Button(frame, text="1", command=lambda: self.__add_to_box(1))
        btn_1.place(height=80, width=80)
        btn_1.place(relx=0.30, rely=0.30)
        btn_1.bind("<1>", btn_clk)

        btn_2 = tk.Button(frame, text="2", command=lambda: self.__add_to_box(2))
        btn_2.place(height=80, width=80)
        btn_2.place(relx=0.45, rely=0.30)
        btn_2.bind("<1>", btn_clk)

        btn_3 = tk.Button(frame, text="3", command=lambda: self.__add_to_box(3))
        btn_3.place(height=80, width=80)
        btn_3.place(relx=0.60, rely=0.30)
        btn_3.bind("<1>", btn_clk)

        btn_4 = tk.Button(frame, text="4", command=lambda: self.__add_to_box(4))
        btn_4.place(height=80, width=80)
        btn_4.place(relx=0.30, rely=0.45)
        btn_4.bind("<1>", btn_clk)

        btn_5 = tk.Button(frame, text="5", command=lambda: self.__add_to_box(5))
        btn_5.place(height=80, width=80)
        btn_5.place(relx=0.45, rely=0.45)
        btn_5.bind("<1>", btn_clk)

        btn_6 = tk.Button(frame, text="6", command=lambda: self.__add_to_box(6))
        btn_6.place(height=80, width=80)
        btn_6.place(relx=0.60, rely=0.45)
        btn_6.bind("<1>", btn_clk)

        btn_7 = tk.Button(frame, text="7", command=lambda: self.__add_to_box(7))
        btn_7.place(height=80, width=80)
        btn_7.place(relx=0.30, rely=0.60)
        btn_7.bind("<1>", btn_clk)

        btn_8 = tk.Button(frame, text="8", command=lambda: self.__add_to_box(8))
        btn_8.place(height=80, width=80)
        btn_8.place(relx=0.45, rely=0.60)
        btn_8.bind("<1>", btn_clk)

        btn_9 = tk.Button(frame, text="9", command=lambda: self.__add_to_box(9))
        btn_9.place(height=80, width=80)
        btn_9.place(relx=0.60, rely=0.60)
        btn_9.bind("<1>", btn_clk)
        
        btn_clr = tk.Button(frame, text="CLEAR", command=self.__clear_entry)
        btn_clr.place(height=80, width=80)
        btn_clr.place(relx=0.15, rely=0.75)

        btn_clr = tk.Button(frame, text="<-", command=self.__rem_last)
        btn_clr.place(height=80, width=80)
        btn_clr.place(relx=0.30, rely=0.75)

        btn_0 = tk.Button(frame, text="0", command=lambda: self.__add_to_box(0))
        btn_0.place(height=80, width=80)
        btn_0.place(relx=0.45, rely=0.75)
        btn_0.bind("<1>", btn_clk)

        btn_ent = tk.Button(frame, text="ENTER", command=enter_btn)
        btn_ent.place(height=80, width=80)
        btn_ent.place(relx=0.60, rely=0.75)

    #adds a digit to text box
    def __add_to_box(self, symbol):
        num=""
        num+=str(symbol)
        self.__inp_entry.insert(tk.END, num)

    #removes last character from entry
    def __rem_last(self):
        txt=self.__inp_entry.get()[:-1]
        self.__inp_entry.delete(0, tk.END)
        self.__inp_entry.insert(0, txt)

    #clears the total entry
    def __clear_entry(self):
        self.__inp_entry.delete(0, tk.END)
        self.__inp_result.config(text='')