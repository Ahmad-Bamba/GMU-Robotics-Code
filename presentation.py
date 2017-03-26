import RPi.GPIO as GPIO
import pygame
import sys

frequency = 50
motor_one_pin = 14
motor_two_pin = 17
right_stick_y = 5
safe_sleep = 0.05
stick_port = 0
# pwm_min = 250
# pwm_max = 410
stick = None
motor_one = None
motor_two = None

def init():
    global motor_one
    global motor_two
    global stick
    global stick_port

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor_one_pin, GPIO.OUT)
    GPIO.setup(motor_two_pin, GPIO.OUT)
    motor_one = GPIO.PWM(motor_one_pin, frequency)
    motor_one.start(50)
    motor_two = GPIO.PWM(motor_two_pin, frequency)
    motor_two.start(50)

    pygame.joystick.init()
    pygame.display.init()
    if not (pygame.joystick.get_count() > 0):
        print "No joysticks detected, quiting..."
        sys.exit()
    stick = pygame.joystick.Joystick(stick_port)
    stick.init()

def periodic():
    enabled = True
    while enabled:
        try:
            pygame.event.pump()
            for event in pygame.event.get():
                if pygame.event.event_name(event.type) == "JoyButtonUp":
                    # Do button stuff here
                    if int(event.button) == 0:  # A button
                        print "A"
                    elif int(event.button) == 1:  # B Button
                        print "B"
                    elif int(event.button) == 2:  # X Button?
                        print "X"
                    elif int(event.button) == 3:  # Y Button?
                        print "Y"

            motor_one.ChangeDutyCycle(50.0 + (50.0 * stick.get_axis(right_stick_y)))
            motor_two.ChangeDutyCycle(50.0 + (50.0 * stick.get_axis(right_stick_y)))
        except KeyboardInterrupt:
            print "Keyboard Interrupt!"
            motor_one.stop()
            motor_two.stop()
            GPIO.cleanup()
            print "Closing presentation mode"
            enabled = False

if __name__ == '__main__':
    init()
    periodic()
