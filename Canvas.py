# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from element import *
import os


class Canvas(QLabel):
	def __init__(self, path=None):
		super(Canvas, self).__init__()
		self.nextId = 0
		self.curId = -1
		self.allElements = {}
		# self.curColor = '#FFFFFF'
		self.w = 0
		self.h = 0
		self.hasCanvas = False

	def setCanvasSize(self, w, h):
		self.w = w
		self.h = h
		
	def clearElements(self):
		self.nextId = 0
		self.curId = -1
		self.allElements = {}

	def newCanvas(self):
		self.clearElements()
		self.background_color = QColor(Qt.white)
		emptyCanvas = QPixmap(self.w, self.h)
		self.setPixmap(emptyCanvas)
		self.pixmap().fill(self.background_color)
		self.setAlignment(Qt.AlignCenter)
		self.hasCanvas = True
		self.update()

	def createElement(self, pType, pColor, pId=None, *args, **kwargs):
		# check Id
		self.checkIdValid(pId)
		newElem = Element(self, pType=pType, pColor=pColor, pId=self.curId, *args, **kwargs)
		if newElem.hasObject:
			self.allElements[self.curId] = newElem
		# print(newElem)

	def getElement(self, Id):
		if Id in self.allElements.keys():
			return self.allElements[Id]
		else:
			print("No element with id={}!".format(Id))
			return None

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

	def saveCanvas(self, path):
		if path:
			self.pixmap().save(path, 'BMP')
			print("Image successfully saved at directory: {0}".format(os.path.realpath(path)))
		else:
			print("Failed saving! Path not correct: {0}".format(os.path.realpath(path)))

	def openCanvas(self, path):
		if path:
			pixmap = QPixmap()
			pixmap.load(path)
			self.setPixmap(pixmap)
			self.setAlignment(Qt.AlignCenter)
			self.hasCanvas = True
			self.update()
			# self.setScaledContents(True)
			print("Image successfully loaded from directory: {0}".format(os.path.realpath(path)))
		else:
			print("Failed loading! Path not correct: {0}".format(os.path.realpath(path)))

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












