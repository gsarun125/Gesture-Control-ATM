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
mspg=tk.Frame(root)
fcpg=tk.Frame(root)
wdpg=tk.Frame(root)
cdpg=tk.Frame(root)


#page colour
homepg.config(background="#FFF87F")






#show frame
def show_frame(frame):
    frame.tkraise()


# create a function to be called when the button is clicked
def button_click():
    print("Button clicked")



for frame in (homepg,ftpg,bepg,mspg,fcpg,wdpg,cdpg):
    frame.grid(row=0,column=0,sticky='nsew')





label = tk.Label(homepg, text="AHAN! Bank")
label.pack()
# create a button widget
ftBtn = tk.Button(homepg, text="FUND TRANSFER",command=lambda:show_frame(ftpg))
ftBtn.place(x=0,y=100, height=60,width=200 )


beBtn = tk.Button(homepg, text="BALANCE ENQUIRY", command=lambda:show_frame(bepg))
beBtn.place(x=0,y=300, height=60,width=200 )


msBtn = tk.Button(homepg, text="MINI STATEMENT", command=lambda:show_frame(mspg))
msBtn.place(x=0,y=500, height=60,width=200 )


fcBtn = tk.Button(homepg, text="FAST CASH", command=lambda:show_frame(fcpg))
fcBtn.place(x=600,y=100, height=60,width=200 )


wdBtn = tk.Button(homepg, text="WITHDRAWAL", command=lambda:show_frame(wdpg))
wdBtn.place(x=600,y=300, height=60,width=200 )

cdBtn = tk.Button(homepg, text="CASH DEPOSIT", command=lambda:show_frame(cdpg))
cdBtn.place(x=600,y=500, height=60,width=200 )


show_frame(homepg)

root.mainloop()
