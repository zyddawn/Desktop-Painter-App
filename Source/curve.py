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
		xs, ys = [p[0] for p in self.rawPoints], [p[1] for p in self.rawPoints]
		npoints = 4*(max(xs)-min(xs)+max(ys)-min(ys))	# default value	
		if self.algorithm == 'Bezier':
			self.Bezier(npoints=npoints)
		else:
			# self.algorithm == 'B-spline':
			# len(knot) = k + len(self.rawPoints)
			k = 3
			n = len(self.rawPoints)-1
			# if len(self.rawPoints) < k:
			# 	print("Should have no less than {} points for drawing B-Spline of order {}.".format(k, k))
			knot = []
			for j in range(n+k+1):
				if 0<=j<=k-1:
					knot.append(0)
				elif k<=j<=n:
					knot.append(j-k+1)
				elif n+1<=j<=n+k:
					knot.append(n-k+2)
			self.BSpline(knot, n, k=3, npoints=npoints)

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
		if maxDist(points) < epsilon:
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


	def BSpline(self, knot, n, k=3, npoints=500):
		delta = (knot[n+1] - knot[k-1]) / npoints
		ith, u = k-1, knot[k-1]
		for j in range(npoints+1):
			while ith<n and u>knot[ith+1]:
				ith += 1
			p = deBoor(self.rawPoints, ith, k, knot, u)
			self.point_arr.append(QPoint(p[0], p[1]))
			u += delta


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

def deBoor(points, ith, k, knot, u):
	denom = alpha = 0.0
	p = points[:k]
	epsilon = 0.005
	for j in range(k):
		p[j] = points[ith-k+1+j]
	for r in range(1, k):
		for m in range(r, k)[::-1]:
			j = m+ith-k+1
			denom = knot[j+k-r]-knot[j]
			if np.abs(denom) < epsilon:
				alpha = 0.0
			else:
				alpha = (u - knot[j]) / denom
			x = (1-alpha)*p[m-1][0] + alpha*p[m][0]
			y = (1-alpha)*p[m-1][1] + alpha*p[m][1]
			p[m] = (x, y)
	return p[k-1]








