# Program that takes ttyAMA0 input from the Neo 6m GPS module and
# converts it into Latitude and Longitude coordinates, used by
# Google Maps for offline use.
#
# Code used sourced from https://sparklers-the-makers.github.io/blog/robotics/realtime-gps-tracker-with-raspberry-pi/
#

import serial
import time
import string
import pynmea2

while True:
    port="/dev/ttyAMA0"
    ser=serial.Serial(port, baudrate=9600, timeout=0.5)
    dataout = pynmea2.NMEAStreamReader()
    newdata=ser.readline()

    if newdata[0:6] == "$GPRMC":
        newmsg=pynmea2.parse(newdata)
        lat=newmsg.latitude
        lng=newmsg.longitude
        gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
        print(gps)
