#!/bin/sh

sleep 60

echo "Subject: Car Statistics" > /home/pi/pyobd-pi/emailme.txt

# Add the results from the drive
echo >> /home/pi/pyobd-pi/emailme.txt
echo /home/pi/pyobd-pi/log/ >> /home/pi/pyobd-pi/emailme.txt

sendmail za08gilm@siena.edu < /home/pi/pyobd-pi/emailme.txt