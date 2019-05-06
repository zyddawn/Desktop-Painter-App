from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Ellipse(QLabel):
	def __init__(self, rCenter=QPoint(100, 100), rx=50, ry=50, algorithm='Midpoint-circle'):
		super(Ellipse, self).__init__()
		self.rCenter = rCenter
		self.rx = rx
		self.ry = ry
		self.algorithm = algorithm
		self.qpainter = None

	def draw(self, qp):
		# TODO
		self.qpainter = qp
		
		qp.drawEllipse(self.rCenter, self.rx, self.ry)

	# def getPath(self):
	# 	self.path = QPainterPath()
	# 	self.path.moveTo(100, 100)
	# 	self.path.lineTo(200, 200)
	# 	return self.path