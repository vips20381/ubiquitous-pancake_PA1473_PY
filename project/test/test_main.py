#!/usr/bin/env pybricks-micropython
#Importer
import sys

from pybricks.hubs import EV3Brick
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor, TouchSensor


#KOD

##Grunder av roboten##
ev3 = EV3Brick()
motorA = Motor(Port.A) #kolla port
motorB = Motor(Port.B) #kolla port
motorC = Motor(Port.C) #kolla port
left_motor = motorA
right_motor = motorB
lift_motor = motorC

touch = TouchSensor(Port.S1)
color_sensor = ColorSensor(Port.E)
robot = DriveBase(left_motor, right_motor, wheel_diameter= 47, axle_track= 128) # Initialize the drive base.

##Basic movement##
def basicmove():
    # Go forward and backwards for one meter.
    robot.straight(1000)
    robot.straight(-1000)
    # Turn clockwise by 360 degrees and back again.
    robot.turn(360)
    robot.turn(-360)


##Följa linje##
def line_follow():
    # Initialize the color sensor.
    line_sensor = ColorSensor(Port.S3)

    # Calculate the light threshold. Choose values based on your measurements.
    BLACK = 9
    WHITE = 85
    threshold = (BLACK + WHITE) / 2

    # Set the drive speed at 100 millimeters per second.
    DRIVE_SPEED = 100

    # Set the gain of the proportional line controller. This means that for every
    # percentage point of light deviating from the threshold, we set the turn
    # rate of the drivebase to 1.2 degrees per second.

    # For example, if the light value deviates from the threshold by 10, the robot
    # steers at 10*1.2 = 12 degrees per second.
    PROPORTIONAL_GAIN = 1.2

    # Start following the line endlessly.
    while True:
        # Calculate the deviation from the threshold.
        deviation = line_sensor.reflection() - threshold

        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation

        # Set the drive base speed and turn rate.
        robot.drive(DRIVE_SPEED, turn_rate)

        # You can wait for a short time or do other things in this loop.
        wait(10)


##Plocka upp##

def pickup(touch_sensor):

    if touch_sensor.pressed() == True:
        motorC.run(10)
        robot.straight(-20)
        motorC.run(-30) #dubbelkolla hur långt ner den ska sänka armarna
        robot.turn(180)
        print("Roboten har tagit upp något")
        
    else:
        print('Roboten har inte tagit upp något')
    #kolla så att 'pressed' är True under diverse funktioner

#  kolla färg
# om rätt färg:
# 	kör fram tills .pressed() == True
# 	lyft lite
# 	backa
# 	sänk armar
# 	vänd runt
# 	kör tillbaka
# om inte rätt färg:
#	kör vidare
    return


##plocka upp från en höjd##



##Undvika kollision##

def collision():
    # Initialize the Ultrasonic Sensor. It is used to detect
    # obstacles as the robot drives around.
    obstacle_sensor = UltrasonicSensor(Port.S4)


    # The following loop makes the robot drive forward until it detects an
    # obstacle. Then it backs up and turns around. It keeps on doing this
    # until you stop the program.
    while True:
        # Begin driving forward at 200 millimeters per second.
        robot.drive(200, 0)

        # Wait until an obstacle is detected. This is done by repeatedly
        # doing nothing (waiting for 10 milliseconds) while the measured
        # distance is still greater than 300 mm.
        while obstacle_sensor.distance() > 300:
            wait(10)

        # Drive backward for 300 millimeters.
        robot.straight(-300)

        # Turn around by 120 degrees
        robot.turn(120)


#RÖR EJ
def main():
    return 0

if __name__ == '__main__':
    sys.exit(main())

