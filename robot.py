# User defined
import constants as c
import motor
# import ir

# 3rd Party
import pygame
import sys
import time
from networktables import NetworkTable
import logging
logging.basicconfig(level=logging.DEBUG)

# Robot Dashboard
dash = NetworkTable.getTable("Robot Dashboard")

# set period to 20ms, which is what the VictorSPs need
c.PWM.set_pwm_freq(50)
enabled = True
stick = None

# init hardware
cim_top = motor.Victor(c.MOTOR_TOP)
cim_bot = motor.Victor(c.MOTOR_BOTTOM)
cim_lef = motor.Victor(c.MOTOR_LEFT)
cim_rig = motor.Victor(c.MOTOR_RIGHT)

def updateDash(updates):
	"""2D array where the first element of each row is the key and the second is a value"""
	for i in xrange(len(updates)):
		dash.putValue(updates[i][0], updates[i][1])

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
	global enabled

	try: # TODO: Test this crap!
		while True:
			dashupdate = [ ("Robot State", enabled), ("Axis 0", stick.get_axis(0)),\
			 ("Axis 3", stick.get_axis(3)), ("Axis 2", stick.get_axis(2)), ("Axis 4", stick,get_axis(4))  ]
			updateDash(dashupdate)
			if enabled:
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
						elif int(event.button) == 7: # Back Button?
							print "Start"
							if enabled:
								enabled = False
								c.PWM.set_all_pwm(0, 0)
								print "Robot disabled!"
							else:
								enabled = True
								print "Robot enabled"
						elif int(event.button) == 8: # Start button?
							print "Start"
							print "Kill switch activated!"
							raise c.KillSwitch()

				for i in xrange(stick.get_numaxes()):
					if i == 1:
						if abs(stick.get_axis(1)) > c.THRESHOLD:
							cim_lef.set(stick.get_axis(1) * -1)
							cim_rig.set(stick.get_axis(1))
						else:
							cim_lef.set(0)
							cim_rig.set(0)
					if i == 3:
						if abs(stick.get_axis(3)) > c.THRESHOLD:
							cim_top.set(stick.get_axis(3) * -1)
							cim_bot.set(stick.get_axis(3))
						else:
							cim_top.set(0)
							cim_bot.set(0)
	except KeyboardInterrupt:
		print "Exited by user request"
		enabled = False
		c.PWM.set_all_pwm(0, 0)
		sys.exit()
	except c.KillSwitch:
		print "Code terminated through kill switch!"
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
