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
motorA = Motor(Port.A) #kolla port #Lyft
motorB = Motor(Port.B) #kolla port # Vänster
motorC = Motor(Port.C) #kolla port # Höger 
left_motor = motorB
right_motor = motorC
lift_motor = motorA

obstacle_sensor = UltrasonicSensor(Port.S4)
touch_sensor = TouchSensor(Port.S1)
color_sensor = ColorSensor(Port.S3)
robot = DriveBase(left_motor, right_motor, wheel_diameter= 47, axle_track= 128) # Initialize the drive base.

##Funktioner##
def height(touch):
    
    height = 30 #höjd på saken man ska lyfta från

    while touch.pressed == False:
        motorA.run(height)
        a = robot.straight()
        touch = True
    while touch == True:
        motorA.run(10)
        robot.straight(-(a+30))
        robot.turn(360) #vänd ett halvt varv


##Följa linje##
def line_follow():
    # Initialize the color sensor.
    color_sensor = ColorSensor(Port.S3)

    BLACK = 9
    WHITE = 85
    threshold = (BLACK + WHITE) / 2

    DRIVE_SPEED = 100
    PROPORTIONAL_GAIN = 1.2

    while True:
        deviation = color_sensor.reflection() - threshold #threshold

        turn_rate = PROPORTIONAL_GAIN * deviation

        robot.drive(DRIVE_SPEED, turn_rate)

        wait(10)

##Undvika Kollision
        while obstacle_sensor.distance() < 400:
            wait(10)
            print(obstacle_sensor.distance())
            robot.straight(-150)
            robot.turn(120)

        
    
##Left the specified area##
def area(color_sensor, color):
    color = color_sensor
    if color == 'Green':
        loc = 'Warehouse'
    elif color == 'Red':
        loc = 'Red Warehouse'
    elif color == 'Blue':
        loc = 'Blue Warehouse'
    elif color == 'Yellow':
        loc = 'Ring'
    print("Robot is currently at",loc)
##Plocka upp##

def pickup(touch_sensor, color_sensor):
    if touch_sensor.pressed() == True:
        motorA.run(200)
        robot.straight(-50)
        motorA.run(-200)
        robot.turn(360)
        print("Roboten har tagit upp något")
        
    else:
        print('Roboten har inte tagit upp något')
    #kolla så att 'pressed' är True under diverse funktioner


##Follow line 2##
def lft():
    while robot.distance() >= 1000:
        correction = (30 - color_sensor.reflection())*2
        robot.drive(100, correction)
    robot.stop()
    left_motor.brake()
    right_motor.brake()


##Undvika kollision##
def collision():
    obstacle_sensor = UltrasonicSensor(Port.S4)

    while True:
        robot.drive(-50, 0)
        print(obstacle_sensor.distance())
        while obstacle_sensor.distance() > 170:
            wait(10)
            print(obstacle_sensor.distance())
            robot.straight(-150)
            robot.turn(120)

### FÄRGER ###
##Testa färg##
def see_color():
    color = color_sensor.color()
    color_list = []
    color_list.append(color)
    print(color_list)
    return color_list[-1]

##hitta reflection
def rgb_color():
    färg_reflection = color_sensor.reflection()
    print(färg_reflection)


#RÖR EJ
def main():
    return 0

if __name__ == '__main__':
    sys.exit(main())

