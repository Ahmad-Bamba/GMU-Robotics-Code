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
    movingb = False
    movingx = False
    movingy = False

    enabled = True
    try:
        while enabled:
            pygame.event.pump()
            for event in pygame.event.get():
                if pygame.event.event_name(event.type) == "JoyButtonUp":
                    # Do button stuff here
                    if int(event.button) == 0: # A button
                        print "A"
                        if not movinga:
                            print "cim_top.set(.1)"
			                cim_top.set(.1)
                            movinga = True
                        else:
                            print "cim_top.set(0)"
			                cim_top.set(0)
                            movinga = False
		            elif int(event.button) == 2:
			            print "B"
                        if not movingb:
                            print "cim_lef.set(.1)"
                            cim_lef.set(.1)
                            movingb = True
                        else:
                            print "cim_lef.set(0)"
                            cim_lef.set(0)
                            movingb = False
                    elif int(event.button) == 3:
                        print "X"
                        if not movingx:
                            print "cim_rig.set(.1)"
                            cim_rig.set(.1)
                            movingx = True
                        else:
                            print "cim_rig.set(0)"
                            cim_rig.set(0)
                            movingx = False
                    elif int(event.button) == 4:
                        print "Y"
                        if not movingy:
                            print "cim_bot.set(.1)"
                            cim_bot.set(.1)
                            movingy = True
                        else:
                            print "cim_bot.set(0)"
                            cim_bot.set(0)
                            movingy = False
    except KeyboardInterrupt:
        enabled = False
	    c.PWM.set_all_pwm(0, 0)
        sys.exit()

init()
periodic()
