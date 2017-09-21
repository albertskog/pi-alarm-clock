"""Module for playing alarm sound"""
import threading
import subprocess
import time
import platform

class Sound(object):
    """Alarm sound"""
    def __init__(self):
        self.stop_event = threading.Event()
        self.stop_event.clear()

        if platform.system() == "Linux":
            self.sound_player = play_alarm_linux
        elif platform.system() == "Darwin":
            self.sound_player = play_alarm_mac
        else:
            print "Unknown operating system!"
            return

        self.alarm_sound = ""

    def start(self):
        """Start alarm sound"""
        self.stop_event.clear()
        self.alarm_sound = threading.Thread(target=self.sound_player,
                                            args=(self.stop_event,))
        self.alarm_sound.start()

    def stop(self):
        """Stop alarm sound"""
        self.stop_event.set()
        self.alarm_sound.join()

def play_alarm_linux(stop_event):
    """Play the alarm sound untill stopped."""

    proc = subprocess.Popen(["omxplayer",
                             "--loop",
                             "--vol",
                             "-4000",
                             "sound.mp3"],
                            stdout=subprocess.PIPE,
                            stdin=subprocess.PIPE,
                            stderr=subprocess.PIPE)

    last_volume_increase_time = time.time()
    while not stop_event.is_set():
        time.sleep(0)

        if time.time() - last_volume_increase_time >= 10:
            last_volume_increase_time = time.time()
            proc.stdin.write('+')

    proc.stdin.write('q')

def play_alarm_mac(stop_event):
    """Play the alarm sound untill stopped."""
    print "Playing alarm sound"
    while not stop_event.is_set():
        time.sleep(0)
