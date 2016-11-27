import Adafruit_PCA9685
import constants as c

# 1.0 ms = 205 ticks, 1.5 ms = 307 ticks, and 2.0 ms 410 ticks

ms2 = 410
ms15 = 330
ms1 = 250

class Motor:
    "To make VictorSP connected through Adafruit_PCA9685 move"
    def __init__(self, channel, debug = false):
        self.ch = channel
        c.PWM.set_pwm(self.ch, 0, ms15)

    def set(self, value):
        "Converts value from -1 to 1 to a pulse. 'Correct' widths: 1ms = full reverse, 1.5ms = stop, 2.0ms = full forward"
        "Source: https://www.vexforum.com/index.php/15882-pwming-a-victor-sp/p1#p144589"
        # How controlling PWM works is that you have to set the pulse width
        # by saying what part of the signal should be off and what should be on
        # But it only works in ticks, so math must be done so that the pulses are the
        # correct widths to understand what to do
	
	# Tbh I'm going to guesstimate these until it works

	x = value

        if x > 1:
		x = 1
	elif x < -1:
		x = -1

	percent = float(abs(x) / 1) # Math
	write = 80 * percent
	
	if debug:
		print "Debugging: " + str(int(write))

	if x == 1:
        	c.PWM.set_pwm(self.ch, 0, int(ms15 + write))
	else:
		c.PWM.set_pwm(self.ch, 0, int(ms15 - write))
