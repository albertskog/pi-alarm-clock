"""Main script for Pi Alarm Clock"""
from Tkinter import Tk
from app.gui import Gui
from app.logic import Logic

if __name__ == '__main__':

    print "Starting..."

    ROOT = Tk()

    GUI = Gui(ROOT)
    LOGIC = Logic(GUI)

    ROOT.mainloop()
