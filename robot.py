# User defined
import constants as c
import motor
from networking import client as cl
from protobuf import dashboard_pb2
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
cim_top = motor.Victor(c.MOTOR_TOP)
cim_bot = motor.Victor(c.MOTOR_BOTTOM)
cim_lef = motor.Victor(c.MOTOR_LEFT)
cim_rig = motor.Victor(c.MOTOR_RIGHT)

def dashboard_update_send():
	global stick
	global enabled

	update = dashboard_pb2.RobotStaus()
	update.robot_state = enabled
	axes_list = update.axes.add()

	axes_list.joy1 = stick.get_axis(1)
	axes_list.joy2 = stick.get_axis(2)
	axes_list.joy3 = stick.get_axis(3)
	axes_list.joy4 = stick.get_axis(4)
	axes_list.joy5 = stick.get_axis(5)

	button_list = update.button_list.add()
	buttons = [False, False, False, False]

	pygame.event.pump()
	for event in pygame.event.get():
		if pygame.event.event_name(event.type) == "JoyButtonUp":
			# Do button stuff here
			if int(event.button) == 0: # A button
				buttons[0] = True
			elif int(event.button) == 1: # B Button
				buttons[1] = True
			elif int(event.button) == 2: # X Button?
				buttons[2] = True
			elif int(event.button) == 3: # Y Button?
				buttons[3] = True

	button_list.butA = buttons[0]
	button_list.butB = buttons[1]
	button_list.butX = buttons[2]
	button_list.butY = buttons[3]

	cli = cl.Client("10.23.34.3")
	cli.send(update.SerializeToString() + chr(182))

	# cleanup
	cli.end()
	del cli
	del update

def dashboard_update_receive():
	global enabled

	cli = cl.Client("10.23.34.3")
	update_str = cli.receive(chr(182))
	update = dashboard_pb2.RobotStaus()
	update.ParseFromString(update_str)

	enabled = update.robot_state

	# cleanup
	del update_str
	del update

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
	except Exception as e:
		print "".format(e.errno, e.strerror)
		enabled = False
		c.PWM.set_all_pwm(0, 0)
		sys.exit()

init()
periodic()
