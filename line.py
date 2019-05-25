from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Line(QLabel):
	def __init__(self, p1=QPoint(100, 100), p2=QPoint(200, 200), algorithm='DDA'):
		super(Line, self).__init__()
		self.p1 = p1
		self.p2 = p2
		self.algorithm = algorithm
		self.qpainter = None
		self.point_arr = []

	def draw(self, qp):
		self.qpainter = qp
		self.path = QPainterPath()
		self.path.moveTo(self.p1)
		# vs qt standard
		self.qpainter.setPen(QPen(Qt.red))
		self.qpainter.drawPath(self.getPath())
		self.qpainter.setPen(QPen(Qt.black))
		Res = True
		if self.algorithm == 'DDA':
			Res = self.DDA()
		elif self.algorithm == 'Midpoint':
			Res = self.Midpoint()
		elif self.algorithm == 'Bresenham':
			Res = self.Bresenham()
		else:
			print("Can't draw! Unknown algorithm.")
			Res = False
		return Res
		
	def getPath(self):
		self.path = QPainterPath()
		self.path.moveTo(self.p1)
		self.path.lineTo(self.p2)
		return self.path

	def DDA(self):
		x1, y1 = self.p1.x(), self.p1.y()
		x2, y2 = self.p2.x(), self.p2.y()
		self.point_arr = []
		dx, dy = x2-x1, y2-y1
		e = abs(dx) if abs(dx)>abs(dy) else abs(dy)
		dx = dx*1.0 / e
		dy = dy*1.0 / e
		x, y = x1, y1
		# calc points
		for i in range(e):
			self.point_arr.append(QPoint(int(x+0.5), int(y+0.5)))
			x += dx
			y += dy
		# draw
		for p in self.point_arr:
			self.qpainter.drawPoint(p)
		return True

	def Midpoint(self):
		x1, y1 = self.p1.x(), self.p1.y()
		x2, y2 = self.p2.x(), self.p2.y()
		self.point_arr = []
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
			point_arr.append(QPoint(x1, y1))
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
		# draw
		for p in self.point_arr:
			self.qpainter.drawPoint(p)
		return True

	def Bresenham(self):
		x1, y1 = self.p1.x(), self.p1.y()
		x2, y2 = self.p2.x(), self.p2.y()
		self.point_arr = []
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
				print("Case 3")
				p = 2*dx - dy
				while y <= y2:
					self.point_arr.append(QPoint(x, y))
					if p < 0:
						y, p = y+1, p+2*dx
					else:
						x, y, p = x+1, y+1, p+2*(dx-dy)
			else: # dx<0, dy>0
				print("Case 4")
				p = -2*dx - dy
				while y <= y2:
					self.point_arr.append(QPoint(x, y))
					if p < 0:
						y, p = y+1, p-2*dx
					else:
						x, y, p = x-1, y+1, p-2*(dx+dy)
		# draw 	
		for p in self.point_arr:
			self.qpainter.drawPoint(p)
		return True

















