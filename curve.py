from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Curve(QLabel):
	def __init__(self):
		super(Curve, self).__init__()

	def draw(self, qp):
		# TODO
		pass

	def getPath(self):
		self.path = QPainterPath()
		self.path.moveTo(100, 100)
		self.path.lineTo(200, 200)
		return self.path

