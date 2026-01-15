import RPi.GPIO as GPIO
import time
import subprocess
def kick(file_path):
    subprocess.call(['aplay', file_path])
button = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(button, GPIO.IN)
GPIO.input(button)
while True:
    if GPIO.input(button) == 0:
        kick("kick7cut.wav")
        time.sleep(0.25)
GPIO.cleanup()