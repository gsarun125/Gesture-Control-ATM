import tkinter as tk
import cv2

root = tk.Tk()
root.geometry("800x600")
#root.configure(background="#FFF87F")



root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

homepg = tk.Frame(root)
ftpg=tk.Frame(root)
bepg=tk.Frame(root)





#page colour
homepg.config(background="#FFF87F")






#show frame
def show_frame(frame):
    frame.tkraise()


# create a function to be called when the button is clicked
def button_click():
    print("Button clicked")

for frame in (homepg,ftpg,bepg):
    frame.grid(row=0,column=0,sticky='nsew')


label = tk.Label(homepg, text="AHAN! Bank")
label.pack()
# create a button widget
ftBtn = tk.Button(homepg, text="FUND TRANSFER",command=lambda:show_frame(ftpg))
ftBtn.place(x=0,y=100, height=60,width=200 )


beBtn = tk.Button(homepg, text="BALANCE ENQUIRY", command=lambda:show_frame(bepg))
beBtn.place(x=0,y=300, height=60,width=200 )


msBtn = tk.Button(homepg, text="MINI STATEMENT", command=button_click)
msBtn.place(x=0,y=500, height=60,width=200 )


fCBtn = tk.Button(homepg, text="FAST CASH", command=button_click)
fCBtn.place(x=600,y=100, height=60,width=200 )


wdBtn = tk.Button(homepg, text="WITHDRAWAL", command=button_click)
wdBtn.place(x=600,y=300, height=60,width=200 )

cdBtn = tk.Button(homepg, text="CASH DEPOSIT", command=button_click)
cdBtn.place(x=600,y=500, height=60,width=200 )


show_frame(homepg)

root.mainloop()
