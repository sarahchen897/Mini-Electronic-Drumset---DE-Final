import board
i2c = board.I2C()
from adafruit_ads1x15 import ADS1015, AnalogIn, ads1x15
ads = ADS1015(i2c)
while True:
    chan = AnalogIn(ads, ads1x15.Pin.A0)
    print(chan.value, chan.voltage)