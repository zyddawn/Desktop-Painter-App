from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from random import *

class Curve(QLabel):
	def __init__(self, points=[], algorithm='Bezier'):
		super(Curve, self).__init__()
		self.rawPoints = points
		# self.rawPoints = [(114,488), (260,92), (199,300), (542,124)]
		# , (100, 100), (180, 250)]
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
		if self.algorithm == 'Bezier':
			xs, ys = [p[0] for p in self.rawPoints], [p[1] for p in self.rawPoints]
			npoints = 4*(max(xs)-min(xs)+max(ys)-min(ys))	# default value
			self.Bezier(npoints=npoints)
		else:
			 # self.algorithm == 'B-spline':
			self.BSpline()

	def Bezier(self, npoints=500):
		self.geometryBezier(npoints=npoints)
		# if randint(0,1)==0:
		# 	self.geometryBezier(npoints=npoints)
		# else:
		# 	self.splitBezier()
		
	def geometryBezier(self, npoints=500):
		t, delta = 0.0, 1.0/npoints
		for i in range(npoints+1):
			p = deCasteljau(self.rawPoints, t)
			self.point_arr.append(QPoint(p[0], p[1]))
			t += delta

	def splitBezier(self):
		pass






	def BSpline(self):
		print("BSpline not implemented yet.")
		pass


def deCasteljau(points, t):
	R = points[:]
	Q = points[:]
	for m in range(1, len(points))[::-1]:
		Q = [(R[i][0]+t*(R[i+1][0]-R[i][0]), R[i][1]+t*(R[i+1][1]-R[i][1])) for i in range(0, m)]
		R[:m] = Q[:m]
	return R[0]

def maxDist(points):
	s1 = (p[0].x)


