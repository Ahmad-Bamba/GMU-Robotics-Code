# 3rd Party
import sys
import time
from networktables import NetworkTable
import logging
# logging.basicconfig(level=logging.DEBUG)

# Robot Dashboard
dash = NetworkTable.getTable("Robot Dashboard")

enabled = True

def updateDash(updates):
	"""2D array where the first element of each row is the key and the second is a value"""
	for i in xrange(len(updates)):
		dash.putValue(updates[i][0], updates[i][1])
		print "Update helper: " + updates[i] + " " + dash.getValue(updates[i])

def init():
	pass

def periodic():
	try: # TODO: Test this crap!
		while True:
			dashupdate = [ ["Robot State", str(enabled)], ["Axis 0", str(random.uniform(-1, 1))], ["Axis 3", str(random.uniform(-1, 1))], ["Axis 2", str(random.uniform(-1, 1))], ["Axis 4", str(random.uniform(-1, 1))] ]
			print str(dashupdate)
			updateDash(dashupdate)
			if enabled:
				print "Enabled!"
			enabled = bool(dash.getValue("Robot State"))
	except KeyboardInterrupt:
		print "Exited by user request"
		enabled = False
		sys.exit()
	except Exception as e:
		print "".format(e.message)
		enabled = False
		sys.exit()

init()
periodic()
