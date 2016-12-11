import Adafruit_PCA9685

# VictorSP IDs (PWM)
MOTOR_TOP    = 0 # Wheel closest to top of battery
MOTOR_RIGHT  = 2
MOTOR_BOTTOM = 1
MOTOR_LEFT   = 3

# IR Sensors (PWM)
IR_TOP          = 4
IR_TOP_RIGHT    = 5
IR_RIGHT        = 6
IR_BOTTOM_RIGHT = 7
IR_BOTTOM       = 8
IR_BOTTOM_LEFT  = 9
IR_LEFT         = 10
IR_TOP_LEFT     = 11

# Lead Screw (PWM?)
MOTOR_SCREW  = 12

# Servo IDs
SERVO_CLAMP      = 13
SERVO_ROTATE_ARM = 14

# Servo
SERVO_MIN = 150
SERVO_MAX = 600

# Joystick
JOYSTICK = 0

# Misc
FULL_POWER = 1.0 # Can be changed if mechanical wants to "fix it in code"
HALF_POWER = FULL_POWER / 2
LOW_POWER  = FULL_POWER / 5
# QUARTER_POWER = FULL_POWER /4
PWM = Adafruit_PCA9685.PCA9685() # One pwm handler for the entire robot (pls no break)
THRESHOLD = 0.2

# Kill switch Exception
class KillSwitch(Exception):
    pass
