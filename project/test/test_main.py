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

##Funktioner## #Måste testa#
def height():
    motorA.run_angle(200, 90, then = Stop.HOLD, wait = True)
    #while touch_sensor.pressed() == False:
    robot.drive(-75,0)
    if touch_sensor.pressed() == True:
        ev3.speaker.say('Picking up an item')
        motorA.run_angle(500, 180, then = Stop.HOLD, wait = True)
        robot.drive(50,0)
    
        
    elif touch_sensor.pressed() == False:
        print("Det upplockade obejektet har tappats")


##Följa linje## #Klar#
def line_follow():
    # Initialize the color sensor.
    color_sensor = ColorSensor(Port.S3)

    BLACK = 9
    WHITE = 85
    threshold = (BLACK + WHITE) / 2

    DRIVE_SPEED = 50
    PROPORTIONAL_GAIN = 1.2

    while True:
        deviation = color_sensor.reflection() - threshold #threshold

        turn_rate = PROPORTIONAL_GAIN * deviation

        robot.drive(DRIVE_SPEED, turn_rate)

        wait(10)

        if touch_sensor.pressed() == True:
            pickup(touch_sensor, color_sensor)

#Undvika Kollision
        while obstacle_sensor.distance() < 170:
            wait(10)
            print(obstacle_sensor.distance())
            robot.straight(-150)
            robot.turn(120)
            print('Undviker kollision')
        

    
#Left the specified area## 
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


#Plocka upp## #Klar#
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


##Undvika kollision## #Funkar och är implementerad i line_follow#
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

##Follow line 2##
def lft():
    while robot.distance() >= 1000:
        correction = (30 - color_sensor.reflection())*2
        robot.drive(100, correction)
    robot.stop()
    left_motor.brake()
    right_motor.brake()



### FÄRGER ###
#blå 27<r<39, 31<g<36, 81<b<97
#cirkelgrön 21<r<51, 17<g<40, 18<b<84
#lila 23<r<34, 15<g<25, 66<b<88
#grön 13<r<49, 38<g<61, 31<b<92

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

#----------idéer efter andra presentationen---------------
#den ska pipa olika antal gånger när den utför en uppgift, så att det 'talar' om det för oss

##rena funktioner
def just_pickup(touch_sensor):
    #motorA.run_angle(-500, 90, then = Stop.HOLD, wait = True)
    #while touch_sensor.pressed() == False:
    while True:
        robot.drive(-75,0)
        if touch_sensor.pressed() == True:
            ev3.speaker.say('Picked up an item')
            motorA.run_angle(500, 180, then = Stop.HOLD, wait = True)
            robot.drive(50,0)
            break
    
        if touch_sensor.pressed() == False:
            print("Det upplockade obejektet har tappats")
            

def collision():
    obstacle_sensor = UltrasonicSensor(Port.S4)

    while True:
        robot.drive(-100, 0)
        print(obstacle_sensor.distance())
        while obstacle_sensor.distance() < 200:
            ev3.speaker.say('Avoided an collision')
            wait(10)
            print(obstacle_sensor.distance())
            robot.straight(50)
            robot.turn(120)



        
            
