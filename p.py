import RPi.GPIO as GPIO
import pygame
import sys

f = 333.333 #frequency #3ms period
mone_pin = 23
mtwo_pin = 24
mthree_pin = 17
mfour_pin = 12
rest_dc = 47.8
speed = -10 # 0 - 17 max
#right_stick_y = 1
safe_sleep = 0.2
#stick_port = 0
# pwm_min = 250
# pwm_max = 410
stick = None
mone = None
mtwo = None
mthree = None
mfour = None

def init():
    global mone
    global mtwo
    global mthree
    global mfour
    global stick

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(mone_pin, GPIO.OUT)
    GPIO.setup(mtwo_pin, GPIO.OUT)
    GPIO.setup(mthree_pin, GPIO.OUT)
    GPIO.setup(mfour_pin, GPIO.OUT)    
    mone = GPIO.PWM(mone_pin,f)
    mone.start(rest_dc)
    mtwo = GPIO.PWM(mtwo_pin,f)
    mtwo.start(rest_dc)
    mthree = GPIO.PWM(mthree_pin,f)
    mthree.start(rest_dc)
    mfour = GPIO.PWM(mfour_pin,f)
    mfour.start(rest_dc)
    pygame.joystick.init()
    pygame.display.init()
    if not (pygame.joystick.get_count() > 0):
        print "No joysticks detected, quiting..."
        sys.exit()
#    print pygame.joystick.get_count()
    stick = pygame.joystick.Joystick(0)
    stick.init()

def periodic():
    enabled = True
    global stick

    i = 0

    while enabled:
        try:
            i += 1
            pygame.event.pump()
            for event in pygame.event.get():
                if pygame.event.event_name(event.type) == "JoyButtonUp":
                    # Do button stuff here
                    if int(event.button) == 0:  # A button
                        print "A"
                    elif int(event.button) == 1:  # B Button
                        print "B"
                    elif int(event.button) == 2:  # X Button?
			mone.start(rest_dc)
			mtwo.start(rest_dc)
			mthree.start(rest_dc)
			mfour.start(rest_dc)                        
			print "X"
                    elif int(event.button) == 3:  # Y Button?
                        print "Y"
		if pygame.event.event_name(event.type) == "JoyAxisMotion": 
                    # Do Axis stuff
		    # display duty cycle values (DC: 33=full reverse, 50=stop, 66=full forward)
		    # max speed 17 ticks, limit set at 5 so the robot doesn't move too fast (adjust later)
		    # sys.stdout.write("%04.2f \r" % (rest_dc + (speed * pygame.joystick.Joystick(0).get_axis(0))))
		    # sys.stdout.flush()

                    strafe_one = 0
                    strafe_two = 0
                    rotate = 0


		    if abs(stick.get_axis(1)) < safe_sleep:
			strafe_one = 0
		    else:
                        strafe_one = stick.get_axis(1)
                    
                    if abs(stick.get_axis(0)) < safe_sleep:
                         strafe_two = 0
                    else:
                         strafe_two = stick.get_axis(0)
              
                    if abs(stick.get_axis(3)) < safe_sleep:
                        rotate = 0
                    else:
                        rotate = stick.get_axis(3)
                    
                    m1_p = min(1, max(-1, strafe_one + rotate))
                    m3_p = min(1, max(-1, -strafe_one + rotate))
                    m2_p = min(1, max(-1, strafe_two + rotate))
                    m4_p = min(1, max(-1, -strafe_two + rotate))

                    
                    # print "m1_p:" + str(m1_p)
                    # print "m2_p:" + str(m2_p)
                    # print "m3_p:" + str(m3_p)
                    # print "m4_p:" + str(m4_p)

                    mone.ChangeDutyCycle(rest_dc + (speed * m1_p))
                    mtwo.ChangeDutyCycle(rest_dc + (speed * m2_p))
                    mthree.ChangeDutyCycle(rest_dc + (speed * m3_p))
                    mfour.ChangeDutyCycle(rest_dc + (speed * m4_p))

        except KeyboardInterrupt:
            print "Keyboard Interrupt!"
            mone.ChangeDutyCycle(rest_dc)
            mtwo.ChangeDutyCycle(rest_dc)
            mthree.ChangeDutyCycle(rest_dc)
            mfour.ChangeDutyCycle(rest_dc)

            mone.stop()
            mtwo.stop()
	    mthree.stop()
	    mfour.stop()
            GPIO.cleanup()
            print "Closing presentation mode"
            enabled = False

if __name__ == '__main__':
    init()
    periodic()
