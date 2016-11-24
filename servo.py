import RPi.GPIO as GPIO
import time

# Too bad python doesn't have const...

pin = 17
c = 95

# Set up GPIO stuff

GPIO.setmod(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, 20)

pwm.start(c)

try:
	while 1:
		
