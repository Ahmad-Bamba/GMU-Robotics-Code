import pygame
import sys
import atexit as quit
from time import sleep

# Notes
# This code goes through the most useful joystick function we will probably use
# It pretty much works the same way as WPILib does (buttons return true/false and
# axes return -1 to 1)
# jstest-gtk will reveal all button-mapping woes. I think they are the same as our
# robot as well.

stick = None
f = None
enabled = True
eventstack = [-1] * 20

def closefile():
    f.close()
    print str(eventstack)

def start():
    global stick

    print "Starting joystick test...."
    pygame.joystick.init()
    pygame.display.init()
    print "There are " + str(pygame.joystick.get_count()) + " joystick(s) connected."
    joynames = "They are: "
    for x in xrange(pygame.joystick.get_count()):
        joynames += pygame.joystick.Joystick(x).get_name() + ", "
    print joynames

    stick = pygame.joystick.Joystick(0)
    stick.init()

def loop():
    global stick
    global f
    global eventstack

    quit.register(closefile)

    print "Recording data..."
    while(enabled):
        f = open("output.txt", 'w')
        pygame.event.pump()

        for x in xrange(stick.get_numbuttons() - 1):
            f.write("Button " + str(x) + ": " + str(stick.get_button(x)) + "\n")
            # FILO
            if stick.get_button(x):
                eventstack.insert(0, x)
                eventstack.pop()
            else:
                eventstack.insert(0, -1)
                eventstack.pop()

        for y in xrange(stick.get_numaxes() - 1):
            f.write("Axis " + str(y) + ": " + str(stick.get_axis(y)) + "\n")

start()
loop()
