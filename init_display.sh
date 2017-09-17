#!/bin/bash
XAUTHORITY=~pi/.Xauthority DISPLAY=:0 xset s noblank
XAUTHORITY=~pi/.Xauthority DISPLAY=:0 xset s off
XAUTHORITY=~pi/.Xauthority DISPLAY=:0 xset -dpms
sudo modprobe fbtft_device name=sainsmart18 txbuflen=32768
FRAMEBUFFER=/dev/fb1 startx -- -dpi 60 -nocursor
