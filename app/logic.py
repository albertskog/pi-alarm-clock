"""Module implementing the logic of the Pi Alarm Clock"""
from datetime import datetime
from config import CONFIG
from app.buttons import Buttons
from app.backlight import Backlight
from app.sound import Sound
from app.smart_home import SmartHome

class Logic(object):
    """Class for alarm clock logic"""

    alarm_is_active = False
    alarm_is_enabled = True

    def __init__(self, gui):
        self.gui = gui
        self.gui.register_button_handler(self.button_handler)
        self.buttons = Buttons(self.button_handler)
        self.backlight = Backlight()
        self.sound = Sound()

        self.set_alarm(CONFIG["alarm_time"][0], CONFIG["alarm_time"][1])
        self.update_time()

        self.smart_home = SmartHome(self.command_handler)
        event = {"event": "started", "alarm_time": self.alarm_time}
        self.smart_home.send_event(event)

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
        weekend = [5, 6]
        if datetime.now().weekday() in weekend:
            # No alarm on weekends
            return

        if self.alarm_is_active:
            return

        if not self.alarm_is_enabled:
            enable_time = add_minutes(self.alarm_time, 1)
            if enable_time == (time.hour, time.minute):
                print "Automatic enable alarm"
                self.alarm_is_enabled = True
                self.gui.enable_alarm()
                event = {"event": "state",
                         "alarm_time": self.alarm_time,
                         "alarm_is_enabled": self.alarm_is_enabled,
                         "alarm_is_active": self.alarm_is_active}
                self.smart_home.send_event(event)
            return

        if self.alarm_time == (time.hour, time.minute):
            print "Alarm active"
            self.alarm_is_active = True
            self.backlight.set_brightness(100)
            self.sound.start()
            self.gui.start_alarm()

    def move_alarm(self, minutes):
        """Move alarm given number of minutes"""
        (new_hour, new_minute) = add_minutes(self.alarm_time, minutes)
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

        if self.alarm_is_enabled:
            print "Disable alarm"
            self.alarm_is_enabled = False
            self.gui.disable_alarm()
        else:
            print "Enable alarm"
            self.alarm_is_enabled = True
            self.gui.enable_alarm()

    def button_handler(self, button):
        """Handler for button events"""
        print "Button {0} pressed".format(button)

        if button == "+":
            self.move_alarm(minutes=CONFIG["time_increment"])
        elif button == "-":
            self.move_alarm(minutes=-CONFIG["time_increment"])
        elif button == "a":
            self.toggle_alarm()
        elif button == "b":
            pass
        else:
            return

        event = {"event": "button",
                 "button": button,
                 "alarm_time": self.alarm_time,
                 "alarm_is_enabled": self.alarm_is_enabled,
                 "alarm_is_active": self.alarm_is_active}
        self.smart_home.send_event(event)

    def command_handler(self, command):
        """Handler for incoming commands"""
        if command["command"] == "move_alarm":
            self.move_alarm(minutes=command["time_delta"])
        if command["command"] == "toggle_alarm":
            self.toggle_alarm()

        event = {"event": "command_complete",
                 "alarm_time": self.alarm_time,
                 "alarm_is_enabled": self.alarm_is_enabled,
                 "alarm_is_active": self.alarm_is_active}
        self.smart_home.send_event(event)

def add_minutes(old_time, minutes_to_add):
    """Add given amount of time, handling hour/minute overflow"""
    new_hour = old_time[0]
    new_minute = old_time[1] + minutes_to_add
    if new_minute >= 60:
        new_minute -= 60
        new_hour += 1
    if new_minute < 0:
        new_minute += 60
        new_hour -= 1
    return (new_hour, new_minute)
