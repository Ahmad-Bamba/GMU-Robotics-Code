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
class EmergencyStop( Exception ):
    pass

def init():
    pygame.joystick.init()
    if not (pygame.joystick.get_count() > 0):
        print "No joysticks detected, quiting..."
        sys.exit()
    stick = pygame.joystick.Joystick(0)
    stick.init()

def periodic():
    try:
        while enabled:
            pygame.event.pump()
            for event in pygame.event.get():
                if pygame.event.event_name(event.type) == "JoyButtonUp":
                    if int(event.button) == 7:
                        print "ERROR: Emergency stop triggered!"
                        print "Printing event traceback que..."
                        print str(pygame.event.get())
                        enabled = False
                        raise EmergencyStop
                    else:
                        # Do button stuff here
                        if int(event.button) == 0:
                            # control the hatch
            
    except EmergencyStop:
        pass
