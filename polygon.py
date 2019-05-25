from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *

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
		print("DDA not implemented yet.")
		pass

	def Bresenham(self):
		print("Bresenham not implemented yet.")
		pass














