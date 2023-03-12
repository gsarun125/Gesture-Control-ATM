import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("800x600")
root.title("MiNI STATEMENT")

message = tk.Label(root, text="Enter your account number:")
message.pack()

account_entry = tk.Entry(root)
account_entry.pack()
def min_statement():
# create labels for header and account balance
    header_label = tk.Label(root, text="Mini Statement", font=('Arial', 16, 'bold'))
    balance_label = tk.Label(root, text="Account Balance: $1000", font=('Arial', 12))

# create a listbox to display transaction history
    transactions_listbox = tk.Listbox(root, width=40, height=5, font=('Arial', 12))

# add some sample transactions to the listbox
    transactions = ["03/01/2023: Withdrawal $100", "02/28/2023: Deposit $500", "02/25/2023: Payment $50"]
    for transaction in transactions:
        transactions_listbox.insert(tk.END, transaction)


# pack the widgets into the window
    header_label.pack(pady=10)
    balance_label.pack(pady=5)
    transactions_listbox.pack(padx=5, pady=5)


def get_minibalance():
    # TODO: Replace this with actual balance inquiry logic
    account_number = account_entry.get()

    account_number_int=int(account_number)
    if account_number_int==962820104013:
        balance_label.config(text=f"Your Account no is {account_number}")
        min_statement()
    else:
        balance_label.config(text="Enter the valid Account no")




def add_to_pin(symbol):
    acc = ""
    acc += str(symbol)
    account_entry.insert(END, acc)



def clear_entry():
    account_entry.delete(0, END)
    balance_label.config(text="")


balance_button = tk.Button(root, text="Get MINI STATEMENT", command=get_minibalance)
balance_button.pack()

#key pad  button
btn_1=tk.Button(root, text="1", command=lambda: add_to_pin(1))
btn_1.place(x=0, y=300, height=60, width=150 )


btn_2=tk.Button(root,text="2",command=lambda: add_to_pin(2))
btn_2.place(x=200, y=300, height=60, width=150 )

btn_3=tk.Button(root, text="3", command=lambda: add_to_pin(3))
btn_3.place(x=400, y=300, height=60, width=150 )

btn_4=tk.Button(root, text="4", command=lambda: add_to_pin(4))
btn_4.place(x=0, y=400, height=60, width=150 )

btn_5=tk.Button(root,text="5", command=lambda: add_to_pin(5))
btn_5.place(x=200, y=400, height=60, width=150 )

btn_6=tk.Button(root, text="6", command=lambda: add_to_pin(6))
btn_6.place(x=400, y=400, height=60, width=150 )

btn_7=tk.Button(root, text="7", command=lambda: add_to_pin(7))
btn_7.place(x=0, y=500, height=60, width=150)

btn_8=tk.Button(root,text="8", command=lambda: add_to_pin(8))
btn_8.place(x=200, y=500, height=60, width=150 )


btn_9=tk.Button(root,text="9",command=lambda: add_to_pin(9))
btn_9.place(x=400, y=500, height=60, width=150 )

btn_0=tk.Button(root, text="0",command=lambda: add_to_pin(0))
btn_0.place(x=600, y=400, height=60, width=150 )

btn_enter = tk.Button(root, text="ENTER", command=get_minibalance)
btn_enter.place(x=600, y=500, height=60, width=150)

btn_clear = tk.Button(root, text="CLEAR", command=clear_entry)
btn_clear.place(x=600, y=300, height=60, width=150)

balance_label = tk.Label(root, text="")
balance_label.pack()


root.mainloop()
