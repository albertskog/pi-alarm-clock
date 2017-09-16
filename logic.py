"""Module implementing the logic of the Pi Alarm Clock"""
from datetime import datetime
from buttons import Buttons

class Logic(object):
    """Class for alarm clock logic"""
    def __init__(self, gui):
        self.gui = gui
        self.gui.register_button_handler(self.button_handler)
        self.buttons = Buttons(self.button_handler)
        self.set_alarm(6, 0)
        self.alarm_is_active = False
        self.update_time()


    def update_time(self):
        """Callback used to update current time in the gui"""
        self.gui.register_callback(1000, self.update_time)
        time = datetime.now().time()
        self.gui.set_time(str(time)[0:5])
        self.check_alarm(time)

    def set_alarm(self, hour, minute):
        """Functions for setting new alarm time"""
        self.alarm_time = (hour, minute)
        self.gui.set_alarm_time("{h:02d}:{m:02d}".format(h=hour, m=minute))

    def check_alarm(self, time):
        """Check if it is time to start the alarm"""
        if self.alarm_is_active:
            return

        if self.alarm_time == (time.hour, time.minute):
            print "Alarm active"
            self.alarm_is_active = True
            self.gui.start_alarm()

    def move_alarm(self, minutes):
        """Move alarm given number of minutes"""
        new_hour = self.alarm_time[0]
        new_minute = self.alarm_time[1] + minutes
        if new_minute >= 60:
            new_minute -= 60
            new_hour += 1
        if new_minute < 0:
            new_minute += 60
            new_hour -= 1
        self.set_alarm(new_hour, new_minute)

    def button_handler(self, button):
        """Handler for button events"""
        print "Button {0} pressed".format(button)
        if button == "+":
            self.move_alarm(minutes=15)
        if button == "-":
            self.move_alarm(minutes=-15)
