# User defined
import constants as c
import pygame
import motor
# import ir

# 3rd Party
import pygame
import sys
import time

# init hardware TODO: Get IRs set up later
top    = motor.Motor(c.MOTOR_TOP)
left   = motor.Motor(c.MOTOR_LEFT)
bottom = motor.Motor(c.MOTOR_BOTTOM)
right  = motor.Motor(c.MOTOR_RIGHT)
screw  = motor.Motor(c.MOTOR_SCREW)
stick  = None

# E stop variable
enabled = True
class EmergencyStop(Exception):
    pass

# Make it easier to handle inputs
def handle(axisarray):
    # Designed to make sure we don't strafe and rotate at the same time
    if len(axisarray) != 6:
        print "ERROR: Invalid Axis Input!"
        return -1

    if abs(axisarray[2]) > c.THRESHOLD and abs(axisarray[0]) < c.THRESHOLD and abs(axisarray[1]) < c.THRESHOLD and abs(axisarray[5]) < c.THRESHOLD:
        top.set(-axisarray[2])
        left.set(-axisarray[2])
        bottom.set(-axisarray[2])
        right.set(-axisarray[2])
    elif abs(axisarray[5]) > c.THRESHOLD and abs(axisarray[0]) < c.THRESHOLD and abs(axisarray[1]) < c.THRESHOLD and abs(axisarray[2]) < c.THRESHOLD:
        top.set(-axisarray[5])
        left.set(-axisarray[5])
        bottom.set(-axisarray[5])
        right.set(-axisarray[5])
    elif abs(axisarray[0]) > c.THRESHOLD and abs(axisarray[0]) > abs(axisarray[1]):
        # The user is trying to go side to side
        top.set(axisarray[0])
        bottom.set(axisarray[0])
    elif abs(axisarray[1]) > c.THRESHOLD and abs(axisarray[1]) > abs(axisarray[0]):
        # The user is trying to go up and down
        left.set(axisarray[1])
        right.set(axisarray[1])
    else:
        top.set(0)
        left.set(0)
        bottom.set(0)
        right.set(0)
        stick.set(0)

    if abs(axisarray[4]) > c.THRESHOLD:
        screw.set(axisarray[4])

    return 0

def init():
    pygame.joystick.init()
    if not (pygame.joystick.get_count() > 0):
        print "No joysticks detected, quiting..."
        sys.exit()
    stick = pygame.joystick.Joystick(c.JOYSTICK)
    stick.init()

def periodic():
    try:
        while enabled:
            pygame.event.pump()
            for event in pygame.event.get():
                if pygame.event.event_name(event.type) == "JoyButtonUp":
                    if int(event.button) == 7:
                        print "ERROR: Emergency stop triggered!"
                        print "Printing event traceback queue..."
                        print str(pygame.event.get())
                        enabled = False
                        raise EmergencyStop
                    # Do button stuff here
                    elif int(event.button) == 0: # A button
                        # control the hatch
                        pass
                    elif int(event.button) == 1: # B button
                        # grab claw
                        pass
            stickaxis = [stick.get_axis(0), stick.get_axis(1), stick.get_axis(2), stick.get_axis(3), stick.get_axis(4), stick.get_axis(5)]
            handle(stickaxis)
    except EmergencyStop:
        pass
