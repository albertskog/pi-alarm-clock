#!/bin/bash

XAUTHORITY=~pi/.Xauthority xset -display :0 s off         # don't activate screensaver
XAUTHORITY=~pi/.Xauthority xset -display :0 -dpms         # disable DPMS (Energy Star) features.
XAUTHORITY=~pi/.Xauthority xset -display :0 s noblank     # don't blank the video device

SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

cd $SCRIPTPATH
/usr/bin/screen -dmS alarm sh -c "DISPLAY=:0 /usr/bin/python "$SCRIPTPATH"/alarm_clock.py; exec bash"
