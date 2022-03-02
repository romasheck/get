import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

leds = [21, 20, 16, 12, 7, 8, 25, 24]
aux = [22, 23, 27, 18, 15, 14, 3, 2]

for i in 0, 1, 2, 3, 4, 5, 6, 7:
    GPIO.setup (leds[i], GPIO.OUT)

for i in 0, 1, 2, 3, 4, 5, 6, 7:
    GPIO.setup (aux[i], GPIO.IN)


GPIO.output (leds, 0)

GPIO.cleanup()






