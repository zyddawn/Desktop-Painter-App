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
			# print("Create new {0} with id={1}".format(self.type, self.id))
			print("New Element: {}".format(self))
			pass

	def __repr__(self):
		if self.hasObject:
			attributes = {"ID": self.id, "type": self.type, **self.object.params}
			return str(attributes)
		else:
			return None
	
	def createObj(self):
		if not self.hasObject:
			if self.type=='Line':
				self.object = Line(self.kwargs['p1'], self.kwargs['p2'], self.kwargs['algorithm'])
			elif self.type=='Polygon':
				self.object = Polygon(self.kwargs['points'], self.kwargs['algorithm'])
			elif self.type=='Ellipse':
				self.object = Ellipse(self.kwargs['rCenter'], self.kwargs['rx'], self.kwargs['ry'], self.kwargs['algorithm'])
			elif self.type=='Curve':
				self.object = Curve()
			else:
				raise RuntimeError('Invalid element type: {}'.format(self.type))
			self.paintEvent()
			self.hasObject = True
		else:
			raise RuntimeError("Already created an object within current element.")

	def updatePoints(self, newArr):
		self.object.updatePoints(newArr)
		self.paintEvent()
		self.hasObject = True
		self.canvas.update()

	def paintEvent(self):
		qp = QPainter(self.canvas.pixmap())
		# qp.setPen(QPen(self.color))
		# qp.setBrush(QBrush(self.color))
		self.getPoints()
		qp.setPen(QPen(Qt.white))	# erase old element
		for p in self.object.old_point_arr:
			qp.drawPoint(p)
		qp.setPen(QPen(self.color))
		for p in self.object.point_arr:
			qp.drawPoint(p)
		self.canvas.update()
		qp.end()

	def getPoints(self):
		self.object.getPoints()


