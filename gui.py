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

        master.configure(background="red")
        master.grid_rowconfigure(0, weight=1)
        master.grid_columnconfigure(0, weight=1)
        self.frame = Frame(master)
        self.frame.configure(background="black")
        self.frame.grid(sticky="nsew")

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
                           background="black")
        time_label.place(relx=0.5, rely=0.5, anchor="center")

        self.alarm_time_variable = StringVar()

        alarm_time_label = Label(self.frame,
                                 textvariable=self.alarm_time_variable,
                                 font=("Helvetica", 20, "bold"),
                                 foreground="white",
                                 background="black")
        alarm_time_label.place(relx=0.5, rely=0.9, anchor="center")

    def register_callback(self, time_ms, callback):
        """Register a function to be called some time in the future"""
        self.frame.after(time_ms, callback)

    def set_time(self, time):
        """Set contents of time label"""
        self.time_variable.set(time)

    def set_alarm_time(self, time):
        """Set contents of alarm time label"""
        self.alarm_time_variable.set(time)

    def start_alarm(self):
        """Show the alarm label on screen"""
        self.alarm_label.place(relx=0.5, rely=0.15, anchor="center")

    def stop_alarm(self):
        """Remove alarm label from screen"""
        self.alarm_label.grid_forget()
