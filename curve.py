from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Curve(QLabel):
	def __init__(self, points=[], algorithm='Bezier'):
		super(Curve, self).__init__()
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
		if self.algorithm == 'Bezier':
			self.Bezier()
		elif self.algorithm == 'B-spline':
			self.BSpline()
		else:
			print("Can't draw! Unknown algorithm.")
			Res = False
		return Res

	def Bezier(self):
		print("Bezier not implemented yet.")
		pass


	def BSpline(self):
		print("BSpline not implemented yet.")
		pass








