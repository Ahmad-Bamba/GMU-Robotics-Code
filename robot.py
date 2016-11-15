# User defined
import constants as c
import pygame
import motor
# import ir

# 3rd Party
import pygame
import sys
import time

# init hardware
cim = motor.Motor(c.MOTOR_TOP)

def init():
    pygame.joystick.init()
    if not (pygame.joystick.get_count() > 0):
        print "No joysticks detected, quiting..."
        sys.exit()
    stick = pygame.joystick.Joystick(c.JOYSTICK)
    stick.init()

def periodic():
    moving = False
    try:
        while enabled:
            pygame.event.pump()
            for event in pygame.event.get():
                if pygame.event.event_name(event.type) == "JoyButtonUp":
                    # Do button stuff here
                    if int(event.button) == 0: # A button
                        print "A"
                        if !moving:
                            cim.set(1)
                            moving = True
                        else:
                            cim.set(0)
                            moving = False
    except KeyboardInterrupt:
        sys.exit()
