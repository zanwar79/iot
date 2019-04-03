gcalcli --nostarted --calendar "" agenda --nocolor | cut -d " " -f 4- | head -2 | tail -1 | sed "s/^ *//g" | sed "s/    / /g" > /home/pi/rpi-rgb-led-matrix-master/today
