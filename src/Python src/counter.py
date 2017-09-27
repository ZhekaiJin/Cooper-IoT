import numpy as np
import imutils
import cv2
import Person
from picamera import PiCamera
from picamera.array import PiRGBArray
from time import sleep



ToRight = 0
ToLeft = 0
pid = 0
persons = []


#video = cv2.VideoCapture('test.mp4')
bg = cv2.createBackgroundSubtractorMOG2()

#_,frame = video.read()
#height,width = frame.shape[:2]
width = 640
height = 480
left = 250
right = width - 250
LB = 150
RB = width - 150

# setup camera
camera = PiCamera()
camera.rotation = 180
camera.resolution = (width,height)
rawCap = PiRGBArray(camera,size=(width,height))
sleep(2)


#gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#gray = cv2.GaussianBlur(gray,(21,21),0)
#prev_frame = gray

for f in camera.capture_continuous(rawCap,format='bgr',use_video_port=True):
	'''
	returned,frame = video.read()
	if not returned:
		break
	'''

	"""
	# convert it to grayscale, and blur it
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray,(21,21),0)
 
	frameDif = cv2.absdiff(prev_frame, gray)
	threshold = cv2.threshold(frameDif,50,255,cv2.THRESH_BINARY)[1]
	threshold = cv2.dilate(threshold,None, iterations=2)
	_,cnts,_ = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
	"""
	
	frame = f.array
	#frame = imutils.resize(frame,width=width)
	fgmask = frame
	fgmask = cv2.blur(frame,(21,21))
	fgmask = bg.apply(fgmask)
	oldMask = fgmask.copy()
	_,cnts,_ = cv2.findContours(fgmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

	for c in cnts:
		x,y,w,h = cv2.boundingRect(c)
		if w > 100 and h > 200:
			cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
			cv2.circle(frame,(x+w/2,y+h/2),1,(0,0,255),5)
			#print x
				
			new = True
			for i in persons:
				if abs(x-i.getX()) <= w and abs(y-i.getY()) <= h:
					new = False
					i.update(x,y)
					break
			if x < LB or x  > RB:
				new = False
			if new == True:
				if x < right:
					p = Person.MyPerson(pid,x,y,True)
				else:
					p = Person.MyPerson(pid,x,y,False)
				persons.append(p)
				pid += 1
				print 'one person added'
			
	for person in persons:
		if person.isDone():
			continue
		if person.isFromLeft() and person.getX() > right:
			print 'to right'
			ToRight += 1
			person.finished()
		elif not person.isFromLeft() and person.getX() < left:
			print 'to left'
			ToLeft += 1
			person.finished()
	
	for person in persons:
		if not person.isDone():
			continue
		if person.getX() > RB or person.getX() < LB:
			persons.remove(person)
			
	if len(persons) > 10:
		persons = []
 	

	cv2.line(frame,(right,0),(right,height),(0,0,255),2)
	cv2.line(frame,(left,0),(left,height),(0,0,255),2) 
	cv2.line(frame,(RB,0),(RB,height),(255,0,0),2)
	cv2.line(frame,(LB,0),(LB,height),(255,0,0),2) 

	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
	cv2.putText(frame, "ToRight: {}".format(str(ToRight)),(10,50),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
	cv2.putText(frame, "ToLeft: {}".format(str(ToLeft)),(10,70),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,255),2)
	
	cv2.imshow('frame',frame)
	#cv2.imshow('fgbg',fgmask)
	rawCap.truncate(0)
	

#video.release()
cv2.destroyAllWindows()
print len(persons)
