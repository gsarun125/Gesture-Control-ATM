import tkinter as tk
from window import Window
from bacc import *

DLY_MS = 1500
BCK_YELLOW = "#FFF87F"

class Atm:
    def __init__(self, window: Window):
        self.__acc=BankAcc()
        self.__trns=TranDet()
        self.__sh=4321
        self.__win=window
        self.__wnd=window.get_window()
        self.__show_pinpg()

    def __set_title(self, title):
        self.__win.set_title(title)

    # pin input & verification page
    def __show_pinpg(self):
        self.__set_title("Enter Your PIN Number")
        self.__pinpg = tk.Frame(self.__wnd, background=BCK_YELLOW)

        self.__pinpg.grid(row=0, column=0, sticky='nsew')

        self.pin_label = tk.Label(self.__pinpg, text="Enter your PIN:", background=BCK_YELLOW)
        self.pin_label.pack()

        self.__inp_entry = tk.Entry(self.__pinpg, font=('Arial', 14, 'bold'), justify='center')
        self.__inp_entry.place(relx=0.40, rely=0.10, width=175, height=50)

        # displays the PIN verification result
        self.__inp_result = tk.Label(self.__pinpg, text="", background=BCK_YELLOW)
        self.__inp_result.pack()

        self.__place_keypad(self.__pinpg, self.__add_to_box, self.__verify_pin, self.__clear_entry)
        self.__show_frame(self.__pinpg)

    # verifies the PIN entered
    def __verify_pin(self):
        entered_pin=int(self.__inp_entry.get()) # Get the PIN entered by the user

        # Replace this with your own PIN verification logic; Should I AG?
        if entered_pin == self.__acc.pnnum:
            self.__show_homepg()
        else:
            self.__inp_result.config(text="Incorrect PIN!")

    # home page
    def __show_homepg(self):
        self.__set_title("Home Page")

        hmpg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        hmpg.grid(row=0, column=0, sticky='nsew')

        titl = tk.Label(hmpg, text="AHAN! Bank", background=BCK_YELLOW)
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

    # fund transfer
    def __show_ftpg(self):
        self.__set_title("Fund Transfer")

        ftpg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        ftpg.grid(row=0, column=0, sticky='nsew')

        self.amt_label = tk.Label(ftpg, text="Enter account number:", font=('Arial', 8, 'bold'), background=BCK_YELLOW)
        self.amt_label.place(relx=0.25, rely=0.050)

        amt_label = tk.Label(ftpg, text="Enter amount to transfer:", font=('Arial', 8, 'bold'), background=BCK_YELLOW)
        amt_label.place(relx=0.25, rely=0.150)
        
        self.__acc_entry = tk.Entry(ftpg, font=('Arial', 14, 'bold'), justify='center')
        self.__acc_entry.place(relx=0.45, rely=0.025, width=225, height=50)

        self.__amt_entry = tk.Entry(ftpg, font=('Arial', 14, 'bold'), justify='center')
        self.__amt_entry.place(relx=0.45, rely=0.125, width=225, height=50)

        self.__ft_result = tk.Label(ftpg, text='', background=BCK_YELLOW)
        self.__ft_result.place(relx=0.40, rely=0.20, width=200, height=35)

        self.__inp_entry = self.__acc_entry

        self.__place_keypad(ftpg, self.__add_to_box, self.__upd_ftpg, self.__clear_entry)

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

        wdpg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        wdpg.grid(row=0, column=0, sticky='nsew')

        wdrl = tk.Label(wdpg, text="WITHDRAWAL", font=("Arial", 30), background=BCK_YELLOW)
        wdrl.pack()
     
        sa_btn=tk.Button(wdpg, text="SAVINGS ACCOUNT", font=("Aria", 20), command=self.__show_scpg)
        sa_btn.place(x=250, y=200, height=100, width=300)

        ca_btn= tk.Button(wdpg, text="CURRENT ACCOUNT", font=("Arial", 20), command=self.__show_scpg)
        ca_btn.place(x=250, y=400, height=100, width=300)
        
        self.__show_frame(wdpg)

    # savings and current account page
    def __show_scpg(self):
        self.__set_title("Withdrawal")
        sapg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        sapg.grid(row=0, column=0, sticky='nsew')

        amt_label = tk.Label(sapg, text="Enter amount to withdraw (in terms of ₹500):", background=BCK_YELLOW)
        amt_label.pack()

        self.__inp_entry = tk.Entry(sapg, font=('Arial', 14, 'bold'), justify='center')
        self.__inp_entry.place(relx=0.40, rely=0.10, width=175, height=50)

        self.__inp_result = tk.Label(sapg, text="", background=BCK_YELLOW)
        self.__inp_result.pack()

        self.__place_keypad(sapg, self.__add_to_box, self.__debit_amt, self.__clear_entry)

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
            elif amt > 10000:
                self.__sh=1 #amount limit exceed
            else:
                self.__sh=2 #invalid amount
        else:
            self.__sh=2 #same shit
            self.__inp_result.config(text='Enter a Valid Amount')
            
        self.__show_trdpg()

    #cash deposit page
    def __show_cdpg(self):      
        self.__set_title("Cash Deposit")
        cdpg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        cdpg.grid(row=0, column=0, sticky='nsew')

        label = tk.Label(cdpg, text = "CASH DEPOSIT", font='times 35', background=BCK_YELLOW)
        label.pack()

        inst=tk.Label(cdpg, text='Please deposit your cash...', font='times 35', background=BCK_YELLOW)
        inst.pack(expand=True)

        inst.after(DLY_MS, self.__depos_amt)

        self.__show_frame(cdpg)

    #ithu amount deposit panna
    def __depos_amt(self):
        new_bal = self.__acc.acbal + 10000
        self.__trns.transact("Deposit", 10000)
        self.__acc.update_bal(new_bal)
        self.__sh=-1    #amount deposition
        self.__show_trdpg()

    def __show_mspg(self):
        self.__set_title("MINI STATEMENT")
        mspg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        mspg.grid(row=0, column=0, sticky='nsew')

        # create labels for header and account balance
        header_label = tk.Label(mspg, text="Mini Statement", font=('Arial', 16, 'bold'), background=BCK_YELLOW)
        balance_label = tk.Label(mspg, text=f"Account Balance: ₹ {self.__acc.acbal}", font=('Arial', 12), background=BCK_YELLOW)

        back_btn=tk.Button(mspg, text="<-", command=self.__show_homepg)
        back_btn.place(relx=0, rely=0.90, height=40, width=40)

        # create a listbox to display transaction history
        transactions_listbox = tk.Listbox(mspg, width=40, height=5, font=('Arial', 18), justify='center')

        # add some sample transactions to the listbox
        transactions = self.__trns.get_details()
        for transaction in transactions:
            transactions_listbox.insert(tk.END, transaction)

        # pack the widgets into the window
        header_label.pack(pady=10)
        balance_label.pack(pady=5)
        transactions_listbox.pack(padx=5, pady=5)

    #fast cash page
    def __show_fcpg(self):
        self.__set_title("Fast Cash")
        self.fcpg=tk.Frame(self.__wnd)
        self.fcpg.grid(row=0, column=0, sticky='nsew')
        self.fcpg.config(background=BCK_YELLOW) #page colour set pannum

        label = tk.Label(self.fcpg, text = "FAST CASH", font=("Arial", 30), background=BCK_YELLOW)
        label.pack()

        # buttons, so many buttons
        at_5h = tk.Button(self.fcpg, text="500", font=("Arial", 30), command=lambda: self.__debit_amt(500))
        at_5h.place(x=0, y=50, height=60, width=200)

        at_1t = tk.Button(self.fcpg, text = "1000", font=("Arial", 30), command=lambda: self.__debit_amt(1000))
        at_1t.place(x=0, y=200, height=60, width=200)

        at_2t = tk.Button(self.fcpg, text ="2000",font=("Arial", 30), command=lambda: self.__debit_amt(2000))
        at_2t.place(x=0, y=350, height=60, width=200)
        
        at_3t = tk.Button(self.fcpg, text="3000", font=("Arial", 30), command=lambda: self.__debit_amt(3000))
        at_3t.place(x=0, y=500, height=60, width=200)
        
        at_4t = tk.Button(self.fcpg, text="4000", font=("Arial", 30), command=lambda: self.__debit_amt(4000))
        at_4t.place(x=600, y=50, height=60, width=200)

        at_5t = tk.Button(self.fcpg, text="5000",font=("Arial", 30), command=lambda: self.__debit_amt(5000))
        at_5t.place(x=600, y=200, height=60, width=200)

        at_10t = tk.Button(self.fcpg, text = "10000",font=("Arial", 30), command=lambda: self.__debit_amt(10000))
        at_10t.place(x=600, y=350, height=60, width=200)

        at_20t = tk.Button(self.fcpg, text="20000",font=("Arial", 30), command=lambda: self.__debit_amt(20000))
        at_20t.place(x=600, y=500, height=60, width=200)

        self.__show_frame(self.fcpg)

    #transaction done page
    def __show_trdpg(self):
        self.__set_title("Please wait...")
        chpg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        chpg.grid(row=0, column=0, sticky='nsew')

        self.col_ch=tk.Label(chpg, text='', font='times 35', background=BCK_YELLOW)
        self.col_ch.pack(expand=True)

        self.tk_ch=tk.Label(chpg, text='', font='times 35', background=BCK_YELLOW)
        self.tk_ch.pack(expand=True)

        if self.__sh == 0:
            self.col_ch.config(text="Please Wait...")
            self.col_ch.after(DLY_MS, self.__upd_trdpg)

        elif self.__sh == 1:
            self.col_ch.config(text="Amount Exceed!")
            self.tk_ch.config(text="Enter amount less than 10000")
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

        self.bepg=tk.Frame(self.__wnd, background=BCK_YELLOW)
        self.bepg.grid(row=0, column=0, sticky='nsew')

        bal_lbl=tk.Label(self.bepg, text="BALANCE")
        bal_lbl.config(background=BCK_YELLOW, font=('Arial', 56, 'bold'))
        bal_lbl.pack()

        bal_lbl=tk.Label(self.bepg, text=f"₹ {self.__acc.acbal}", background=BCK_YELLOW)
        bal_lbl.config(font=('Arial', 28))
        bal_lbl.pack(fill="none", expand=True)

        back_btn=tk.Button(self.bepg, text="<-", command=self.__show_homepg)
        back_btn.place(relx=0, rely=0.90, height=40, width=40)

        self.__show_frame(self.bepg)

    #show frame
    def __show_frame(self, frame):
        frame.tkraise()

    #places the keypad of the ATM on-screen
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
        btn_clr.place(relx=0.15, rely=0.75)

        btn_clr = tk.Button(frame, text="<-", command=self.__rem_last)
        btn_clr.place(height=80, width=80)
        btn_clr.place(relx=0.30, rely=0.75)

        btn_0 = tk.Button(frame, text="0", command=lambda: num_click(0))
        btn_0.place(height=80, width=80)
        btn_0.place(relx=0.45, rely=0.75)

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