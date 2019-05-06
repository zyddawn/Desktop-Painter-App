from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from time import *
from line import *
from polygon import *
from ellipse import *
from curve import *

class Element(QLabel):
	ElementsTypes = ['Line', 'Polygon', 'Ellipse', 'Curve']
	def __init__(self, canvas, pType, pColor, pId=None, *args, **kwargs):
		if pType not in self.ElementsTypes:
			raise RuntimeError('Invalid element type: {}'.format(pType))
		super(Element, self).__init__()
		self.type = pType
		self.color = pColor
		self.id = pId
		self.args = args
		self.kwargs = kwargs
		self.path = None
		self.canvas = canvas
		self.hasObject = False
		self.object = None
		self.createObj()
		if self.hasObject:
			print("Create new {0} with id={1}".format(self.type, self.id))
			pass
	
	def createObj(self):
		if not self.hasObject:
			if self.type=='Line':
				self.object = Line(self.kwargs['p1'], self.kwargs['p2'], self.kwargs['algorithm'])
			elif self.type=='Polygon':
				self.object = Polygon()
			elif self.type=='Ellipse':
				self.object = Ellipse(self.kwargs['rCenter'], self.kwargs['rx'], self.kwargs['ry'], self.kwargs['algorithm'])
			elif self.type=='Curve':
				self.object = Curve()
			else:
				raise RuntimeError('Invalid element type: {}'.format(self.type))
			self.hasObject = self.paintEvent()
		else:
			raise RuntimeError("Already created an object within current element.")

	def paintEvent(self):
		qp = QPainter(self.canvas.pixmap())
		qp.setPen(QPen(self.color))
		qp.setBrush(QBrush(self.color))
		drawRes = self.object.draw(qp)
		self.canvas.update()
		qp.end()
		return drawRes



