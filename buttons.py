"""Module for handling pushbuttons attached to GPIO"""
import platform
if platform.system() == "Linux":
    import RPi.GPIO as GPIO # pylint: disable=E0401

class Buttons(object): # pylint: disable=R0903
    """Button press handler"""

    PLUS_BUTTON = 35
    MINUS_BUTTON = 33
    A_BUTTON = 31
    B_BUTTON = 29

    BUTTON_MAP = {MINUS_BUTTON: "-",
                  PLUS_BUTTON: "+",
                  A_BUTTON: "a",
                  B_BUTTON: "b"}

    def __init__(self, button_handler):
        if platform.system() != "Linux":
            return
        self.button_handler = button_handler

        io_mode = GPIO.getmode()

        if io_mode is GPIO.BCM:
            raise ValueError("RPi GPIO mode was set to BCM.")

        if io_mode is None:
            GPIO.setmode(GPIO.BOARD)

        GPIO.setup(self.BUTTON_MAP.keys(), GPIO.IN, pull_up_down=GPIO.PUD_UP)

        for button in self.BUTTON_MAP:
            GPIO.add_event_detect(button,
                                  GPIO.FALLING,
                                  callback=self.callback,
                                  bouncetime=200)

    def callback(self, channel):
        """Button press callback"""
        print channel
        self.button_handler(self.BUTTON_MAP[channel])
