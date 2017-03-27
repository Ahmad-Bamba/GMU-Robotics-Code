import RPi.GPIO as GPIO
import pygame
import sys

frequency = 50
motor_top_pin = 14
motor_bot_pin = 17
motor_lef_pin = 15
motor_rig_pin = 18
right_stick_y = 5
safe_sleep = 0.05
stick_port = 0
threshold = 0.01
# pwm_min = 250
# pwm_max = 410
stick = None
motor_top = None
motor_bot = None
motor_lef = None
motor_rig = None

def joystick_floor(x):
    global threshold
    return x if abs(x) > threshold else 0


def joystick_limit(x):
    return x if abs(x) < 50 else 50 if x > 0 else -50

def init():
    global motor_top
    global motor_bot
    global motor_lef
    global motor_rig

    global stick

    global stick_port
    global motor_top_pin
    global motor_bot_pin
    global motor_rig_pin
    global motor_lef_pin

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(motor_top_pin, GPIO.OUT)
    GPIO.setup(motor_bot_pin, GPIO.OUT)
    GPIO.setup(motor_lef_pin, GPIO.OUT)
    GPIO.setup(motor_rig_pin, GPIO.OUT)

    motor_top = GPIO.PWM(motor_top_pin, frequency)
    motor_bot = GPIO.PWM(motor_bot_pin, frequency)
    motor_lef = GPIO.PWM(motor_lef_pin, frequency)
    motor_rig = GPIO.PWM(motor_rig_pin, frequency)

    motor_top.start(50)
    motor_bot.start(50)
    motor_lef.start(50)
    motor_rig.start(50)

    pygame.joystick.init()
    pygame.display.init()
    if not (pygame.joystick.get_count() > 0):
        print "No joysticks detected, quiting..."
        sys.exit()
    stick = pygame.joystick.Joystick(stick_port)
    stick.init()

def periodic():
    global motor_top
    global motor_bot
    global motor_lef
    global motor_rig

    global stick

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
            hori = joystick_floor(stick.get_axis(0))
            vert = joystick_floor(stick.get_axis(1))
            rota = joystick_floor(stick.get_axis(3) - stick.get_axis(2))

            motor_top.ChangeDutyCycle(50 + joystick_limit(50 * (hori + rota)))
            motor_bot.ChangeDutyCycle(50 - joystick_limit(50 * (hori - rota)))
            motor_lef.ChangeDutyCycle(50 + joystick_limit(50 * (vert + rota)))
            motor_rig.ChangeDurtCycle(50 - joystick_limit(50 * (vert - rota)))
        except KeyboardInterrupt:
            print "Keyboard Interrupt!"
            motor_rig.stop()
            motor_lef.stop()
            motor_top.stop()
            motor_bot.stop()
            GPIO.cleanup()
            print "Closing presentation mode"
            enabled = False

if __name__ == '__main__':
    init()
    periodic()
