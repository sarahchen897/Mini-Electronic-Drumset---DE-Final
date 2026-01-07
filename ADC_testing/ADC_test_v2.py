#The ADC reads the input value and voltage, then prints it
#Then it calculates the time between each loop and prints the value
import board
import time
i2c = board.I2C()
from adafruit_ads1x15 import ADS1015, AnalogIn, ads1x15
ads = ADS1015(i2c)
while True:
    start = time.perf_counter()
    chan = AnalogIn(ads, ads1x15.Pin.A0)
    print(chan.value, chan.voltage)
    end = time.perf_counter()
    elapsed = end - start
    print (elapsed)