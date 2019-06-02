from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from line import *
from random import *
import numpy as np

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
		if len(self.rawPoints)!=4:
			self.geometryBezier(npoints=npoints)
		else:
			self.splitBezier(self.rawPoints)
		
	def geometryBezier(self, npoints=500):
		t, delta = 0.0, 1.0/npoints
		for i in range(npoints+1):
			p = deCasteljau(self.rawPoints, t)
			self.point_arr.append(QPoint(p[0], p[1]))
			t += delta

	def splitBezier(self, points):
		# n=4
		# print("\t splitBezier")
		R, Q = points[:], points[:]
		epsilon = 0.01
		if (maxDist(points)<epsilon):
			newLine = Line(QPoint(points[0][0], points[0][1]), QPoint(points[3][0], points[3][1]), algorithm='Bresenham')
			newLine.getPoints()
			self.point_arr.extend(newLine.point_arr)
		else:
			for i in range(3):
				Q[i] = R[0]
				for j in range(3-i):
					x = (R[j][0]+R[j+1][0]) / 2
					y = (R[j][1]+R[j+1][1]) / 2
					R[j] = (x, y)
			Q[3] = R[0]
			self.splitBezier(Q)
			self.splitBezier(R)


	def BSpline(self):
		print("BSpline not implemented yet.")
		pass


def deCasteljau(points, t):
	R, Q = points[:], points[:]
	for m in range(1, len(points))[::-1]:
		Q = [(R[i][0]+t*(R[i+1][0]-R[i][0]), R[i][1]+t*(R[i+1][1]-R[i][1])) for i in range(0, m)]
		R[:m] = Q[:m]
	return R[0]

def maxDist(points):
	s1 = ((points[0][0]-points[1][0])*(points[0][1]-points[1][1]) + \
			(points[1][0]-points[3][0])*(points[1][1]-points[3][1]) + \
			(points[3][0]-points[0][0])*(points[3][1]-points[0][1]))
	s2 = ((points[0][0]-points[2][0])*(points[0][1]-points[2][1]) + \
			(points[2][0]-points[3][0])*(points[2][1]-points[3][1]) + \
			(points[3][0]-points[0][0])*(points[3][1]-points[0][1]))
	dist = np.sqrt((points[0][0]-points[3][0])**2 + (points[0][1]-points[3][1])**2)
	h1, h2 = np.abs(s1/dist), np.abs(s2/dist)
	return max(h1, h2)


