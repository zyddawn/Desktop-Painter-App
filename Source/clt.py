from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
from canvas import *
from puw import *
from time import *
import transform as tm
from args import *

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.canvasOffset = 10
		self.curColor = QColor(0, 0, 0)
		self.path = None
		self.initUI()
		self.canvasPos = self.centralWidget().pos()

	def initUI(self):
		self.setUpWindow(0.8)
		self.setUpCanvas()
		
	def setUpWindow(self, ratio=0.8):
		ScreenRect = QDesktopWidget().availableGeometry()
		[x, y, w, h] = [ScreenRect.x(), ScreenRect.y(), ScreenRect.width(), ScreenRect.height()]
		self.setGeometry((1-ratio)*w/2+x, (1-ratio)*h/2+y, ratio*w, ratio*h)
		self.setWindowTitle("Yudong Zhang's Mini CG System")

	def selectColor(self, R, G, B):
		if 0<=R<=255 and 0<=G<=255 and 0<=B<=255:
			self.curColor = QColor(R, G, B)

	def setUpCanvas(self):
		self.canvas = Canvas()
		self.setCentralWidget(self.canvas)
		self.newCanvas(0, 0)	# default size

	def resetCanvasSize(self, w, h):
		if not (isinstance(w,int) and isinstance(h,int) and 100<=w<=1000 and 100<=h<=1000):
			w = self.canvas.width()-self.canvasOffset*2
			h = self.canvas.height()-self.canvasOffset*2
		self.canvas.setCanvasSize(w, h)

	def newCanvas(self, w, h):
		self.resetCanvasSize(w, h)
		self.canvas.newCanvas()

	def setPath(self, path):
		self.path = path

	def loadFile(self, loadPath, savePath=None):
		self.canvas.openCanvas(loadPath)
		if savePath:
			self.path = savePath
		else:
			self.path = loadPath

	def saveFile(self, name):
		if not self.canvas.hasCanvas:
			print("Should create a canvas before saving the canvas.")
		else:
			self.canvas.saveCanvas(os.path.join(self.path, "{0}.{1}".format(name, "bmp")))

	def newLine(self, Id, p1, p2, algorithm):
		if self.canvas.hasCanvas:
			self.canvas.newLine(self.curColor, pId=Id, p1=p1, p2=p2, algorithm=algorithm)
		else:
			print("Should create a canvas before drawing a line.")
	
	def newPolygon(self, Id, points, algorithm):
		if self.canvas.hasCanvas:
			self.canvas.newPolygon(self.curColor, pId=Id, points=points, algorithm=algorithm)
		else:
			print("Should create a canvas before drawing a polygon.")

	def newEllipse(self, Id, center, rx, ry, algorithm):
		if self.canvas.hasCanvas:
			self.canvas.newEllipse(self.curColor, pId=Id, rCenter=center, rx=rx, ry=ry, algorithm=algorithm)
		else:
			print("Should create a canvas before drawing a ellipse.")

	def newCurve(self, Id, points, algorithm):
		if self.canvas.hasCanvas:
			self.canvas.newCurve(self.curColor, pId=Id, points=points, algorithm=algorithm)
		else:
			print("Should create a canvas before drawing a curve.")

	def translate(self, Id, dx, dy):
		if self.canvas.hasCanvas:
			if self.canvas.nextId > 0:
				if Id not in self.canvas.allElements.keys():
					print("Element with id={} doesn't exist!".format(Id))
				else:
					elem = self.canvas.getElement(Id)
					tm.translate(elem, dx, dy)
					print("Translate (id={}, type={}) with (dx={}, dy={})"\
							.format(elem.id, elem.type, dx, dy))
			else:
				print("Should create a element first before translating it.")
		else:
			print("Should create a canvas before translating elements.")

	def rotate(self, Id, x, y, angle):
		if self.canvas.hasCanvas:
			if self.canvas.nextId > 0:
				if Id not in self.canvas.allElements.keys():
					print("Element with id={} doesn't exist!".format(Id))
				else:
					elem = self.canvas.getElement(Id)
					# if elem.type == 'Ellipse':
					# 	print("Cannot rotate ellipse!")
					tm.rotate(elem, x, y, angle)
					print("Rotate (id={}, type={}) with (cx={}, cy={}, angle={})"\
							.format(elem.id, elem.type, x, y, angle))
			else:
				print("Should create a element first before rotating it.")
		else:
			print("Should create a canvas before rotating elements.")

	def scale(self, Id, x, y, portion):
		if self.canvas.hasCanvas:
			if self.canvas.nextId > 0:
				if Id not in self.canvas.allElements.keys():
					print("Element with id={} doesn't exist!".format(Id))
				else:
					elem = self.canvas.getElement(Id)
					tm.scale(elem, x, y, portion)
					print("Scale (id={}, type={}) with (cx={}, cy={}, scale={})"\
							.format(elem.id, elem.type, x, y, portion))
			else:
				print("Should create a element first before scaling it.")
		else:
			print("Should create a canvas before scaling elements.")

	def lineClip(self, Id, x1, y1, x2, y2, algorithm):
		if self.canvas.hasCanvas:
			if Id not in self.canvas.allElements.keys():
				print("Element id doesn't exist!")
			elif self.canvas.allElements[Id].type is not "Line":
				print("The selected element is not a line!")
			else:
				if x1<x2 and y1<y2:
					lineElem = self.canvas.getElement(Id)
					tm.lineClip(lineElem, QPoint(x1, y1), 
							QPoint(x2, y2), algorithm)
					print("Clip line (id={}, type={}) within (lowerleft={}, upperright={}, algorithm={})"\
							.format(lineElem.id, lineElem.type, (x1, y1), \
									(x2, y2), algorithm))
				else:
					print("The given window is invalid!")
		else:
			print("Should create a canvas before clipping lines.")



def execCommands(op_arr, path=None):
	app = QApplication(sys.argv)
	ex = MainWindow()
	if path:
		ex.setPath(path)
	else:
		ex.setPath('../Demos/')
	for op in op_arr:
		if op.action == 'resetCanvas':
			w, h = int(op.params[0]), int(op.params[1])
			ex.newCanvas(w, h)
			# print("    resetCanvas {0} {1}".format(w, h))
		elif op.action == 'saveCanvas':
			name = op.params[0]
			ex.saveFile(name)
			# print("    saveCanvas {0}".format(name))
		elif op.action == 'setColor':
			R, G, B = int(op.params[0]), int(op.params[1]), int(op.params[2])
			ex.selectColor(R, G, B)
			# print("    setColor {0} {1} {2}".format(R, G, B))
		elif op.action == 'drawLine':
			Id, x1, y1, x2, y2, algorithm = int(op.params[0]), int(op.params[1]), int(op.params[2]), \
											int(op.params[3]), int(op.params[4]), op.params[5]
			ex.newLine(Id, QPoint(x1, y1), QPoint(x2, y2), algorithm)
			# print("    drawLine {0} {1}--{2} {3}".format(Id, (x1, y1), (x2, y2), algorithm))
		elif op.action == 'drawPolygon':
			Id, n, algorithm = int(op.params[0]), int(op.params[1]), op.params[2]
			points = []
			for i in range(n):
				points.append((int(op.params[3+2*i]), int(op.params[4+2*i])))
			ex.newPolygon(Id, points, algorithm)
			# print("    drawPolygon {0} {1} {2} {3}".format(Id, n, algorithm, points))
		elif op.action == 'drawEllipse':
			Id, x, y, rx, ry = int(op.params[0]), int(op.params[1]), int(op.params[2]), int(op.params[3]), int(op.params[4])
			algorithm = 'Midpoint-circle'
			ex.newEllipse(Id, QPoint(x, y), rx, ry, algorithm)
			# print("    drawEllipse {0} {1} {2} {3} {4}".format(Id, (x, y), rx, ry, algorithm))
		elif op.action == 'drawCurve':
			Id, n, algorithm = int(op.params[0]), int(op.params[1]), op.params[2]
			points = []
			for i in range(n):
				points.append((int(op.params[3+2*i]), int(op.params[4+2*i])))
			ex.newCurve(Id, points, algorithm)
			print("    drawCurve not implemented yet.")
			# print("    drawCurve {0} {1} {2} {3}".format(Id, n, algorithm, points))
		elif op.action == 'translate':
			Id, dx, dy = int(op.params[0]), int(op.params[1]), int(op.params[2])
			ex.translate(Id, dx, dy)
		elif op.action == 'rotate':
			Id, x, y, r = int(op.params[0]), int(op.params[1]), int(op.params[2]), int(op.params[3])
			ex.rotate(Id, x, y, r)
		elif op.action == 'scale':
			Id, x, y, s = int(op.params[0]), int(op.params[1]), int(op.params[2]), float(op.params[3])
			ex.scale(Id, x, y, s)
		elif op.action == 'clip':
			Id, x1, y1, x2, y2, algorithm = int(op.params[0]), int(op.params[1]), int(op.params[2]), \
											int(op.params[3]), int(op.params[4]), op.params[5]
			ex.lineClip(Id, x1, y1, x2, y2, algorithm)
		elif op.action == 'loadCanvas':
			path = op.params[0]
			if len(op.params)>1:
				savePath = op.params[1]
				ex.loadFile(path, savePath)
			else:
				ex.loadFile(path)
		else:
			print("Unknown command '{}'!".format(op.action))


if __name__=='__main__':
	args = parseArgs(sys.argv)
	if args.script:
		op_arr = parseScript(args.script)
		if args.path:
			execCommands(op_arr, args.path)
		else:
			execCommands(op_arr)
		# for i, x in enumerate(op_arr):
		# 	print("{0}: {1} {2}".format(i, x.action, x.params))

