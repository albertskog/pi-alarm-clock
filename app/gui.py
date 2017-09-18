"""User interface module for Pi Alarm Clock"""
from Tkinter import Frame, Label, StringVar
import platform

class Gui(object):
    """Class for hanling the ui"""

    BUTTON_MAP = {"1": "-", "2": "+", "3": "a", "4": "b", "5": "c"}

    def __init__(self, master):
        self.master = master
        operating_system = platform.system()
        if operating_system == "Linux":
            self.master.attributes("-fullscreen", True)
        elif operating_system == "Darwin":
            self.master.geometry('128x160+0+0')
        else:
            print "Unknown operating system!"
            self.master.destroy()

        self.master.configure(background="red")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.frame = Frame(self.master)
        self.frame.configure(background="black")
        self.frame.grid(sticky="nsew")

        self.alarm_label = Label(self.frame,
                                 text="Alarm",
                                 font=("Helvetica", 30),
                                 foreground="white",
                                 background="black")

        self.time_variable = StringVar()

        time_label = Label(self.frame,
                           textvariable=self.time_variable,
                           font=("Helvetica", 50),
                           foreground="white",
                           background="black")
        time_label.place(relx=0.5, rely=0.5, anchor="center")

        self.alarm_time_variable = StringVar()

        alarm_time_label = Label(self.frame,
                                 textvariable=self.alarm_time_variable,
                                 font=("Helvetica", 20),
                                 foreground="white",
                                 background="black")
        alarm_time_label.place(relx=0.5, rely=0.9, anchor="center")

        self.button_handler = ""

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
        self.alarm_label.place_forget()

    def key_callback(self, event):
        """Callback for keyboard events"""
        if self.button_handler:
            self.button_handler(self.BUTTON_MAP[event.char])

    def register_button_handler(self, button_handler):
        """Setup handler to receive button events"""
        self.button_handler = button_handler
        self.master.bind('1', self.key_callback)
        self.master.bind('2', self.key_callback)
        self.master.bind('3', self.key_callback)
        self.master.bind('4', self.key_callback)
        self.master.bind('5', self.key_callback)
