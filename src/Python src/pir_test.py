# PIR motion sensor has two operation mode:
# normal mode can detect up to about 10 m,
# reduced sensivity mode has range reduced by half.
# It only produces digital output, and restoring
# delay is about 5 sec. To start up, it needs about
# 1 min for the sensor to initialize and adapt the environment.
# It works well for motion detection.

import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(11,GPIO.IN)

While True:
	sensor = GPIO.input(11)
	if sensor == 0:
		print "Not here"
	else:
		print "Someone is here"
	time.sleep(0.5)

