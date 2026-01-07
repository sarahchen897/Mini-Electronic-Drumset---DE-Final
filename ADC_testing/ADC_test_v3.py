#The ADC reads the input value , voltage, and time between each ADC reading, then prints it
#It runs for 3 seconds and outputs the values to a text file
import board
import time
i2c = board.I2C()
from adafruit_ads1x15 import ADS1015, AnalogIn, ads1x15
ads = ADS1015(i2c)
def runtime(seconds):
    endtime = time.time() + seconds
    with open('output.txt', 'w') as f:
        while time.time() < endtime:
            start = time.perf_counter()
            chan = AnalogIn(ads, ads1x15.Pin.A0)
            print(chan.value, chan.voltage)
            end = time.perf_counter()
            elapsed = end - start
            print (elapsed)
runtime(3)
    