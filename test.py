from networking import Client
import dashboard_pb2
# import ir

# 3rd Party
import pygame
import sys
import time

enable = True

def dashboard_update_send():
	global stick
	global enabled

	#try:
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

	cli = Client("10.23.34.3")
	cli.send(update.SerializeToString() + chr(182))

	# cleanup
	cli.end()
	del cli
	del update
	#except Exception as e:
		#print "Caught error " + str(sys.exc_info()[0]) + "\n"
		#print "Failed to update dashboard"

def dashboard_update_receive():
	global enabled

	print "Receiving from dashboard..."

	#try:
	cli = Client("10.23.34.3")
	update_str = cli.receive(chr(182))
	update = dashboard_pb2.RobotStaus()
	update.ParseFromString(update_str)

	enabled = update.robot_state

	# cleanup
	del update_str
	del update
	#except Exception as e:
		#print "Caught error " + str(sys.exc_info()[0]) + "\n"
		#print "Failed to receive dashboard update"

def init():
	global stick
	pygame.joystick.init()
	pygame.display.init()
	if not (pygame.joystick.get_count() > 0):
		print "No joysticks detected, quiting..."
		sys.exit()
	stick = pygame.joystick.Joystick(0)
	stick.init()

def periodic():
	global enabled

	enabled = True
	try:
		while enabled:
			dashboard_update_receive()
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

			#dashboard_update_send()
	except KeyboardInterrupt:
		print "Exited by user request"
		enabled = False
		sys.exit()
	#except:
	#	print "Caught error " + str(sys.exc_info()[0]) + "\n"
	#	enabled = False
	#	sys.exit()

init()
periodic()
