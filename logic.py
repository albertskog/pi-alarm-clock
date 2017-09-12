from datetime import datetime
import time

class Logic:

    def __init__(self, gui):
        self.Gui = gui
        self.update_time()

    def update_time(self):
        self.Gui.frame.after(1000, self.update_time)
        time = str(datetime.now().time())[0:5]
        self.Gui.time_variable.set(time)
