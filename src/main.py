from gui import *

def main():
    window=Window(800, 600)
    AtmGui(window)
    while True:
        window.update_gui()
        if(window.is_closing):
            break

if __name__ == "__main__":
    main()