from picamera import PiCamera
from time import sleep
import RPi.GPIO as GPIO
import io
import socket
import struct
import time



# start a socket
client_socket = socket.socket()
client_socket.connect(("199.98.20.87",8001))
connection = client_socket.makefile('wb')
stream = io.BytesIO()


# setup pin mode
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

# setup camera
camera = PiCamera()
camera.rotation = 180
camera.resolution = (640,480)
# camera.framerate = 15
# camera.brightness = 70
# camera.annotate_text_size = 50

# capture background image

sleep(3)
camera.capture(stream,'jpeg')
connection.write(struct.pack('<L',stream.tell()))
connection.flush()
stream.seek(0)
connection.write(stream.read())
stream.seek(0)
stream.truncate()


# initialize state
prev_state = 0 
start = time.time()
prev = start


while True:
	# PIR sensor code
	current_state = GPIO.input(11)
	if current_state == 1 and prev_state == 0:
		#print "%d %s"% (current_state, prev_state)
		#camera.start_preview()
		sleep(0.2)
		camera.capture(stream, 'jpeg')
		#camera.stop_preview()
		#print "captured"
		
		# tell the length of image
		connection.write(struct.pack('<L',stream.tell()))
		connection.flush()
		stream.seek(0)

		# send the image data to the socket
		connection.write(stream.read())

		# time out
		#if time.time() - current > 30:
		#	stream.seek(0)
		#	stream.truncate()
		#	continue
		# reset the stream	
		stream.seek(0)
		stream.truncate()

	#else:
		#print "NO MOTION DETECTED"

	#print "%d %d" %(prev_state, current_state)
	prev_state = current_state

##############################################################

	# run time is 48 hours or 2 days
	if current - start > 172800:
		# clean up
		file.close()
		# send 0 to signal end of connection
		connection.write(struct.pack('<L',0))
		connection.close()
		client_socket.close()		
		break


	sleep(1)

