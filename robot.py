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
cim_top = motor.Motor(c.MOTOR_TOP)
cim_bot = motor.Motor(c.MOTOR_BOTTOM)
cim_lef = motor.Motor(c.MOTOR_LEFT)
cim_rig = motor.Motor(c.MOTOR_RIGHT)

def init():
    pygame.joystick.init()
    pygame.display.init()
    if not (pygame.joystick.get_count() > 0):
        print "No joysticks detected, quiting..."
        sys.exit()
    stick = pygame.joystick.Joystick(c.JOYSTICK)
    stick.init()

def periodic():
    movinga = False
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
                            print "cim.set(.2)"
			    cim.set(.2)
                            moving = True
                        else:
                            print "cim.set(0)"
			    cim.set(0)
                            moving = False
		    if int(event.button) == 2:
			if
    except KeyboardInterrupt:
        enabled = False
	c.PWM.set_all_pwm(0, 0)
        sys.exit()

init()
periodic()
