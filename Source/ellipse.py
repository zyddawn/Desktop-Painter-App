from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ellipse(QLabel):
	def __init__(self, rCenter=QPoint(100, 100), rx=50, ry=50, algorithm='Midpoint-circle'):
		super(Ellipse, self).__init__()
		self.rCenter = rCenter
		self.a = rx
		self.b = ry
		self.algorithm = algorithm
		# self.qpainter = None
		self.point_arr = []
		self.old_point_arr = []
		self._params = {"rCenter": (self.rCenter.x(), self.rCenter.y()), \
						"rx": self.a, "ry": self.b, "algorithm": self.algorithm}

	@property
	def params(self):
		return self._params

	def updatePoints(self, newArr):
		self.old_point_arr = self.point_arr[:]
		self.point_arr = newArr

	def getPoints(self):
		self.MidPointCircle()
		
	def MidPointCircle(self):
		if len(self.point_arr)>0:
			return ;
		self.getFirstQuadrant()
		self.getSecondQuadrant()
		self.getThirdQuadrant()
		self.getFourthQuadrant()

	def getFirstQuadrant(self):
		x0, y0 = self.rCenter.x(), self.rCenter.y()
		x, y = x0, y0+self.b
		d1 = self.b**2 + self.a**2*(0.25-self.b)
		self.point_arr.append(QPoint(x, y))
		while abs(self.b**2*(x-x0+1)) < abs(self.a**2*(y-y0-0.5)):
			if d1 < 0:
				d1 += self.b**2*(2*x-2*x0+3)
				x += 1
			else:
				d1 += self.b**2*(2*x-2*x0+3) + self.a**2*(-2*y+2*y0+2)
				x, y = x+1, y-1
			self.point_arr.append(QPoint(x, y))
		d2 = (self.b*(x-x0+0.5))**2 + (self.a*(y-y0-1))**2 - (self.a*self.b)**2
		while y > y0:
			if d2 < 0:
				d2 += self.b**2*(2*x-2*x0+2) + self.a**2*(-2*y+2*y0+3)
				x, y = x+1, y-1
			else:
				d2 += self.a**2*(-2*y+2*y0+3)
				y -= 1
			self.point_arr.append(QPoint(x, y))

	def getSecondQuadrant(self):
		x0, y0 = self.rCenter.x(), self.rCenter.y()
		x, y = x0, y0+self.b
		d1 = self.b**2 + self.a**2*(0.25-self.b)
		self.point_arr.append(QPoint(x, y))
		while abs(self.b**2*(x-x0-1)) < abs(self.a**2*(y-y0-0.5)):
			if d1 < 0:
				d1 += self.b**2*(-2*x+2*x0+3)
				x -= 1
			else:
				d1 += self.b**2*(-2*x+2*x0+3) + self.a**2*(-2*y+2*y0+2)
				x, y = x-1, y-1
			self.point_arr.append(QPoint(x, y))
		d2 = (self.b*(x-x0-0.5))**2 + (self.a*(y-y0-1))**2 - (self.a*self.b)**2
		while y > y0:
			if d2 < 0:
				d2 += self.b**2*(-2*x+2*x0+2) + self.a**2*(-2*y+2*y0+3)
				x, y = x-1, y-1
			else:
				d2 += self.a**2*(-2*y+2*y0+3)
				y -= 1
			self.point_arr.append(QPoint(x, y))

	def getThirdQuadrant(self):
		x0, y0 = self.rCenter.x(), self.rCenter.y()
		x, y = x0, y0-self.b
		d1 = self.b**2 + self.a**2*(0.25-self.b)
		self.point_arr.append(QPoint(x, y))
		while abs(self.b**2*(x-x0-1)) < abs(self.a**2*(y-y0+0.5)):
			if d1 < 0:
				d1 += self.b**2*(-2*x+2*x0+3)
				x -= 1
			else:
				d1 += self.b**2*(-2*x+2*x0+3) + self.a**2*(2*y-2*y0+2)
				x, y = x-1, y+1
			self.point_arr.append(QPoint(x, y))
		d2 = (self.b*(x-x0-0.5))**2 + (self.a*(y-y0+1))**2 - (self.a*self.b)**2
		while y <= y0:
			if d2 < 0:
				d2 += self.b**2*(-2*x+2*x0+2) + self.a**2*(2*y-2*y0+3)
				x, y = x-1, y+1
			else:
				d2 += self.a**2*(2*y-2*y0+3)
				y += 1
			self.point_arr.append(QPoint(x, y))

	def getFourthQuadrant(self):
		x0, y0 = self.rCenter.x(), self.rCenter.y()
		x, y = x0, y0-self.b
		d1 = self.b**2 + self.a**2*(0.25-self.b)
		self.point_arr.append(QPoint(x, y))
		while abs(self.b**2*(x-x0+1)) < abs(self.a**2*(y-y0+0.5)):
			if d1 < 0:
				d1 += self.b**2*(2*x-2*x0+3)
				x += 1
			else:
				d1 += self.b**2*(2*x-2*x0+3) + self.a**2*(2*y-2*y0+2)
				x, y = x+1, y+1
			self.point_arr.append(QPoint(x, y))
		d2 = (self.b*(x-x0+0.5))**2 + (self.a*(y-y0+1))**2 - (self.a*self.b)**2
		while y <= y0:
			if d2 < 0:
				d2 += self.b**2*(2*x-2*x0+2) + self.a**2*(2*y-2*y0+3)
				x, y = x+1, y+1
			else:
				d2 += self.a**2*(2*y-2*y0+3)
				y += 1
			self.point_arr.append(QPoint(x, y))





