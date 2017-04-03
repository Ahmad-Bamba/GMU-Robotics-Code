import RPi.GPIO as GPIO
import pygame
import sys

frequency = 100
motor_top_pin = 14
motor_bot_pin = 17
motor_lef_pin = 27
motor_rig_pin = 22
right_stick_y = 5
safe_sleep = 0.05
stick_port = 0
threshold = 0.1
pwm_mid = 14.3
pwm_var = 7.2
stick = None
motor_top = None
motor_bot = None
motor_lef = None
motor_rig = None

def joystick_floor(x):
    global threshold
    return x if abs(x) > threshold else 0


def joystick_limit(x):
    return x if abs(x) < 1 else 1 if x > 0 else -1


def joy_to_raw(x):
    global pwm_mid
    global pwm_var

    return pwm_mid + (-x * pwm_var)


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
    i = 0
    while enabled:
        try:
            i += 1
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
            hori = joystick_floor(stick.get_axis(3))
            if i % 250 == 0:
                print "Hori: " + str(hori)
            vert = joystick_floor(stick.get_axis(1))
            if i % 250 == 0:
                print "Vert: " + str(vert)
            rota = joystick_floor(stick.get_axis(5))
            if i % 250 == 0:
                print "Rota: " + str(rota)

            motor_top.ChangeDutyCycle(joy_to_raw(joystick_limit(hori)))
            motor_bot.ChangeDutyCycle(joy_to_raw(-joystick_limit(hori)))
            motor_lef.ChangeDutyCycle(joy_to_raw(joystick_limit(vert)))
            motor_rig.ChangeDutyCycle(joy_to_raw(-joystick_limit(vert)))
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
