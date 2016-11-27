# User defined
import constants as c
import motor
# import ir

# 3rd Party
import pygame
import sys
import time

# set period to 20ms, which is apparently what the VictorSPs need
c.PWM.set_pwm_freq(50)
enabled = True

# init hardware
cim = motor.Motor(c.MOTOR_TOP)

def init():
    pygame.joystick.init()
    pygame.display.init()
    if not (pygame.joystick.get_count() > 0):
        print "No joysticks detected, quiting..."
        sys.exit()
    stick = pygame.joystick.Joystick(c.JOYSTICK)
    stick.init()

def periodic():
    moving = False
    enabled = True
    try:
        while enabled:
            pygame.event.pump()
            for event in pygame.event.get():
                if pygame.event.event_name(event.type) == "JoyButtonUp":
                    # Do button stuff here
                    if int(event.button) == 0: # A button
                        print "A"
                        if not moving:
                            cim.set(1)
                            moving = True
                        else:
                            cim.set(0)
                            moving = False
    except KeyboardInterrupt:
        enabled = False
        sys.exit()

init()
periodic()
