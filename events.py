import pygame
import sys
import atexit as quit
from time import sleep

# Notes
# Events are perfect for buttons but are not really worth the hassle for getting axis values.
# Speaking of axis values, we definitely need to set a tolerance for that. Maybe 0.15 in both
# directions?

#vars
enabled = True
stick   = None

#Other methods
def init():
    # pygame inits
    pygame.display.init()
    pygame.joystick.init()
    # unavailable on Linux :(
    # pygame.camera.init()


#Main robot code
def start():
    global stick

    print "Code start!"
    init()
    # Maybe useless in the long run, but allows us to mess around with mouse events too.
    # pygame.display.set_mode([400, 300], pygame.OPENGL)

    if not (pygame.joystick.get_count() > 0):
        print "No joysticks detected, quiting..."
        sys.exit()

    joynames = "Joysticks Connected: "
    for x in xrange(pygame.joystick.get_count()):
        joynames += pygame.joystick.Joystick(x).get_name() + ", "
    print joynames
    stick = pygame.joystick.Joystick(0)
    stick.init()

    # print "Cameras?: " + str(pygame.camera.list_cameras())


def loop():
    global stick
    while enabled:
        pygame.event.pump()
        for event in pygame.event.get():
            # print event #if you want to loook at all the events...
            if pygame.event.event_name(event.type) == "JoyButtonUp":
                print "Button " + str(event.button) + " pressed."
            if pygame.event.event_name(event.type) == "Quit":
                sys.exit()

start()
loop()
