import RPi.GPIO as GPIO
import time

# Too bad python doesn't have const...
pin = 11
c = 5

# Set up GPIO stuff

GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, 50)

# Left: 5, Center: 7.5, Right: 10

pwm.start(c)

try:
	while 1:
		pwm.ChangeDutyCycle(7.5)
		time.sleep(1)
		pwm.ChangeDutyCycle(10)
		time.sleep(1)
		pwm.ChangeDutyCycle(5)
		time.sleep(1)
except KeyboardInterrupt:
	pwm.stop()
	GPIO.cleanup()
	print "whatever"
