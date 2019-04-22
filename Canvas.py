# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Primitive(object):
	primitiveTypes = ['Line', 'Polygon', 'Ellipse', 'Curve']
	def __init__(self, pType='Line', pColor='#000000', pId=None):
		# TODO: judge if the type, color … are valid
		if pType not in primitiveTypes:
			raise RuntimeError('Invalid primitive type: {}'.format(pType))
		self.type = pType
		self.color = pColor
		self.id = pId
		self.path = None

	def draw(self):
		self.path = QPainterPath()
		self.path.moveTo(30, 30)


# Line
class Line(Primitive):
	def __init__(self, pColor='#000000', pId=None):
		super(Line, self).__init__(pType='Line', pColor=pColor, pId=self.curId)

	def draw(self):
		super(Line, self).draw()
		pass

# Polygon
class Polygon(Primitive):
	def __init__(self, pColor='#000000', pId=None):
		super(Polygon, self).__init__(pType='Polygon', pColor=pColor, pId=self.curId)

	def draw(self):
		super(Polygon, self).draw()
		pass

# Ellipse
class Ellipse(Primitive):
	def __init__(self, pColor='#000000', pId=None):
		super(Ellipse, self).__init__(pType='Ellipse', pColor=pColor, pId=self.curId)

	def draw(self):
		super(Ellipse, self).draw()
		pass

# Curve
class Curve(Primitive):
	def __init__(self, pColor='#000000', pId=None):
		super(Curve, self).__init__(pType='Curve', pColor=pColor, pId=self.curId)

	def draw(self):
		super(Curve, self).draw()
		pass


class Canvas(QLabel):
	def __init__(self):
		super(Canvas, self).__init__()
		self.curPrimitive = None	# 当前图元
		self.nextId = 0
		self.curId = -1
		self.allPrimitives = {}
		self.setUpCanvas()

	def setUpCanvas(self):
		pass

	def createPrimitive(self, pType, pColor, pId=None):
		# check Id
		self.checkIdValid(pId)
		self.curPrimitive = Primitive(pType=pType, pColor=pColor, pId=self.curId)
		self.allPrimitives[self.curId] = self.curPrimitive
		pass

	def checkIdValid(self, pId):
		if pId==self.nextId:
			self.curId, self.nextId = self.nextId, self.nextId+1
		elif pId<self.nextId:
			if pId<0 or pId not in self.allPrimitives.keys():
				raise RuntimeError('Invalid primitive id: {}'.format(pId))
			else:
				self.curId = pId
		elif pId>self.nextId:
			self.curId, self.nextId = pId, pId+1
		else:
			self.curId, self.nextId = self.nextId, self.nextId+1






