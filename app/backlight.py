"""Module for handling TFT backlight"""
import platform
if platform.system() == "Linux":
    import pigpio # pylint: disable=E0401

class Backlight(object): # pylint: disable=R0903
    """Backlight control"""
    PIN = 4

    def __init__(self, brightness_percent=3):
        if platform.system() != "Linux":
            return
        self.gpio = pigpio.pi()
        self.gpio.set_PWM_range(self.PIN, 100)
        self.set_brightness(brightness_percent)

    def set_brightness(self, brightness_percent):
        """Set backlight."""
        try:
            self.gpio.set_PWM_dutycycle(self.PIN, brightness_percent)
        except AttributeError:
            pass
        print "Set backlight: {0}%".format(brightness_percent)
