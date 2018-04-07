#!/bin/bash

XAUTHORITY=~pi/.Xauthority xset -display :0 s off         # don't activate screensaver
XAUTHORITY=~pi/.Xauthority xset -display :0 -dpms         # disable DPMS (Energy Star) features.
XAUTHORITY=~pi/.Xauthority xset -display :0 s noblank     # don't blank the video device

cd /home/pi/pi-alarm-dev
/usr/bin/screen -dmS alarm sh -c "DISPLAY=:0 /usr/bin/python /home/pi/pi-alarm-dev/alarm_clock.py; exec bash"
