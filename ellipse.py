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
		self.qpainter = None
		self.point_arr = []

	def draw(self, qp):
		self.qpainter = qp
		# vs qt standard
		self.qpainter.setPen(QPen(Qt.red))
		self.qpainter.drawEllipse(self.rCenter, self.a, self.b)
		self.qpainter.setPen(QPen(Qt.black))
		Res = True
		if self.algorithm == 'Midpoint-circle':
			Res = self.MidPointCircle()
		else:
			print("Can't draw! Unknown algorithm.")
			Res = False
		return Res

	def MidPointCircle(self):
		# TODO
		self.getFirstQuadrant()
		self.getSecondQuadrant()
		self.getThirdQuadrant()
		self.getFourthQuadrant()
		for p in self.point_arr:
			self.qpainter.drawPoint(p)
		return True

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





