
import pir
import subprocess
from datetime import datetime
import led

pir_sensor = pir.sensor(4)
irled = led.sensor(3)  # Instantiate led class and assign the pin the BCM3
irled.off()  # Turn led off


while True:
    hour = int(datetime.strftime(datetime.now(), '%H'))
#   if hour > 0: # switch on for commissioning
    if hour >= 22  or hour <= 6:
        if pir_sensor.read(500) == 1:
            print("PIR triggered")
            irled.on()
            subprocess.run(["/usr/bin/python3", "/home/pi/HogPi/app/remoteCam/video.py"])
            irled.off()
