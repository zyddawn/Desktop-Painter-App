# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
from canvas import *
from puw import *
import random
from time import *

iconPath = './Icons'
imageTypes = ['.bmp', '.png', '.jpeg']


class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.initUI()
		self.canvasPos = self.centralWidget().pos()
		self.canvasOffset = 10
		self.curColor = QColor(0, 0, 0)
		self.path = None

	def initUI(self):
		self.setUpWindow(0.8)
		self.setUpMenu()
		self.setUpStatusBar()
		self.setUpCanvas()
		self.setUpToolBar()
		self.show()

	def setUpWindow(self, ratio=0.8):
		ScreenRect = QDesktopWidget().availableGeometry()
		[x, y, w, h] = [ScreenRect.x(), ScreenRect.y(), ScreenRect.width(), ScreenRect.height()]
		self.setGeometry((1-ratio)*w/2+x, (1-ratio)*h/2+y, ratio*w, ratio*h)
		self.setWindowTitle("Yudong Zhang's Mini CG System")

	def setUpMenu(self):
		menubar = self.menuBar()
		fileMenu = menubar.addMenu('File')
		editMenu = menubar.addMenu('Edit')
		viewMenu = menubar.addMenu('View')
		helpMenu = menubar.addMenu('Help')

		# Create new canvas
		newAct = QAction(QIcon(os.path.join(iconPath, 'icons8-add-new-64.png')), 'New/Refresh canvas', self)
		newAct.setShortcut('Ctrl+N')
		newAct.setStatusTip('Create new canvas / refresh canvas')
		newAct.triggered.connect(self.newCanvas)
		# Open file
		openAct = QAction(QIcon(os.path.join(iconPath, 'icons8-opened-folder-64.png')), 'Open...', self)
		openAct.setShortcut('Ctrl+O')
		openAct.setStatusTip('Open file...')
		openAct.triggered.connect(self.openFile)
		# Save file
		saveAct = QAction(QIcon(os.path.join(iconPath, 'icons8-save-64.png')), 'Save', self)
		saveAct.setShortcut('Ctrl+S')
		saveAct.setStatusTip('Save file')
		saveAct.triggered.connect(self.saveFile)
		# Save as file
		saveAsAct = QAction(QIcon(os.path.join(iconPath, 'icons8-save-as-64.png')), 'Save as...', self)
		saveAsAct.setShortcut('Shift+Ctrl+S')
		saveAsAct.setStatusTip('Save file as...')
		saveAsAct.triggered.connect(self.saveFileAs)
		### Add to fileMenu
		fileMenu.addAction(newAct)
		fileMenu.addSeparator()
		fileMenu.addAction(openAct)
		fileMenu.addAction(saveAct)
		fileMenu.addAction(saveAsAct)
		
		# Cut
		cutAct = QAction('Cut', self)
		cutAct.setShortcut('Ctrl+X')
		cutAct.setStatusTip('Cut')
		# cutAct.triggered.connect()
		# Copy
		copyAct = QAction('Copy', self)
		copyAct.setShortcut('Ctrl+C')
		copyAct.setStatusTip('Copy')
		# copyAct.triggered.connect()
		# Paste
		pasteAct = QAction('Paste', self)
		pasteAct.setShortcut('Ctrl+V')
		pasteAct.setStatusTip('Paste')
		# pasteAct.triggered.connect()
		### Add to editMenu
		editMenu.addAction(cutAct)
		editMenu.addAction(copyAct)
		editMenu.addAction(pasteAct)
		
		# Show toolbar
		toolBarAct = QAction('View tool bar', self, checkable=True)
		toolBarAct.setStatusTip('View tool bar')
		toolBarAct.setChecked(True)
		toolBarAct.triggered.connect(self.toggleToolBar)
		# Show statusbar
		statusBarAct = QAction('View status bar', self, checkable=True)
		statusBarAct.setStatusTip('View status bar')
		statusBarAct.setChecked(True)
		statusBarAct.triggered.connect(self.toggleStatusBar)

		##### set up tool bar
		self.toolbar = self.addToolBar("Operations")
		self.toolbar.addAction(newAct)
		self.toolbar.addAction(openAct)
		self.toolbar.addAction(saveAct)
		self.toolbar.addAction(saveAsAct)
		self.toolbar.addSeparator()
		

	def setUpToolBar(self):
		# choose color 
		colorAct = QAction(QIcon(os.path.join(iconPath, 'icons8-color-palette-64.png')), 'Select color', self)
		colorAct.setStatusTip('Select color')
		colorAct.triggered.connect(self.selectColor)
		# new line
		newLineAct = QAction(QIcon(os.path.join(iconPath, 'icons8-line-64.png')), 'Create new line', self)
		newLineAct.setStatusTip('Create new line')
		newLineAct.setShortcut('Shift+Ctrl+L')
		newLineAct.triggered.connect(self.newLine)
		# new polygon
		newPolygonAct = QAction(QIcon(os.path.join(iconPath, 'icons8-polygon-64.png')), 'Create new polygon', self)
		newPolygonAct.setStatusTip('Create new polygon')
		newPolygonAct.setShortcut('Shift+Ctrl+P')
		newPolygonAct.triggered.connect(self.newPolygon)
		# new ellipse
		newEllipseAct = QAction(QIcon(os.path.join(iconPath, 'icons8-sphere-64.png')), 'Create new ellipse', self)
		newEllipseAct.setStatusTip('Create new ellipse')
		newEllipseAct.setShortcut('Shift+Ctrl+E')
		newEllipseAct.triggered.connect(self.newEllipse)
		# new curve
		newCurveAct = QAction(QIcon(os.path.join(iconPath, 'icons8-graph-report-64.png')), 'Create new curve', self)
		newCurveAct.setStatusTip('Create new curve')
		newCurveAct.setShortcut('Shift+Ctrl+C')
		newCurveAct.triggered.connect(self.newCurve)

		self.toolbar.addAction(newLineAct)
		self.toolbar.addAction(newPolygonAct)
		self.toolbar.addAction(newEllipseAct)
		self.toolbar.addAction(newCurveAct)
		self.toolbar.addSeparator()
		self.toolbar.addAction(colorAct)


	def setUpStatusBar(self):
		self.statusbar = self.statusBar()
		self.statusbar.showMessage('Ready')
		# print("statusbar: {}".format(self.statusbar.size()))

	def setUpCanvas(self):
		self.canvas = Canvas()
		self.setCentralWidget(self.canvas)
		self.setMouseTracking(True)

	def resetCanvasSize(self, w, h):
		if not (isinstance(w,int) and isinstance(h,int) and 100<=w<=1000 and 100<=h<=1000):
			print("Set default canvas size.")
			w = self.canvas.width()-self.canvasOffset*2
			h = self.canvas.height()-self.canvasOffset*2
		self.canvas.setCanvasSize(w, h)

	def newCanvas(self, w=None, h=None):
		# TODO: Ask if need to save old canvas
		if self.canvas.hasCanvas:
			print("save canvas query not implemented yet")

		tmpDict = {"w": -1, "h": -1}
		win = PUWGetCanvasSize(tmpDict, self)
		self.resetCanvasSize(tmpDict['w'], tmpDict['h'])
		self.canvas.newCanvas()
		self.path = None

	def popUpMsg(self, text):
		msg = QMessageBox()
		pixmap = QPixmap(os.path.join(iconPath, 'icons8-cartoon-face-64.png'))
		msg.setIconPixmap(pixmap)
		msg.setText(text)
		msg.exec_()


	def openFile(self):
		fileDlg = QFileDialog()
		fileDlg.setFilter(fileDlg.filter() | QDir.Hidden)
		fname = fileDlg.getOpenFileName(self, 'Open image', './Demos/')
		if fname[0]:
			if fname[0][-4:] not in imageTypes:
				# pop up msg: can only open .bmp file
				self.popUpMsg("Can only open image-typed files.")
			else:
				# TODO: show the file 
				print("Open file functionality has not been implemented yet.")


	def saveFile(self):
		if not self.canvas.hasCanvas:
			self.popUpMsg("Should create a canvas before saving the canvas.")
		else:
			if self.path is None:
				self.saveFileAs()
			else:
				self.canvas.saveCanvas(self.path)


	def saveFileAs(self):
		if not self.canvas.hasCanvas:
			self.popUpMsg("Should create a canvas before saving the canvas.")
		else:
			fileDlg = QFileDialog()
			# fileDlg.setFilter(fileDlg.filter() | QDir.Hidden)
			# fileDlg.setDefaultSuffix('bmp')
			fileDlg.setDirectory("./Demos/")
			fileDlg.setAcceptMode(QFileDialog.AcceptSave)
			# fileDlg.setNameFilters(['PBM (*.bmp)'])
			# fileDlg.selectFile(strftime("%Y%m%d-%H%M%S.bmp")
			# fname = fileDlg.getSaveFileName(self, 'Save image', '.', 'PBM (*.bmp)')
			if fileDlg.exec_() == QDialog.Accepted:
				path = fileDlg.selectedFiles()[0]
				self.canvas.saveCanvas(path)
				self.path = path


	def toggleToolBar(self, state):
		if state:
			self.toolbar.show()
		else:
			self.toolbar.hide()

	def toggleStatusBar(self, state):
		if state:
			self.statusbar.show()
		else:
			self.statusbar.hide()

	def selectColor(self):
		colDlg = QColorDialog(self)
		# colDlg.mapToParent(QPoint(100, 100))
		color = colDlg.getColor()
		if color.isValid():
			self.curColor = color


	# Some bug when resizing canvas
	def toCanvasCoord(self, x, y):
		cx = x - self.canvasOffset - self.canvasPos.x()
		cy = y - self.canvasOffset - self.canvasPos.y()
		return cx, cy

	# Some bug when resizing canvas
	def pointInRange(self, x, y):
		return 0<=x<=self.canvas.getWidth and 0<=y<=self.canvas.getHeight


	# Some bug when resizing canvas
	def mousePressEvent(self, e):
		x, y = self.toCanvasCoord(e.x(), e.y())
		if self.pointInRange(x, y):
			text = "(x: {0}, y: {1})".format(x, y)
			self.statusbar.showMessage(text)

	def mouseMoveEvent(self, e):
		return self.mousePressEvent(e)

	def newLine(self):
		if self.canvas.hasCanvas:
			# TODO: implement algorithm choice
			# TODO: judge if point valid
			pArr = []
			pWin = PUWGetLineSettings(pArr, self)
			if pArr:
				self.canvas.newLine(self.curColor, p1=pArr[0], p2=pArr[1])
		else:
			self.popUpMsg("Should create a canvas before drawing a line.")
	
	def newPolygon(self):
		if self.canvas.hasCanvas:
			# TODO: implement input points
			# TODO: judge if point valid
			self.canvas.newPolygon(self.curColor)
		else:
			self.popUpMsg("Should create a canvas before drawing a polygon.")

	def newEllipse(self):
		if self.canvas.hasCanvas:
			# TODO: implement algorithm choice
			# TODO: judge if point valid
			rCenter = []
			rArr = []
			pWin = PUWGetEllipseSettings(rCenter, rArr, self)
			if rArr:
				self.canvas.newEllipse(self.curColor, rCenter=rCenter[0], rx=rArr[0], ry=rArr[1])
		else:
			self.popUpMsg("Should create a canvas before drawing a ellipse.")

	def newCurve(self):
		if self.canvas.hasCanvas:
			# TODO: implement algorithm choice
			# TODO: judge if point valid
			self.canvas.newCurve(self.curColor)
		else:
			self.popUpMsg("Should create a canvas before drawing a curve.")



if __name__ == '__main__':
	
	print("sys.argv: {}".format(sys.argv))
	# args = parseArgs(sys.argv)
	app = QApplication(sys.argv)
	ex = MainWindow()
	sys.exit(app.exec_())

