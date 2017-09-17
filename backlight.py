"""Module for handling TFT backlight"""
import platform
if platform.system() == "Linux":
    import RPi.GPIO as GPIO # pylint: disable=E0401

class Backlight(object): # pylint: disable=R0903
    """Backlight control"""
    PIN = 7

    def __init__(self, brightness_percent=3):
        if platform.system() != "Linux":
            return

        io_mode = GPIO.getmode()

        if io_mode is GPIO.BCM:
            raise ValueError("RPi GPIO mode was set to BCM.")

        if io_mode is None:
            GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.PIN, GPIO.OUT)

        self.backlight = GPIO.PWM(self.PIN, 100)
        self.backlight.start(100)
        self.set_brightness(brightness_percent)

    def set_brightness(self, brightness_percent):
        """Set backlight."""
        try:
            self.backlight.ChangeDutyCycle(brightness_percent)
        except AttributeError:
            pass
        print "Set backlight: {0}%".format(brightness_percent)
