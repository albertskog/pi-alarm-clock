"""Module implementing the logic of the Pi Alarm Clock"""
from datetime import datetime
from app.buttons import Buttons
from app.backlight import Backlight
from app.sound import Sound

class Logic(object):
    """Class for alarm clock logic"""

    time_increment = 15

    def __init__(self, gui):
        self.gui = gui
        self.gui.register_button_handler(self.button_handler)
        self.buttons = Buttons(self.button_handler)
        self.backlight = Backlight()
        self.sound = Sound()
        self.set_alarm(6, 0)
        self.alarm_is_active = False
        self.alarm_is_enabled = True
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

        if not self.alarm_is_enabled:
            if self.alarm_time != (time.hour, time.minute):
                print "Automatic enable alarm"
                self.alarm_is_enabled = True
            return

        if self.alarm_time == (time.hour, time.minute):
            print "Alarm active"
            self.alarm_is_active = True
            self.backlight.set_brightness(100)
            self.sound.start()
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

    def toggle_alarm(self):
        """Turn off alarm if it is active"""
        if self.alarm_is_active:
            self.sound.stop()
            self.backlight.set_brightness(3)
            self.gui.stop_alarm()
            self.alarm_is_enabled = False
            self.alarm_is_active = False
            print "Stopped alarm"
            return

        # if self.alarm_is_enabled:
        #     print "Disable alarm"
        #     self.alarm_is_enabled = False
        #     self.gui.set_alarm_time("--:--")
        # else:
        #     print "Enable alarm"
        #     self.alarm_is_enabled = True
        #     time = "{h:02d}:{m:02d}".format(h=self.alarm_time[0],
        #                                     m=self.alarm_time[1])
        #     self.gui.set_alarm_time(time)

    def button_handler(self, button):
        """Handler for button events"""
        print "Button {0} pressed".format(button)
        if button == "+":
            self.move_alarm(minutes=self.time_increment)
        if button == "-":
            self.move_alarm(minutes=-self.time_increment)
        if button == "a":
            self.toggle_alarm()