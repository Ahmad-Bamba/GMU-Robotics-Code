import Adafruit_PCA9685
import constants as c

class Motor:
    "To make Adafruit_PCA9685"
    def __init__(self, channel):
        self.c = channel

    def set(self, value):
        "Converts value from -1 to 1 to a pulse"
        part = ((value + 1) / 2)
        normal = c.SERVO_MAX - c.SERVO_MIN
        real = part * normal
        pulse = constants.SERVO_MIN + real
        c.PWM.set_pwm(c, pulse)
