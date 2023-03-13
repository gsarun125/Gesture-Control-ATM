from atm import *

def main():
    window=Window(800, 600)
    Atm(window)
    while True:
        window.update_gui()
        if(window.is_closing):
            break

if __name__ == "__main__":
    main()