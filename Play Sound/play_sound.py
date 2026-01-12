#When a hit (above 1.2 volts) is detected, the snare audio file will play and the code will stop
import board
import time
import subprocess
i2c = board.I2C()
from adafruit_ads1x15 import ADS1015, AnalogIn, ads1x15
ads = ADS1015(i2c)
def snare(file_path):
    subprocess.call(['aplay', file_path])
def runtime(seconds):
    endtime = time.time() + seconds
    with open('output.txt', 'w') as f:
        while time.time() < endtime:
            chan = AnalogIn(ads, ads1x15.Pin.A0)
            if chan.voltage > 1.2:
                snare("snare2.wav")
                break
runtime(3)