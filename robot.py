# User defined
import constants as c
import motor
# import ir

# 3rd Party
import pygame
import sys
import time

# set period to 20ms, which is what the VictorSPs need
c.PWM.set_pwm_freq(50)
enabled = True
stick = None

# init hardware
cim_top = motor.Motor(c.MOTOR_TOP)
cim_bot = motor.Motor(c.MOTOR_BOTTOM)
cim_lef = motor.Motor(c.MOTOR_LEFT)
cim_rig = motor.Motor(c.MOTOR_RIGHT)

def init():
	global stick

	pygame.joystick.init()
	pygame.display.init()
	if not (pygame.joystick.get_count() > 0):
		print "No joysticks detected, quiting..."
		sys.exit()
	stick = pygame.joystick.Joystick(c.JOYSTICK)
	stick.init()

def periodic():
	global stick

	enabled = True
	try:
		while enabled:
			pygame.event.pump()
			for event in pygame.event.get():
				if pygame.event.event_name(event.type) == "JoyButtonUp":
					# Do button stuff here
					if int(event.button) == 0: # A button
						print "A"
					elif int(event.button) == 1: # B Button
						print "B"
					elif int(event.button) == 2: # X Button?
						print "X"
					elif int(event.button) == 3: # Y Button?
						print "Y"

			for i in xrange(stick.get_numaxes()):
				if i == 1:
					if abs(stick.get_axis(1)) > c.THRESHOLD:
						cim_lef.set(stick.get_axis(1))
						cim_rig.set(stick.get_axis(1))
					else:
						cim_lef.set(0)
						cim_rig.set(0)
				if i == 3:
					if abs(stick.get_axis(3)) > c.THRESHOLD:
						cim_top.set(stick.get_axis(3))
						cim_bot.set(stick.get_axis(3))
					else:
						cim_top.set(0)
						cim_bot.set(0)
	except KeyboardInterrupt:
		print "Exited by user requed"
		enabled = False
		c.PWM.set_all_pwm(0, 0)
		sys.exit()
	except Exception as e:
		print "".format(e.errno, e.strerror)
		enabled = False
		c.PWM.set_all_pwm(0, 0)
		sys.exit()

init()
periodic()
