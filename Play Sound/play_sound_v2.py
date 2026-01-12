#When a hit (above 1.5 volts) is detected, the snare audio file will play
#There will be a delay of 0.25 seconds after the audio files plays, and the code runs for 10 seconds
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
    while time.time() < endtime:
        chan = AnalogIn(ads, ads1x15.Pin.A0)
        if chan.voltage > 1.5:
            snare("snare2.wav")
            time.sleep(0.25)
runtime(10)