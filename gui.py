from Tkinter import Tk, Frame, Label, StringVar
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

        self.frame = Frame(master)
        self.frame.pack()

        self.frame.configure(background='black')
        self.time_variable = StringVar()

        time_label = Label(self.frame,
                           textvariable=self.time_variable,
                           font=("Helvetica", 30, "bold"),
                           foreground="white",
                           background="black",
                           height=100,
                           width=150)
        time_label.pack()

    def register_callback(self, time_ms, callback):
        self.frame.after(time_ms, callback)

    def set_time(self, time):
        self.time_variable.set(time)
