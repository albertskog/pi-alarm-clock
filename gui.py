from Tkinter import *
import platform

class Gui:

    def __init__(self, master):
        operating_system = platform.system()
        if operating_system == "Linux":
            master.attributes("-fullscreen", True)
        elif operating_system == "Darwin":
            master.geometry('128x160+0+0')
        else:
            print "Unknown operating system!"
            master.destroy()

        frame = Frame(master)
        frame.pack()

        frame.configure(background='black')
        time_variable = StringVar()
        time_variable.set("00:00")

        time_label = Label(frame,
                           textvariable=time_variable,
                           font=("Helvetica", 30, "bold"),
                           foreground="white",
                           background="black",
                           height=100,
                           width=150)
        time_label.pack()
