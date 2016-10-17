# User defined
import constants as c
import pygame
import motor
import ir
# 3rd Party
import pygame
import sys
import time

# init hardware TODO: Get IRs set up later
top    = motor.Motor(c.MOTOR_TOP)
left   = motor.Motor(c.MOTOR_LEFT)
bottom = motor.Motor(c.MOTOR_BOTTOM)
right  = motor.Motor(c.MOTOR_RIGHT)
stick  = None

# E stop variable
enabled = True

def init():
    pygame.joystick.init()
    if not (pygame.joystick.get_count() > 0):
        print "No joysticks detected, quiting..."
        sys.exit()
    

def periodic():
    while enabled:
        pygame.event.pump()
