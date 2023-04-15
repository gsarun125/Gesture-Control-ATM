
import subprocess
import keyboard

cmd1 = "python main.py"
cmd2 = "python hamigi.py"


def on_key_press(event):
    if event.name == 'q': 
        print("Exiting gracefully...")
        p1.terminate()
        p2.terminate()
        p1.join()
        p2.join()
        print("Both scripts have finished executing.")
        exit(0)


# Launch the two scripts 
p1 = subprocess.Popen(cmd1.split())
p2 = subprocess.Popen(cmd2.split())

keyboard.on_press_key('q', on_key_press)



# Wait for both processes to finish
p1.wait()
p2.wait()

print("ATM closed")
