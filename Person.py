from random import randint
import time


class MyPerson:
	def __init__(self,i,x,y,fromLeft):
		self.i = i
		self.x = x
		self.y = y
		self.fromLeft = fromLeft
		self.done = False

	def getId(self):
		return self.i

	def getX(self):
		return self.x
	
	def getY(self):
		return self.y

	def isFromLeft(self):
		return self.fromLeft

	def isDone(self):
		return self.done

	def update(self,x,y):
		self.x = x
		self.y = y
		
	def finished(self):
		self.done = True
