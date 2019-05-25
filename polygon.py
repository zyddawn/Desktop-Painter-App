from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from line import *

class Polygon(QLabel):
	def __init__(self, points=[], algorithm='Bresenham'):
		super(Polygon, self).__init__()
		self.rawPoints = points
		self.algorithm = algorithm
		# self.qpainter = None
		self.point_arr = []
		self.old_point_arr = []
		self._params = {"points": self.rawPoints, "algorithm": self.algorithm}
		
	@property
	def params(self):
		return self._params

	def updatePoints(self, newArr):
		self.old_point_arr = self.point_arr[:]
		self.point_arr = newArr

	def getPoints(self):
		Res = True
		if self.algorithm == 'DDA':
			self.DDA()
		elif self.algorithm == 'Bresenham':
			self.Bresenham()
		else:
			print("Can't draw! Unknown algorithm.")
			Res = False
		return Res

	def DDA(self):
		n = len(self.rawPoints)
		for i in range(n):
			p1, p2 = self.rawPoints[i], self.rawPoints[(i+1)%n]
			newLine = Line(QPoint(p1[0], p1[1]), QPoint(p2[0], p2[1]), algorithm='DDA')
			Res = newLine.getPoints()
			if Res:
				self.point_arr.extend(newLine.point_arr)

	def Bresenham(self):
		n = len(self.rawPoints)
		for i in range(n):
			p1, p2 = self.rawPoints[i], self.rawPoints[(i+1)%n]
			newLine = Line(QPoint(p1[0], p1[1]), QPoint(p2[0], p2[1]), algorithm='Bresenham')
			Res = newLine.getPoints()
			if Res:
				self.point_arr.extend(newLine.point_arr)



