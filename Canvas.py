# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from time import *
import os

class Element(QLabel):
	ElementsTypes = ['Line', 'Polygon', 'Ellipse', 'Curve']
	def __init__(self, canvas, pType, pColor, pId=None, *args, **kwargs):
		if pType not in self.ElementsTypes:
			raise RuntimeError('Invalid element type: {}'.format(pType))
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
		print("Create new {0} with id={1}".format(self.type, self.id))
	
	def createObj(self):
		if not self.hasObject:
			if self.type=='Line':
				self.object = Line(self.kwargs['p1'], self.kwargs['p2'])
			elif self.type=='Polygon':
				self.object = Polygon()
			elif self.type=='Ellipse':
				self.object = Ellipse(self.kwargs['rCenter'], self.kwargs['rx'], self.kwargs['ry'])
			elif self.type=='Curve':
				self.object = Curve()
			else:
				raise RuntimeError('Invalid element type: {}'.format(self.type))
			self.hasObject = True
			self.paintEvent()
		else:
			raise RuntimeError("Already created an object within current element.")

	def paintEvent(self):
		qp = QPainter(self.canvas.pixmap())
		qp.setPen(QPen(self.color))
		qp.setBrush(QBrush(self.color))
		self.object.draw(qp)
		self.canvas.update()


# Line
class Line(QLabel):
	### BUG!!!!
	def __init__(self, p1=QPoint(100, 100), p2=QPoint(200, 200)):
		super(Line, self).__init__()
		self.p1 = p1
		self.p2 = p2
		# self.

	def draw(self, qp, algorithm='DDA'):
		# TODO: self-implement algorithms
		qp.drawPath(self.getPath())

	def getPath(self):
		self.path = QPainterPath()
		self.path.moveTo(self.p1)
		self.path.lineTo(self.p2)
		return self.path


# Polygon
class Polygon(QLabel):
	def __init__(self):
		super(Polygon, self).__init__()
		

	def draw(self, qp):
		# TODO
		# qp.drawEllipse(rCenter, rx, ry)
		pass

	def getPath(self):
		self.path = QPainterPath()
		self.path.moveTo(100, 100)
		self.path.lineTo(200, 200)
		return self.path

# Ellipse
class Ellipse(QLabel):
	def __init__(self, rCenter=QPoint(100, 100), rx=50, ry=50):
		super(Ellipse, self).__init__()
		self.rCenter = rCenter
		self.rx = rx
		self.ry = ry

	def draw(self, qp):
		# TODO
		qp.drawEllipse(self.rCenter, self.rx, self.ry)

	# def getPath(self):
	# 	self.path = QPainterPath()
	# 	self.path.moveTo(100, 100)
	# 	self.path.lineTo(200, 200)
	# 	return self.path

# Curve
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


class Canvas(QLabel):
	def __init__(self, savePath='.', fileName=''):
		super(Canvas, self).__init__()
		self.nextId = 0
		self.curId = -1
		self.allElements = {}
		# self.curColor = '#FFFFFF'
		self.w = 0
		self.h = 0
		self.hasCanvas = False
		self.savePath = savePath
		self.fileName = fileName

	def setCanvasSize(self, w, h):
		self.w = w
		self.h = h
		
	def newCanvas(self):
		self.background_color = QColor(Qt.white)
		emptyCanvas = QPixmap(self.w, self.h)
		self.setPixmap(emptyCanvas)
		self.pixmap().fill(self.background_color)
		self.setAlignment(Qt.AlignCenter)
		self.hasCanvas = True

	def createElement(self, pType, pColor, pId=None, *args, **kwargs):
		# check Id
		self.checkIdValid(pId)
		self.allElements[self.curId] = Element(self, pType=pType, pColor=pColor, pId=self.curId, *args, **kwargs)

	@property
	def curElement(self):
		return self.allElements[self.curId]

	def checkIdValid(self, pId):
		if isinstance(pId, int):
			if pId==self.nextId:
				self.curId, self.nextId = self.nextId, self.nextId+1
			elif pId<self.nextId:
				if pId<0 or pId not in self.allElements.keys():
					raise RuntimeError('Invalid primitive id: {}'.format(pId))
				else:
					self.curId = pId
			elif pId>self.nextId:
				self.curId, self.nextId = pId, pId+1
		else:
			self.curId, self.nextId = self.nextId, self.nextId+1

	def saveCanvas(self, path=None):
		if path is None:
			fileName = self.fileName if self.fileName else strftime("%Y%m%d-%H%M%S.bmp")
			path = os.path.join(self.savePath, fileName)
		self.pixmap().save(path, 'PBM')
		print("Image successfully saved at directory: {0}".format(os.path.realpath(path)))


	def openCanvas(self, path, name):
		self.savePath = path
		self.fileName = name
		# TODO
		pass

	@property
	def getWidth(self):
		return self.w

	@property
	def getHeight(self):
		return self.h
	
	def newLine(self, pColor, pId=None, *args, **kwargs):
		self.createElement(pType='Line', pColor=pColor, pId=pId, *args, **kwargs)

	def newPolygon(self, pColor, pId=None):
		self.createElement(pType='Polygon', pColor=pColor, pId=pId)

	def newEllipse(self, pColor, pId=None, *args, **kwargs):
		self.createElement(pType='Ellipse', pColor=pColor, pId=pId, *args, **kwargs)

	def newCurve(self, pColor, pId=None):
		self.createElement(pType='Curve', pColor=pColor, pId=pId)












