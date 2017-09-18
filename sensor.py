from time import sleep
import RPi.GPIO as GPIO
from rpisensors import VL6180X
import Adafruit_DHT as dht
import time


# open log file to write
file = open('data_log.csv', 'w')
file.write('Time, Light, Temperature, Humidity\n')

# setup pin mode
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

# setup light sensor
light_sensor = VL6180X(1)


sleep(3)

# initialize state
prev_state = 0 
start = time.time()
prev = start


while True:

	# other sensors' code
	# read sensor data every 3 minutes
	current = time.time()
	if current - prev > 180:
		now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
		light = light_sensor.read_lux() 
		humidity,temp = dht.read_retry(dht.DHT22,4) 
		temp = temp*9/5.0 + 32
		light = str('{0:0.1f}'.format(light))
		humidity = str('{0:0.1f}'.format(humidity))
		temp = str('{0:0.1f}'.format(temp))
		file.write(now + ',' + light + ',' + temp + ',' + humidity + '\n')
		file.flush()
		prev = current

##############################################################

	# run time is 48 hours or 2 days
	# 172800
	if current - start > 172800:
		# clean up
		file.close()
		# send 0 to signal end of connection
		connection.write(struct.pack('<L',0))
		connection.close()
		client_socket.close()		
		break


	sleep(1)

