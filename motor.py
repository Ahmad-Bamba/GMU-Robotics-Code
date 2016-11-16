import Adafruit_PCA9685
import constants as c

# 1.0 ms = 205 ticks, 1.5 ms = 307 ticks, and 2.0 ms 410 ticks

class Motor:
    "To make Adafruit_PCA9685 move"
    ms2 = 410
    m15 = 307
    ms1 = 205
    def __init__(self, channel):
        self.ch = channel
        c.PWM.set_pwm(ch, 0, ms15)

    def set(self, value):
        "Converts value from -1 to 1 to a pulse. 'Correct' widths: 1ms = full reverse, 1.5ms = stop, 2.0ms = full forward"
        "Source: https://www.vexforum.com/index.php/15882-pwming-a-victor-sp/p1#p144589"
        # How controlling PWM works is that you have to set the pulse width
        # by saying what part of the signal should be off and what should be on
        # But it only works in ticks, so math must be done so that the pulses are the
        # correct widths to understand what to do

        if value > 1:
            value = 1
        elif value < -1:
            value = - 1

        percent = double((value + 1)/2) # 1 would go to 100%, -1 would go to 0%, 0 would go to 50%
        write = ms1 + ((ms2 - ms1) * percent)
        c.PWM.set_pwm(ch, 0, int(write))

        
