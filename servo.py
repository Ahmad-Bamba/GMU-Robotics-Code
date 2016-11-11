import RPi.GPIO as GPIO
import time

pin = 17
cycle = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, 50)
pwm.start(cycle)

try:
    while 1:
        GPIO.output(pin, 0)
	print "0"
	time.sleep(1)
	GPIO.output(pin, 5)
	print "5"
	time.sleep(1)
	GPIO.output(pin, 10)
	print "10"
	time.sleep(1)
	GPIO.output(pin, 50)
	print "50"
	time.sleep(1)
	GPIO.output(pin, 75)
	print "75"
	time.sleep(1)
	GPIO.output(pin, 128)
	print "128"
	time.sleep(1)
except KeyboardInterrupt:
    print "shrecking"
    pwm.stop()
    GPIO.cleanup()
