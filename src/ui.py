import tkinter as tk

root = tk.Tk()
root.geometry("800x600")
root.configure(background="#FFF87F")

# create a function to be called when the button is clicked
def button_click():
    print("Button clicked")

label = tk.Label(root, text="AHAN! Bank")
label.pack()
# create a button widget
ftBtn = tk.Button(root, text="FUND TRANSFER", command=button_click)
ftBtn.place(x=0,y=100, height=60,width=200 )


beBtn = tk.Button(root, text="BALANCE ENQUIRY", command=button_click)
beBtn.place(x=0,y=300, height=60,width=200 )


msBtn = tk.Button(root, text="MINI STATEMENT", command=button_click)
msBtn.place(x=0,y=500, height=60,width=200 )


fCBtn = tk.Button(root, text="FAST CASH", command=button_click)
fCBtn.place(x=600,y=100, height=60,width=200 )


wdBtn = tk.Button(root, text="WITHDRAWAL", command=button_click)
wdBtn.place(x=600,y=300, height=60,width=200 )

cdBtn = tk.Button(root, text="CASH DEPOSIT", command=button_click)
cdBtn.place(x=600,y=500, height=60,width=200 )




root.mainloop()
