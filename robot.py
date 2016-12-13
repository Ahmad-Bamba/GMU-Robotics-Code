# User defined
import constants as c
import networking as net
import RobotExceptions as rexept
import motor
# import ir

# 3rd Party
import pygame
import sys
import time
import socket

# Testing only
import random

# set period to 20ms, which is what the VictorSPs need
c.PWM.set_pwm_freq(50)
enabled = True
stick = None

# Networking
robosock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# init hardware
cim_top = motor.Victor(c.MOTOR_TOP)
cim_bot = motor.Victor(c.MOTOR_BOTTOM)
cim_lef = motor.Victor(c.MOTOR_LEFT)
cim_rig = motor.Victor(c.MOTOR_RIGHT)

def init():
	global stick

	pygame.joystick.init()
	pygame.display.init()
	if not (pygame.joystick.get_count() > 0):
		print "No joysticks detected, quiting..."
		sys.exit()
	stick = pygame.joystick.Joystick(c.JOYSTICK)
	stick.init()

	while True:
		time.sleep(1)
		try:
			robosock.connect((c.LAPTOP_IP, 9685))
			break
		except Exception as e:
			print e
			print "Connection failed, check to make sure static ip set up correctly"
			print "Retrying..."

def periodic():
	global stick
	global enabled
	global robosock

	try:
		while True:
			message = net.recieveFromDashboard(robosock, c.MSG_STANDARD)
			if message[:2] == "+U":
				# print message[2]
				enabled = bool(int(message[2]))
				if message[3] == ":":
					print "Message from socket: " + message[4:24]

			dashupdate = "-U" + str(int(enabled)) + ":" + ("%.3f" % round(random.uniform(-1, 1), 3)) + ":" + ("%.3f" % round(random.uniform(-1, 1), 3)) + ":" + ("%.3f" % round(random.uniform(-1, 1), 3)) + ":" + ("%.3f" % round(random.uniform(-1, 1), 3)) + "$"
			net.sendToDashboard(robosock, dashupdate)

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
	except rexept.KillSwitch:
		print "KillSwitch activated!"
		enabled = False
		c.PWM.set_all_pwm(0, 0)
		sys.exit()

init()
periodic()
