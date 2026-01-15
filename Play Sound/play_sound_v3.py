#added code for kick drum and bumper switch
import board
import time
import subprocess
import RPi.GPIO as GPIO
i2c = board.I2C()
from adafruit_ads1x15 import ADS1015, AnalogIn, ads1x15
ads = ADS1015(i2c)
def snare(file_path):
    subprocess.call(['aplay', file_path])
def kick(file_path):
    subprocess.call(['aplay', file_path])
button = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)
GPIO.input(button)
def runtime(seconds):
    endtime = time.time() + seconds
    while time.time() < endtime:
        chan = AnalogIn(ads, ads1x15.Pin.A0)
        if chan.voltage > 1.5:
            snare("snare2.wav")
            time.sleep(0.25)
        if GPIO.input(button) == 0:
            kick("kick7cut.wav")
            time.sleep(0.25)
    GPIO.cleanup()
runtime(10)