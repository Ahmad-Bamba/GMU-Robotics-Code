# User defined
import constants as c
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
robosock.bind(socket.gethostname(), 9685)
robosock.listen(5)

# init hardware
cim_top = motor.Victor(c.MOTOR_TOP)
cim_bot = motor.Victor(c.MOTOR_BOTTOM)
cim_lef = motor.Victor(c.MOTOR_LEFT)
cim_rig = motor.Victor(c.MOTOR_RIGHT)


def sendToDashboard(sock, msg):
    totalsent = 0
    while totalsent < len(msg):
        sent = sock.send(msg[totalsent:])
        if sent == 0:
            raise RuntimeError("Socket connection broken!")
        totalsent = totalsent + sent

def recieveFromDashboard(sock, msg):
    chunks = []
    bytes_recd = 0
    while bytes_recd < len(msg):
        chunk = sock.recv(min(len(msg) - bytes_recd, 2048))
        if chunk == '':
            raise RuntimeError("Socket connection broken!")
        chunks.append(chunk)
        bytes_recd = bytes_recd + len(chunk)
    return ''.join(chunks)

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
	global robosock

	try:
		while True:
			(cli, address) = robosock.accept()
			print "Recieved connection from " + str(address)
			dashupdate = [ ["RobotState", str(enabled)],  ["Axis0", str(random.uniform(-1, 1))], ["Axis4", str(random.uniform(-1, 1))], ["Axis2", str(random.uniform(-1, 1))], ["Axis3", str(random.uniform(-1, 1))] ]
			print str(dashupdate)
			# sendToDashboard(str(dashupdate))

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

init()
periodic()
