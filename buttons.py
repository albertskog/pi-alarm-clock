"""Module for handling pushbuttons attached to GPIO"""
import platform
if platform.system() == "Linux":
    import RPi.GPIO as GPIO # pylint: disable=E0401

class Buttons(object): # pylint: disable=R0903
    """Button press handler"""

    plus_button = 35
    minus_button = 33
    a_button = 31
    b_button = 29

    buttons = {"plus_button": plus_button,
               "minus_button": minus_button,
               "a_button": a_button,
               "b_button": b_button}

    def __init__(self, button_handler):
        if platform.system() != "Linux":
            return
        self.button_handler = button_handler

        io_mode = GPIO.getmode()

        if io_mode is GPIO.BCM:
            raise ValueError("RPi GPIO mode was set to BCM.")

        if io_mode is None:
            GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.buttons.values(), GPIO.IN, pull_up_down=GPIO.PUD_UP)

        for button in self.buttons.values():
            GPIO.add_event_detect(button,
                                  GPIO.FALLING,
                                  callback=self.callback,
                                  bouncetime=200)

    def callback(self, channel):
        """Button press callback"""
        print channel
        self.button_handler(channel)
