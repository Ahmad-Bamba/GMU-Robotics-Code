import Adafruit_PCA9685
import constants as c

# 1.0 ms = 205 ticks, 1.5 ms = 307 ticks, and 2.0 ms 410 ticks

ms2 = 410
ms15 = 330
ms1 = 250

class Victor:
	"To make VictorSP connected through Adafruit_PCA9685 move"
	def __init__(self, channel):
		self.channel = channel
		c.PWM.set_pwm(self.channel, 0, ms15)

	def set(self, value, inverse = False, debug = False):
		"Converts value from -1 to 1 to a pulse. 'Correct' widths: 1ms = full reverse, 1.5ms = stop, 2.0ms = full forward"
		"Source: https://www.vexforum.com/index.php/15882-pwming-a-victor-sp/p1#p144589"

	x = value

	if x > 1:
		x = 1
	elif x < -1:
		x = -1

	percent = float(abs(x) / 1) # Math
	write = 80 * percent

	if debug:
		print "Debugging: " + str(int(write))

	if not inverse:
		if x > 0:
			c.PWM.set_pwm(self.channel, 0, int(ms15 + write))
		else:
			c.PWM.set_pwm(self.channel, 0, int(ms15 - write))
	else:
		if x > 0:
			c.PWM.set_pwm(self.channel, 0, int(ms15 - write))
		else:
			c.PWM.set_pwm(self.channel, 0, int(ms15 + write))

class Stepper:
	"""Code to make stepper motor controller work with PCA9685"""
	def __init__(self, channel):
		self.channel = channel
