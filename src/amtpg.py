import tkinter as tk
from tkinter import *

def verify_pin():
    # Get the Amount entered by the user
    entered_amt_str = amt_entry.get()
    
    #converting String to integer
    entered_amt_int=int(entered_amt_str)
    # check the entered amount>500
    if entered_amt_int >= 500:
        pin_result.config(text="PIN verified!")
        
        
    else:
        pin_result.config(text="please Enter the amount greater then 500")

# Create a new tkinter window
root = tk.Tk()

# Set the window title and size
root.title("AMOUNT")
root.geometry("800x600")

# Create a label and entry widget for the PIN
pin_label = tk.Label(root, text="Enter the Amount to withdraw:")
pin_label.pack()

amt_entry = tk.Entry(root)
amt_entry.pack() 

# Create a button widget to submit the PIN
pin_button = tk.Button(root, text="confirm amount", command=verify_pin)
pin_button.pack()

# Create a label widget to display the PIN verification result
pin_result = tk.Label(root, text="")
pin_result.pack()

def add_to_amt(symbol):
    amt = ""
    amt += str(symbol)
    amt_entry.insert(END, amt)

def clear_entry():
    amt_entry.delete(0, END)


btn_1=tk.Button(root,text="1",command=lambda:add_to_amt(1))
btn_1.place(x=0,y=300, height=60,width=150 )


btn_2=tk.Button(root,text="2",command=lambda:add_to_amt(2))
btn_2.place(x=200,y=300, height=60,width=150 )

btn_3=tk.Button(root,text="3",command=lambda:add_to_amt(3))
btn_3.place(x=400,y=300, height=60,width=150 )

btn_4=tk.Button(root,text="4",command=lambda:add_to_amt(4))
btn_4.place(x=0,y=400, height=60,width=150 )

btn_5=tk.Button(root,text="5",command=lambda:add_to_amt(5))
btn_5.place(x=200,y=400, height=60,width=150 )

btn_6=tk.Button(root,text="6",command=lambda:add_to_amt(6))
btn_6.place(x=400,y=400, height=60,width=150 )

btn_7=tk.Button(root,text="7",command=lambda:add_to_amt(7))
btn_7.place(x=0,y=500, height=60,width=150)

btn_8=tk.Button(root,text="8",command=lambda:add_to_amt(8))
btn_8.place(x=200,y=500, height=60,width=150 )


btn_9=tk.Button(root,text="9",command=lambda:add_to_amt(9))
btn_9.place(x=400,y=500, height=60,width=150 )

btn_0=tk.Button(root,text="0",command=lambda:add_to_amt(0))
btn_0.place(x=600,y=400, height=60,width=150 )

btn_enter = tk.Button(root, text="ENTER", command=verify_pin)
btn_enter.place(x=600,y=500,height=60,width=150)

btn_clear = tk.Button(root, text="CLEAR", command=clear_entry)
btn_clear.place(x=600,y=300,height=60,width=150)

root.mainloop()
