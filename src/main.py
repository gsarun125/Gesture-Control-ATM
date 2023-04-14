from atm import *
import win32api, win32con

def main():
    window=Window(800, 600)
    #x, y = rect[2]-rect[0], rect[3]-rect[2]
    Atm(window)
    window.update_gui()
    rect = window.get_winrect()
    x, y = int(rect[0] + 800/2), int(rect[1] + 600/2)
    win32api.SetCursorPos((x,y))
    while True:
        window.update_gui()
        if(window.is_closing):
            break

if __name__ == "__main__":
    main()