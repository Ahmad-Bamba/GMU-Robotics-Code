import RPi.GPIO as GPIO

pin = 0
cycle = 95

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
pwm = GPIO.PWM(pin, 50)
pwm.start(cycle)

try:
    while 1:
        GPIO.output(pin, GPIO.LOW)
except KeyboardInterrupt:
    pwm.stop()
    GPIO.cleanup()
