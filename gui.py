"""User interface module for Pi Alarm Clock"""
from Tkinter import Frame, Label, StringVar
import platform

class Gui(object):
    """Class for hanling the ui"""
    def __init__(self, master):
        operating_system = platform.system()
        if operating_system == "Linux":
            master.attributes("-fullscreen", True)
        elif operating_system == "Darwin":
            master.geometry('128x160+0+0')
        else:
            print "Unknown operating system!"
            master.destroy()

        master.configure(background='black')

        self.frame = Frame(master)
        self.frame.configure(background='black')
        self.frame.pack()

        self.alarm_label = Label(self.frame,
                                 text="Alarm",
                                 font=("Helvetica", 30, "bold"),
                                 foreground="white",
                                 background="black")

        self.time_variable = StringVar()

        time_label = Label(self.frame,
                           textvariable=self.time_variable,
                           font=("Helvetica", 30, "bold"),
                           foreground="white",
                           background="black",
                           height=2)
        time_label.pack()

    def register_callback(self, time_ms, callback):
        """Register a function to be called some time in the future"""
        self.frame.after(time_ms, callback)

    def set_time(self, time):
        """Set contents of time label"""
        self.time_variable.set(time)

    def start_alarm(self):
        """Show the alarm label on screen"""
        self.alarm_label.pack()

    def stop_alarm(self):
        """Remove alarm label from screen"""
        self.alarm_label.pack_forget()
