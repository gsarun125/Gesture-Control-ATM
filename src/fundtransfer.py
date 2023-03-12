import tkinter as tk
from tkinter import *

class FundTransferUI:
    def __init__(self, master):
        self.master = master
        master.geometry("800x600")
        master.title("Fund Transfer UI")

        # Create labels and entry boxes for sender and recipient information
        tk.Label(master, text="Sender Account Number:").grid(row=0, column=0)
        self.sender_entry = tk.Entry(master)
        self.sender_entry.grid(row=0, column=1)

        
        tk.Label(master, text="Recipient Account Number:").grid(row=2, column=0)
        self.recipient_entry = tk.Entry(master)
        self.recipient_entry.grid(row=2, column=1)

        
        tk.Label(master, text="Transfer Amount:").grid(row=4, column=0)
        self.transfer_amount_entry = tk.Entry(master)
        self.transfer_amount_entry.grid(row=4, column=1)

        # Create the submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_transfer)
        self.submit_button.grid(row=5, column=0, columnspan=2)

        btn_1 = tk.Button(master, text="1", command=lambda: self.add_to_pin(1))
        btn_1.place(x=0, y=300, height=60, width=150)


        btn_2 = tk.Button(master, text="2", command=lambda: self.add_to_pin(2))
        btn_2.place(x = 200, y = 300, height=60, width=150)

        btn_3 = tk.Button(master, text="3", command=lambda: self.add_to_pin(3))
        btn_3.place(x=400, y=300, height=60, width=150)

        btn_4 = tk.Button(master, text="4", command=lambda: self.add_to_pin(4))
        btn_4.place(x=0, y=400, height=60, width=150)

        btn_5 = tk.Button(master, text="5", command=lambda: self.add_to_pin(5))
        btn_5.place(x=200, y = 400, height = 60,width=150)

        btn_6 = tk.Button(master, text="6", command=lambda: self.add_to_pin(6))
        btn_6.place(x=400, y=400, height=60, width=150)

        btn_7 = tk.Button(master, text="7", command=lambda: self.add_to_pin(7))
        btn_7.place(x=0, y=500, height=60, width=150)
        
        btn_8 = tk.Button(master, text="8", command=lambda: self.add_to_pin(8))
        btn_8.place(x=200,y=500, height=60,width = 150)
        
        btn_9 = tk.Button(master, text="9", command=lambda: self.add_to_pin(9))
        btn_9.place(x=400, y=500, height=60, width=150)
        
        btn_0 = tk.Button(master, text="0", command=lambda: self.add_to_pin(0))
        btn_0.place(x=600, y=400, height=60, width=150)
        
        btn_enter = tk.Button(master, text="ENTER", command=self.submit_transfer)
        btn_enter.place(x=600, y=500, height=60, width=150)
        
        btn_clear = tk.Button(master, text="CLEAR", command=self.clear_entry)
        btn_clear.place(x=600, y=300, height=60, width=150)




    def submit_transfer(self):
        sender_account = self.sender_entry.get()
        sender_name = self.sender_name_entry.get()
        recipient_account = self.recipient_entry.get()
        recipient_name = self.recipient_name_entry.get()
        transfer_amount = self.transfer_amount_entry.get()

        # Insert code here to process the fund transfer

        # Clear the entry boxes after processing the transfer
        self.sender_entry.delete(0, 'end')
        self.sender_name_entry.delete(0, 'end')
        self.recipient_entry.delete(0, 'end')
        self.recipient_name_entry.delete(0, 'end')
        self.transfer_amount_entry.delete(0, 'end')

    def add_to_pin(self,symbol):
        pin=""
        pin+=str(symbol)
        self.sender_entry.insert(END, pin)
        self.recipient_entry.insert(END,pin)
        self.transfer_amount_entry.insert(END,pin)

    def clear_entry(self):
        self.sender_entry.delete(0, END)
        self.recipient_entry.delete(0,END)
        self.transfer_amount_entry.delete(0,END)


root = tk.Tk()
fund_transfer_ui = FundTransferUI(root)
root.mainloop()
