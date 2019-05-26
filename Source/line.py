from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Line(QLabel):
	def __init__(self, p1=QPoint(100, 100), p2=QPoint(200, 200), algorithm='Bresenham'):
		super(Line, self).__init__()
		self.p1 = p1
		self.p2 = p2
		self.algorithm = algorithm
		# self.qpainter = None
		self.point_arr = []
		self.old_point_arr = []
		self._params = {"point1": (self.p1.x(), self.p1.y()), 
						"point2": (self.p2.x(), self.p2.y()), "algorithm": self.algorithm}

	@property
	def params(self):
		return self._params

	def setP1(self, newP):
		self.p1 = newP

	def setP2(self, newP):
		self.p2 = newP

	def updatePoints(self, newArr):
		self.old_point_arr = self.point_arr[:]
		self.point_arr = newArr
		if len(self.point_arr) > 0:
			self.p1, self.p2 = self.point_arr[0], self.point_arr[-1]

	def getPoints(self):
		Res = True
		if self.algorithm == 'DDA':
			self.DDA()
		elif self.algorithm == 'Midpoint':
			self.Midpoint()
		elif self.algorithm == 'Bresenham':
			self.Bresenham()
		else:
			print("Can't draw! Unknown algorithm.")
			Res = False
		return Res

	def DDA(self):
		if len(self.point_arr)>0:
			return ;
		x1, y1 = self.p1.x(), self.p1.y()
		x2, y2 = self.p2.x(), self.p2.y()
		dx, dy = x2-x1, y2-y1
		e = abs(dx) if abs(dx)>abs(dy) else abs(dy)
		if e == 0:
			return ;
		dx = dx*1.0 / e
		dy = dy*1.0 / e
		x, y = x1, y1
		# calc points
		for i in range(e):
			self.point_arr.append(QPoint(int(x+0.5), int(y+0.5)))
			x += dx
			y += dy

	def Midpoint(self):
		if len(self.point_arr)>0:
			return ;
		x1, y1 = self.p1.x(), self.p1.y()
		x2, y2 = self.p2.x(), self.p2.y()
		if x1==x2:	# when k is inf
			k = 100.0*(y2-y1)
		else: 
			k = 1.0*(y2-y1)/(x2-x1)
		# calc points
		if -1 < k < 1:
			(y1, y2) = (y1, y2) if x2>x1 else (y2, y1)
			(x1, x2) = (x1, x2) if x2>x1 else (x2, x1)
			self.point_arr.append(QPoint(x1, y1))
			a, b = y1-y2, x2-x1
			x, y = x1, y1
			if k > 0: # b>0, a<0
				# print("Case 1")
				d = 2*a + b
				delta1, delta2 = 2*a, 2*(a+b)
				while x < x2:
					if d < 0:
						x, y, d = x+1, y+1, d+delta2
					else:
						x, d = x+1, d+delta1
					self.point_arr.append(QPoint(x, y))
			else: # b>0, a>0
				# print("Case 2")
				d = 2*a - b
				delta1, delta2 = 2*(a-b), 2*a
				while x < x2:
					if d < 0:
						x, d = x+1, d+delta2
					else:
						x, y, d = x+1, y-1, d+delta1
					self.point_arr.append(QPoint(x, y))
		else:
			(x1, x2) = (x1, x2) if y2>y1 else (x2, x1)
			(y1, y2) = (y1, y2) if y2>y1 else (y2, y1)
			self.point_arr.append(QPoint(x1, y1))
			a, b = y1-y2, x2-x1
			x, y = x1, y1
			if k > 0: # a<0, b>0
				# print("Case 3")
				d = 2*b + a
				delta1, delta2 = 2*(a+b), 2*b
				while y < y2:
					if d < 0:
						y, d = y+1, d+delta2
					else:
						x, y, d = x+1, y+1, d+delta1
					self.point_arr.append(QPoint(x, y))
			else: # k in (-inf, -1], a<0, b<0
				# print("Case 4")
				d = 2*b - a
				delta1, delta2 = 2*b, 2*(b-a)
				while y < y2:
					if d < 0:
						x, y, d = x-1, y+1, d+delta2
					else:
						y, d = y+1, d+delta1
					self.point_arr.append(QPoint(x, y))
		
	def Bresenham(self):
		if len(self.point_arr)>0:
			return ;
		x1, y1 = self.p1.x(), self.p1.y()
		x2, y2 = self.p2.x(), self.p2.y()
		if x1==x2:	# when k is inf
			k = 100.0*(y2-y1)
		else: 
			k = 1.0*(y2-y1)/(x2-x1)
		# calc points
		if -1 < k < 1:
			(y1, y2) = (y1, y2) if x2>x1 else (y2, y1)
			(x1, x2) = (x1, x2) if x2>x1 else (x2, x1)
			x, y = x1, y1
			dx, dy = x2-x1, y2-y1
			if k > 0: # dx>0, dy>0
				# print("Case 1")
				p = 2*dy - dx
				while x <= x2:
					self.point_arr.append(QPoint(x, y))
					if p < 0: # dx>0, d1<d2
						x, p = x+1, p+2*dy
					else:
						x, y, p = x+1, y+1, p+2*(dy-dx)
			else: # dx>0, dy<0
				# print("Case 2")
				p = -2*dy - dx
				while x <= x2:
					self.point_arr.append(QPoint(x, y))
					if p < 0: # dx>0, d1<d2
						x, p = x+1, p-2*dy
					else:
						x, y, p = x+1, y-1, p-2*(dx+dy)
		else:
			(x1, x2) = (x1, x2) if y2>y1 else (x2, x1)
			(y1, y2) = (y1, y2) if y2>y1 else (y2, y1)
			x, y = x1, y1
			dx, dy = x2-x1, y2-y1
			if k > 0: # dx>0, dy>0
				# print("Case 3")
				p = 2*dx - dy
				while y <= y2:
					self.point_arr.append(QPoint(x, y))
					if p < 0:
						y, p = y+1, p+2*dx
					else:
						x, y, p = x+1, y+1, p+2*(dx-dy)
			else: # dx<0, dy>0
				# print("Case 4")
				p = -2*dx - dy
				while y <= y2:
					self.point_arr.append(QPoint(x, y))
					if p < 0:
						y, p = y+1, p-2*dx
					else:
						x, y, p = x-1, y+1, p-2*(dx+dy)
		















