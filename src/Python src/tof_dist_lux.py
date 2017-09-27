# VL6180X integrates both distance sensor
# and light intensity sensor.

# 1-100k lux with 16 bits output precision.
# 0-100 mm in turns of range. (really short)
# the default I2C address for it is 0x29

import time
from rpisensors import VL6180X 

sensor = VL6180X(1)

while True:
	dist = sensor.read_distance() 
	lux = sensor.read_lux()
	print "%d mm| %d lux" % (dist,lux)
	time.sleep(1)
