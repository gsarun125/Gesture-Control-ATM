import tkinter as tk

root = tk.Tk()

# create a function to be called when the button is clicked
def button_click():
    print("Button clicked")

# create a button widget
button = tk.Button(root, text="Click me", command=button_click)

# display the button
button.pack()

root.mainloop()
