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
		self.getFirstQuarter()
		self.getSecondQuarter()
		self.getThirdQuarter()
		self.getFourthQuarter()
		for p in self.point_arr:
			self.qpainter.drawPoint(p)
		return True

	def getFirstQuarter(self):
		x, y = 0, self.b
		d1 = self.b**2 + self.a**2*(-self.b+0.25)
		self.point_arr.append(QPoint(x, y))
		while self.b**2*(x+1) < self.a**2*(y-0.5):
			if d1 < 0:
				d1 += self.b**2*(2*x+3)
				x += 1
			else:
				d1 += self.b**2*(2*x+3) + self.a**2*(-2*y+2)
				x, y = x+1, y-1
			self.point_arr.append(QPoint(x, y))
		d2 = (self.b*(x+0.5))**2 + (self.a*(y-1))**2 - (self.a*self.b)**2
		while y > 0:
			if d2 < 0:
				d2 += self.b**2*(2*x+2) + self.a**2*(-2*y+3)
				x, y = x+1, y-1
			else:
				d2 += self.a**2*(-2*y+3)
				y -= 1
			self.point_arr.append(QPoint(x, y))

	def getSecondQuarter(self):
		pass

	def getThirdQuarter(self):
		pass

	def getFourthQuarter(self):
		pass





