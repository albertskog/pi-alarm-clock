# Raspberry Pi Alarm Clock
This project uses a Raspberry Pi, a small display, some buttons and speakers to create a small, network connected and configurable alarm clock.

## Parts used

* Raspberry Pi A+
* USB wifi dongle
* HY-1.8 SPI 128x160 TFT display
* Pushbuttons
* PC speakers

## Preparations
Setting up the Pi to run X on the TFT requires the use of [fbtft](https://github.com/notro/fbtft/), which is already included in Raspbian. Many small LCD and TFT displays are supported, see [https://github.com/notro/fbtft/wiki/More-LCD-Modules](https://github.com/notro/fbtft/wiki/More-LCD-Modules).

First step is to make sure the Pi is running up-to-date firmware:

```
sudo rpi-update
```

The screen should stay on at all times and not go in to powersave or screensaver mode. This can be achieved by editing the folllowing file:

```
vi ~/.config/lxsession/LXDE-pi/autostart
# Add:
@xset s off         # don't activate screensaver
@xset -dpms         # disable DPMS (Energy Star) features.
@xset s noblank     # don't blank the video device
```

Next, load the fbtft_device kernel module. The display uses a chip called st7735, which is supported under the name ```sainsmart18```. Some displays may require setting ```bgr``` to get the colors in the right order. Setting ```txbuflen``` to 32 kB ensures smoother operation.

```
sudo modprobe fbtft_device name=sainsmart18 bgr=1 txbuflen=32768
```

X needs to be configured to output to this framebuffer instead of the default one. Assuming the TFT is the only display used on the system, the following file may be edited:

```
vi /usr/share/X11/xorg.conf.d/99-fbturbo.conf
# Replace fb0 with fb1
```

To be allowed to run X without root, we can reconfigure X11:

```
dpkg-reconfigure x11-common
# Choose all
```

X can now be started on the TFT. If no mouse is used, the cursor can be disabled here.

```
FRAMEBUFFER=/dev/fb1 startx -- -dpi 60 -nocursor
```

Finally, the clock script can be started:

```
DISPLAY=:0 python alarm-clock.py
```

Or, for development:

```
export DISPLAY=":0"
nodemon alarm-clock.py
```

The script also runs on OS X (without specifying the display).
