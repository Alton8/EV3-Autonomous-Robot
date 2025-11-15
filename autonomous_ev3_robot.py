#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (
    Motor, TouchSensor, ColorSensor, InfraredSensor,
    UltrasonicSensor, GyroSensor
)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.

# ---------------------------
# Hardware setup
# ---------------------------
ev3 = EV3Brick()
ev3.speaker.beep()

left_motor = Motor(Port.C)
right_motor = Motor(Port.B)

robot = DriveBase(
    left_motor,
    right_motor,
    wheel_diameter=55.5,
    axle_track=104
)

color_sensor = ColorSensor(Port.S3)

# ---------------------------
# Color thresholds (RGB)
# ---------------------------
blue = dict(r=(8, 13),  g=(17, 23), b=(50, 84))
red  = dict(r=(21, 31), g=(6, 9),   b=(14, 18))
black = dict(r=(5, 7),  g=(5, 7),   b=(9, 13))
yellow = dict(r=(34, 42), g=(37, 44), b=(43, 52))

def in_range(v, lo_hi):
    """Return True if v is within [lo, hi]."""
    lo, hi = lo_hi
    return lo <= v <= hi

def is_color(r, g, b, rng):
    """Match (r,g,b) against a dict of channel ranges."""
    return (
        in_range(r, rng['r']) and
        in_range(g, rng['g']) and
        in_range(b, rng['b'])
    )

# ---------------------------
# Main loop
# ---------------------------
while True:
    # Read RGB from the color sensor
    r, g, b = color_sensor.rgb()
    print((r, g, b))

    if is_color(r, g, b, blue):
        # Respond to blue tape: curve right a bit
        robot.drive(75, 50)
        wait(500)

    elif is_color(r, g, b, red):
        # Respond to red tape: stop, go straight, then turn left
        robot.drive(0, 0)
        wait(1000)
        robot.drive(75, 0)
        wait(1500)
        robot.drive(75, -75)
        wait(1500)

    elif is_color(r, g, b, black):
        # Respond to black tape: curve left
        robot.drive(75, -50)

    elif is_color(r, g, b, yellow):
        # Respond to yellow tape: stop, go straight, then turn right
        robot.drive(0, 0)
        wait(1000)
        robot.drive(75, 0)
        wait(1500)
        robot.drive(75, 75)
        wait(1500)

    else:
        # Floor/unknown: go straight
        robot.drive(75, 0)

    # Important: brief pause so the sensor can keep up
    wait(10)
