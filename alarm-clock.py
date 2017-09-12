from Tkinter import Tk
from gui import Gui
from logic import Logic

def check():
    root.after(50, check) # 50 stands for 50 ms.

if __name__ == '__main__':

    print "Starting..."

    root = Tk()

    # Add a callback so we can exit from the terminal
    root.after(50, check)

    Gui = Gui(root)
    Logic = Logic(Gui)

    root.mainloop()
