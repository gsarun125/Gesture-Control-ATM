import tkinter as tk

class UI1:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.label = tk.Label(self.frame, text="This is UI 1")
        self.label.pack()
        self.frame.pack(side="left")

class UI2:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(master)
        self.label = tk.Label(self.frame, text="This is UI 2")
        self.label.pack()
        self.frame.pack(side="right")

root = tk.Tk()
ui1 = UI1(root)
ui2 = UI2(root)
root.mainloop()
