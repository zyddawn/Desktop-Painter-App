from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random

# PUW refer to pop-up-window
class PUWGetCanvasSize(QDialog):
	def __init__(self, params, parent=None):
		super(PUWGetCanvasSize, self).__init__(parent)
		self.params = params
		self.algorithm = None
		self.initUI()

	def initUI(self):
		self.setFixedSize(200, 150)
		self.setWindowTitle("Canvas settings")
		width = QLabel("Width")
		height = QLabel("Height")
		self.widthEdit = QLineEdit()
		self.heightEdit = QLineEdit()
		self.widthEdit.setFixedWidth(80)
		self.heightEdit.setFixedWidth(80)
		self.widthEdit.setText("0")
		self.heightEdit.setText("0")
		OkBtn = QPushButton("OK")
		OkBtn.clicked.connect(self.clickOK)
		OkBtn.setShortcut("Enter")
		OkBtn.setAutoDefault(True)
		CancelBtn = QPushButton("Cancel")
		CancelBtn.clicked.connect(self.clickCancel)
		CancelBtn.setAutoDefault(False)
		
		grid = QGridLayout()
		grid.addWidget(width, 1, 0)
		grid.addWidget(self.widthEdit, 1, 1)
		grid.addWidget(height, 2, 0)
		grid.addWidget(self.heightEdit, 2, 1)
		grid.addWidget(CancelBtn, 3, 0)
		grid.addWidget(OkBtn, 3, 1)
		
		self.setLayout(grid)
		self.exec()

	def clickOK(self):
		self.params['w'], self.params['h'] = int(self.widthEdit.text()), int(self.heightEdit.text())
		self.close()
		
	def clickCancel(self):
		self.close()


class PUWGetLineSettings(QDialog):
	def __init__(self, params, parent=None):
		super(PUWGetLineSettings, self).__init__(parent)
		self.params = params
		self.algorithm = "Bresenham"
		self.initUI()

	def initUI(self):
		self.setFixedSize(260, 185)
		self.setWindowTitle("Line settings")
		x1 = QLabel("x1")
		y1 = QLabel("y1")
		x2 = QLabel("x2")
		y2 = QLabel("y2")
		self.x1Edit = QLineEdit()
		self.y1Edit = QLineEdit()
		self.x2Edit = QLineEdit()
		self.y2Edit = QLineEdit()
		self.x1Edit.setFixedWidth(60)
		self.y1Edit.setFixedWidth(60)
		self.x2Edit.setFixedWidth(60)
		self.y2Edit.setFixedWidth(60)
		self.x1Edit.setText(str(random.randint(100, 900)))
		self.y1Edit.setText(str(random.randint(100, 500)))
		self.x2Edit.setText(str(random.randint(100, 900)))
		self.y2Edit.setText(str(random.randint(100, 500)))
		# self.x1Edit.setText("0")
		# self.y1Edit.setText("0")
		# self.x2Edit.setText(str(random.randint(0, 300)))
		# self.y2Edit.setText(str(random.randint(0, 300)))
		self.algorithmChoice = QComboBox(self)
		self.algorithmChoice.addItem("Bresenham")
		self.algorithmChoice.addItem("Midpoint")
		self.algorithmChoice.addItem("DDA")
		self.algorithmChoice.activated[str].connect(self.getAlgorithm)
		OkBtn = QPushButton("OK")
		OkBtn.clicked.connect(self.clickOK)
		OkBtn.setShortcut("Enter")
		OkBtn.setAutoDefault(True)
		CancelBtn = QPushButton("Cancel")
		CancelBtn.clicked.connect(self.clickCancel)
		CancelBtn.setAutoDefault(False)
		
		h1boxLayout = QHBoxLayout()
		h1boxLayout.addStretch()
		h1boxLayout.addWidget(x1)
		h1boxLayout.addWidget(self.x1Edit)
		h1boxLayout.addWidget(y1)
		h1boxLayout.addWidget(self.y1Edit)
		h1boxLayout.addStretch()

		h2boxLayout = QHBoxLayout()
		h2boxLayout.addStretch()
		h2boxLayout.addWidget(x2)
		h2boxLayout.addWidget(self.x2Edit)
		h2boxLayout.addWidget(y2)
		h2boxLayout.addWidget(self.y2Edit)
		h2boxLayout.addStretch()

		h3boxLayout = QHBoxLayout()
		h3boxLayout.addStretch()
		h3boxLayout.addWidget(QLabel("Algorithm"))
		h3boxLayout.addWidget(self.algorithmChoice)
		h3boxLayout.addStretch()

		h4boxLayout = QHBoxLayout()
		h4boxLayout.addStretch()
		h4boxLayout.addWidget(OkBtn)
		h4boxLayout.addWidget(CancelBtn)
		h4boxLayout.addStretch()

		mainLayout = QVBoxLayout()
		mainLayout.addLayout(h1boxLayout)
		mainLayout.addLayout(h2boxLayout)
		mainLayout.addLayout(h3boxLayout)
		mainLayout.addLayout(h4boxLayout)
		
		self.setLayout(mainLayout)
		self.exec()

	def clickOK(self):
		self.params['p1'] = QPoint(int(self.x1Edit.text()), int(self.y1Edit.text()))
		self.params['p2'] = QPoint(int(self.x2Edit.text()), int(self.y2Edit.text()))
		self.params['algorithm'] = self.algorithm
		self.close()
		
	def clickCancel(self):
		self.close()

	def getAlgorithm(self, text):
		self.algorithm = text


class PUWGetPolygonSettings(QDialog):
	def __init__(self, params, parent=None):
		super(PUWGetPolygonSettings, self).__init__(parent)
		self.params = params
		self.algorithm = "Bresenham"
		self.pointNumber = 100
		self.initUI()

	def initUI(self):
		self.setFixedSize(350, 320)
		self.setWindowTitle("Curve settings")
		x = QLabel("x")
		y = QLabel("y")
		n = QLabel("n")
		cpTitle = QLabel("Current Points: ")
		self.cpList = QLabel("")
		self.xEdit = QLineEdit()
		self.yEdit = QLineEdit()
		self.nEdit = QLineEdit()
		self.xEdit.setFixedWidth(60)
		self.yEdit.setFixedWidth(60)
		self.nEdit.setFixedWidth(30)
		self.xEdit.setText(str(random.randint(200, 900)))
		self.yEdit.setText(str(random.randint(200, 450)))
		self.nEdit.setText("5")
		self.algorithmChoice = QComboBox(self)
		self.algorithmChoice.addItem("Bresenham")
		self.algorithmChoice.addItem("DDA")
		self.algorithmChoice.activated[str].connect(self.getAlgorithm)
		OkBtn = QPushButton("OK")
		OkBtn.clicked.connect(self.clickOK)
		OkBtn.setShortcut("Enter")
		OkBtn.setAutoDefault(True)
		OkBtn.setDefault(True)
		CancelBtn = QPushButton("Cancel")
		CancelBtn.clicked.connect(self.clickCancel)
		CancelBtn.setAutoDefault(False)
		AddBtn = QPushButton("Add")
		AddBtn.clicked.connect(self.clickAdd)
		
		h1boxLayout = QHBoxLayout()
		h1boxLayout.addStretch()
		h1boxLayout.addWidget(x)
		h1boxLayout.addWidget(self.xEdit)
		h1boxLayout.addWidget(y)
		h1boxLayout.addWidget(self.yEdit)
		h1boxLayout.addWidget(AddBtn)
		h1boxLayout.addStretch()

		h2boxLayout = QHBoxLayout()
		h2boxLayout.addStretch()
		# h2boxLayout.addWidget(cpTitle)
		h2boxLayout.addWidget(self.cpList)
		h2boxLayout.addStretch()

		h3boxLayout = QHBoxLayout()
		h3boxLayout.addStretch()
		h3boxLayout.addWidget(n)
		h3boxLayout.addWidget(self.nEdit)
		h3boxLayout.addWidget(QLabel("Algorithm"))
		h3boxLayout.addWidget(self.algorithmChoice)
		h3boxLayout.addStretch()

		h4boxLayout = QHBoxLayout()
		h4boxLayout.addStretch()
		h4boxLayout.addWidget(OkBtn)
		h4boxLayout.addWidget(CancelBtn)
		h4boxLayout.addStretch()

		h5boxLayout = QHBoxLayout()
		h5boxLayout.addStretch()
		h5boxLayout.addWidget(cpTitle)
		h5boxLayout.addStretch()

		mainLayout = QVBoxLayout()
		mainLayout.addLayout(h1boxLayout)
		mainLayout.addLayout(h3boxLayout)
		mainLayout.addLayout(h5boxLayout)
		mainLayout.addLayout(h2boxLayout)
		mainLayout.addLayout(h4boxLayout)
		
		self.setLayout(mainLayout)
		self.exec()

	def clickAdd(self):
		self.pointNumber = int(self.nEdit.text())
		x, y = int(self.xEdit.text()), int(self.yEdit.text())
		if 'points' not in self.params.keys() and self.pointNumber > 0:
			self.params['points'] = [(x, y), ]
		elif self.pointNumber > len(self.params['points']):
			self.params['points'].append((x, y))
		# set text
		self.cpList.setWordWrap(True)
		self.cpList.setText(str(self.params['points']))
		self.adjustSize()

	def clickOK(self):
		if 'points' in self.params.keys():
			self.params['algorithm'] = self.algorithm
		self.close()

	def clickCancel(self):
		self.close()
		
	def getAlgorithm(self, text):
		self.algorithm = text



class PUWGetEllipseSettings(QDialog):
	def __init__(self, params, parent=None):
		super(PUWGetEllipseSettings, self).__init__(parent)
		self.params = params
		self.algorithm = "Midpoint-circle"
		self.initUI()

	def initUI(self):
		self.setFixedSize(260, 185)
		self.setWindowTitle("Ellipse settings")
		x = QLabel("x")
		y = QLabel("y")
		rx = QLabel("rx")
		ry = QLabel("ry")
		self.xEdit = QLineEdit()
		self.yEdit = QLineEdit()
		self.rxEdit = QLineEdit()
		self.ryEdit = QLineEdit()
		self.xEdit.setFixedWidth(60)
		self.yEdit.setFixedWidth(60)
		self.rxEdit.setFixedWidth(60)
		self.ryEdit.setFixedWidth(60)
		self.xEdit.setText(str(random.randint(200, 900)))
		self.yEdit.setText(str(random.randint(200, 450)))
		self.rxEdit.setText(str(random.randint(50, 100)))
		self.ryEdit.setText(str(random.randint(50, 100)))
		self.algorithmChoice = QComboBox(self)
		self.algorithmChoice.addItem("Midpoint-circle")
		self.algorithmChoice.activated[str].connect(self.getAlgorithm)
		OkBtn = QPushButton("OK")
		OkBtn.clicked.connect(self.clickOK)
		OkBtn.setShortcut("Enter")
		OkBtn.setAutoDefault(True)
		CancelBtn = QPushButton("Cancel")
		CancelBtn.clicked.connect(self.clickCancel)
		CancelBtn.setAutoDefault(False)
		
		h1boxLayout = QHBoxLayout()
		h1boxLayout.addStretch()
		h1boxLayout.addWidget(x)
		h1boxLayout.addWidget(self.xEdit)
		h1boxLayout.addWidget(y)
		h1boxLayout.addWidget(self.yEdit)
		h1boxLayout.addStretch()

		h2boxLayout = QHBoxLayout()
		h2boxLayout.addStretch()
		h2boxLayout.addWidget(rx)
		h2boxLayout.addWidget(self.rxEdit)
		h2boxLayout.addWidget(ry)
		h2boxLayout.addWidget(self.ryEdit)
		h2boxLayout.addStretch()

		h3boxLayout = QHBoxLayout()
		h3boxLayout.addStretch()
		h3boxLayout.addWidget(QLabel("Algorithm"))
		h3boxLayout.addWidget(self.algorithmChoice)
		h3boxLayout.addStretch()

		h4boxLayout = QHBoxLayout()
		h4boxLayout.addStretch()
		h4boxLayout.addWidget(OkBtn)
		h4boxLayout.addWidget(CancelBtn)
		h4boxLayout.addStretch()

		mainLayout = QVBoxLayout()
		mainLayout.addLayout(h1boxLayout)
		mainLayout.addLayout(h2boxLayout)
		mainLayout.addLayout(h3boxLayout)
		mainLayout.addLayout(h4boxLayout)
		
		self.setLayout(mainLayout)
		self.exec()

	def clickOK(self):
		self.params['center'] = QPoint(int(self.xEdit.text()), int(self.yEdit.text()))
		self.params['rx'] = int(self.rxEdit.text())
		self.params['ry'] = int(self.ryEdit.text())
		self.params['algorithm'] = self.algorithm
		self.close()

	def clickCancel(self):
		self.close()

	def getAlgorithm(self, text):
		self.algorithm = text


class PUWGetCurveSettings(QDialog):
	def __init__(self, params, parent=None):
		super(PUWGetCurveSettings, self).__init__(parent)
		self.params = params
		self.algorithm = "Bezier"
		self.pointNumber = 100
		self.initUI()

	def initUI(self):
		self.setFixedSize(350, 320)
		self.setWindowTitle("Curve settings")
		x = QLabel("x")
		y = QLabel("y")
		n = QLabel("n")
		cpTitle = QLabel("Current Points: ")
		self.cpList = QLabel("")
		self.xEdit = QLineEdit()
		self.yEdit = QLineEdit()
		self.nEdit = QLineEdit()
		self.xEdit.setFixedWidth(60)
		self.yEdit.setFixedWidth(60)
		self.nEdit.setFixedWidth(30)
		self.xEdit.setText(str(random.randint(200, 900)))
		self.yEdit.setText(str(random.randint(200, 450)))
		self.nEdit.setText("5")
		self.algorithmChoice = QComboBox(self)
		self.algorithmChoice.addItem("Bezier")
		self.algorithmChoice.addItem("B-spline")
		self.algorithmChoice.activated[str].connect(self.getAlgorithm)
		OkBtn = QPushButton("OK")
		OkBtn.clicked.connect(self.clickOK)
		OkBtn.setShortcut("Enter")
		OkBtn.setAutoDefault(True)
		OkBtn.setDefault(True)
		CancelBtn = QPushButton("Cancel")
		CancelBtn.clicked.connect(self.clickCancel)
		CancelBtn.setAutoDefault(False)
		AddBtn = QPushButton("Add")
		AddBtn.clicked.connect(self.clickAdd)
		
		h1boxLayout = QHBoxLayout()
		h1boxLayout.addStretch()
		h1boxLayout.addWidget(x)
		h1boxLayout.addWidget(self.xEdit)
		h1boxLayout.addWidget(y)
		h1boxLayout.addWidget(self.yEdit)
		h1boxLayout.addWidget(AddBtn)
		h1boxLayout.addStretch()

		h2boxLayout = QHBoxLayout()
		h2boxLayout.addStretch()
		# h2boxLayout.addWidget(cpTitle)
		h2boxLayout.addWidget(self.cpList)
		h2boxLayout.addStretch()

		h3boxLayout = QHBoxLayout()
		h3boxLayout.addStretch()
		h3boxLayout.addWidget(n)
		h3boxLayout.addWidget(self.nEdit)
		h3boxLayout.addWidget(QLabel("Algorithm"))
		h3boxLayout.addWidget(self.algorithmChoice)
		h3boxLayout.addStretch()

		h4boxLayout = QHBoxLayout()
		h4boxLayout.addStretch()
		h4boxLayout.addWidget(OkBtn)
		h4boxLayout.addWidget(CancelBtn)
		h4boxLayout.addStretch()

		h5boxLayout = QHBoxLayout()
		h5boxLayout.addStretch()
		h5boxLayout.addWidget(cpTitle)
		h5boxLayout.addStretch()

		mainLayout = QVBoxLayout()
		mainLayout.addLayout(h1boxLayout)
		mainLayout.addLayout(h3boxLayout)
		mainLayout.addLayout(h5boxLayout)
		mainLayout.addLayout(h2boxLayout)
		mainLayout.addLayout(h4boxLayout)
		
		self.setLayout(mainLayout)
		self.exec()

	def clickAdd(self):
		self.pointNumber = int(self.nEdit.text())
		x, y = int(self.xEdit.text()), int(self.yEdit.text())
		if 'points' not in self.params.keys() and self.pointNumber > 0:
			self.params['points'] = [(x, y), ]
		elif self.pointNumber > len(self.params['points']):
			self.params['points'].append((x, y))
		# set text
		self.cpList.setWordWrap(True)
		self.cpList.setText(str(self.params['points']))
		self.adjustSize()

	def clickOK(self):
		if 'points' in self.params.keys():
			self.params['algorithm'] = self.algorithm
		self.close()

	def clickCancel(self):
		self.close()
		
	def getAlgorithm(self, text):
		self.algorithm = text


class PUWGetTranslateSettings(QDialog):
	def __init__(self, params, parent=None):
		super(PUWGetTranslateSettings, self).__init__(parent)
		self.params = params
		self.initUI()

	def initUI(self):
		self.setFixedSize(270, 150)
		self.setWindowTitle("Translate settings")
		Id = QLabel("id")
		dx = QLabel("dx")
		dy = QLabel("dy")
		self.idEdit = QLineEdit()
		self.dxEdit = QLineEdit()
		self.dyEdit = QLineEdit()
		self.idEdit.setFixedWidth(40)
		self.dxEdit.setFixedWidth(40)
		self.dyEdit.setFixedWidth(40)
		self.idEdit.setText("0")
		self.dxEdit.setText("200")
		self.dyEdit.setText("0")
		OkBtn = QPushButton("OK")
		OkBtn.clicked.connect(self.clickOK)
		OkBtn.setShortcut("Enter")
		OkBtn.setAutoDefault(True)
		CancelBtn = QPushButton("Cancel")
		CancelBtn.clicked.connect(self.clickCancel)
		CancelBtn.setAutoDefault(False)

		h1boxLayout = QHBoxLayout()
		h1boxLayout.addStretch()
		h1boxLayout.addWidget(Id)
		h1boxLayout.addWidget(self.idEdit)
		h1boxLayout.addWidget(dx)
		h1boxLayout.addWidget(self.dxEdit)
		h1boxLayout.addWidget(dy)
		h1boxLayout.addWidget(self.dyEdit)
		h1boxLayout.addStretch()

		h2boxLayout = QHBoxLayout()
		h2boxLayout.addStretch()
		h2boxLayout.addWidget(OkBtn)
		h2boxLayout.addWidget(CancelBtn)
		h2boxLayout.addStretch()

		mainLayout = QVBoxLayout()
		mainLayout.addLayout(h1boxLayout)
		mainLayout.addLayout(h2boxLayout)
		
		self.setLayout(mainLayout)
		self.exec()

	def clickOK(self):
		self.params['id'] = int(self.idEdit.text())
		self.params['dx'] = int(self.dxEdit.text())
		self.params['dy'] = int(self.dyEdit.text())
		self.close()

	def clickCancel(self):
		self.close()


class PUWGetRotateSettings(QDialog):
	def __init__(self, params, parent=None):
		super(PUWGetRotateSettings, self).__init__(parent)
		self.params = params
		self.initUI()

	def initUI(self):
		self.setFixedSize(280, 180)
		self.setWindowTitle("Rotate settings")
		Id = QLabel("Id")
		x = QLabel("Center x")
		y = QLabel("Center y")
		angle = QLabel("Clockwise angle")
		self.idEdit = QLineEdit()
		self.xEdit = QLineEdit()
		self.yEdit = QLineEdit()
		self.angleEdit = QLineEdit()
		self.idEdit.setFixedWidth(30)
		self.xEdit.setFixedWidth(40)
		self.yEdit.setFixedWidth(40)
		self.angleEdit.setFixedWidth(40)
		self.idEdit.setText("0")
		self.xEdit.setText("500")
		self.yEdit.setText("200")
		self.angleEdit.setText("180")
		OkBtn = QPushButton("OK")
		OkBtn.clicked.connect(self.clickOK)
		OkBtn.setShortcut("Enter")
		OkBtn.setAutoDefault(True)
		CancelBtn = QPushButton("Cancel")
		CancelBtn.clicked.connect(self.clickCancel)
		CancelBtn.setAutoDefault(False)
		
		h1boxLayout = QHBoxLayout()
		h1boxLayout.addStretch()
		h1boxLayout.addWidget(Id)
		h1boxLayout.addWidget(self.idEdit)
		h1boxLayout.addWidget(angle)
		h1boxLayout.addWidget(self.angleEdit)
		h1boxLayout.addStretch()

		h2boxLayout = QHBoxLayout()
		h2boxLayout.addStretch()
		h2boxLayout.addWidget(x)
		h2boxLayout.addWidget(self.xEdit)
		h2boxLayout.addWidget(y)
		h2boxLayout.addWidget(self.yEdit)
		h2boxLayout.addStretch()

		h3boxLayout = QHBoxLayout()
		h3boxLayout.addStretch()
		h3boxLayout.addWidget(OkBtn)
		h3boxLayout.addWidget(CancelBtn)
		h3boxLayout.addStretch()

		mainLayout = QVBoxLayout()
		mainLayout.addLayout(h1boxLayout)
		mainLayout.addLayout(h2boxLayout)
		mainLayout.addLayout(h3boxLayout)
		
		self.setLayout(mainLayout)
		self.exec()

	def clickOK(self):
		self.params['id'] = int(self.idEdit.text())
		self.params['x'] = int(self.xEdit.text())
		self.params['y'] = int(self.yEdit.text())
		self.params['angle'] = int(self.angleEdit.text())
		self.close()

	def clickCancel(self):
		self.close()


class PUWGetScaleSettings(QDialog):
	def __init__(self, params, parent=None):
		super(PUWGetScaleSettings, self).__init__(parent)
		self.params = params
		self.initUI()

	def initUI(self):
		self.setFixedSize(280, 180)
		self.setWindowTitle("Scale settings")
		Id = QLabel("Id")
		x = QLabel("Center x")
		y = QLabel("Center y")
		scale = QLabel("Scale size")
		self.idEdit = QLineEdit()
		self.xEdit = QLineEdit()
		self.yEdit = QLineEdit()
		self.scaleEdit = QLineEdit()
		self.idEdit.setFixedWidth(40)
		self.xEdit.setFixedWidth(40)
		self.yEdit.setFixedWidth(40)
		self.scaleEdit.setFixedWidth(50)
		self.idEdit.setText("0")
		self.xEdit.setText("500")
		self.yEdit.setText("200")
		self.scaleEdit.setText("0.5")
		OkBtn = QPushButton("OK")
		OkBtn.clicked.connect(self.clickOK)
		OkBtn.setShortcut("Enter")
		OkBtn.setAutoDefault(True)
		CancelBtn = QPushButton("Cancel")
		CancelBtn.clicked.connect(self.clickCancel)
		CancelBtn.setAutoDefault(False)
		
		h1boxLayout = QHBoxLayout()
		h1boxLayout.addStretch()
		h1boxLayout.addWidget(Id)
		h1boxLayout.addWidget(self.idEdit)
		h1boxLayout.addWidget(scale)
		h1boxLayout.addWidget(self.scaleEdit)
		h1boxLayout.addStretch()

		h2boxLayout = QHBoxLayout()
		h2boxLayout.addStretch()
		h2boxLayout.addWidget(x)
		h2boxLayout.addWidget(self.xEdit)
		h2boxLayout.addWidget(y)
		h2boxLayout.addWidget(self.yEdit)
		h2boxLayout.addStretch()

		h3boxLayout = QHBoxLayout()
		h3boxLayout.addStretch()
		h3boxLayout.addWidget(OkBtn)
		h3boxLayout.addWidget(CancelBtn)
		h3boxLayout.addStretch()

		mainLayout = QVBoxLayout()
		mainLayout.addLayout(h1boxLayout)
		mainLayout.addLayout(h2boxLayout)
		mainLayout.addLayout(h3boxLayout)
		
		self.setLayout(mainLayout)
		self.exec()

	def clickOK(self):
		self.params['id'] = int(self.idEdit.text())
		self.params['x'] = int(self.xEdit.text())
		self.params['y'] = int(self.yEdit.text())
		self.params['scale'] = float(self.scaleEdit.text())
		self.close()

	def clickCancel(self):
		self.close()


class PUWGetClipLineSettings(QDialog):
	def __init__(self, params, parent=None):
		super(PUWGetClipLineSettings, self).__init__(parent)
		self.params = params
		self.algorithm = "Cohen-Sutherland"
		self.initUI()

	def initUI(self):
		self.setFixedSize(320, 180)
		self.setWindowTitle("Clip Line settings")
		Id = QLabel("id")
		x1 = QLabel("x1")
		y1 = QLabel("y1")
		x2 = QLabel("x2")
		y2 = QLabel("y2")
		self.idEdit = QLineEdit()
		self.x1Edit = QLineEdit()
		self.y1Edit = QLineEdit()
		self.x2Edit = QLineEdit()
		self.y2Edit = QLineEdit()
		self.idEdit.setFixedWidth(30)
		self.x1Edit.setFixedWidth(40)
		self.y1Edit.setFixedWidth(40)
		self.x2Edit.setFixedWidth(40)
		self.y2Edit.setFixedWidth(40)
		self.idEdit.setText("0")
		self.x1Edit.setText("100")
		self.y1Edit.setText("100")
		self.x2Edit.setText("200")
		self.y2Edit.setText("200")
		self.algorithmChoice = QComboBox(self)
		self.algorithmChoice.addItem("Cohen-Sutherland")
		self.algorithmChoice.addItem("Liang-Barsky")
		self.algorithmChoice.activated[str].connect(self.getAlgorithm)
		OkBtn = QPushButton("OK")
		OkBtn.clicked.connect(self.clickOK)
		OkBtn.setShortcut("Enter")
		OkBtn.setAutoDefault(True)
		CancelBtn = QPushButton("Cancel")
		CancelBtn.clicked.connect(self.clickCancel)
		CancelBtn.setAutoDefault(False)
		
		h1boxLayout = QHBoxLayout()
		h1boxLayout.addStretch()
		h1boxLayout.addWidget(Id)
		h1boxLayout.addWidget(self.idEdit)
		h1boxLayout.addWidget(QLabel("Algorithm"))
		h1boxLayout.addWidget(self.algorithmChoice)
		h1boxLayout.addStretch()

		h2boxLayout = QHBoxLayout()
		h2boxLayout.addStretch()
		h2boxLayout.addWidget(x1)
		h2boxLayout.addWidget(self.x1Edit)
		h2boxLayout.addWidget(y1)
		h2boxLayout.addWidget(self.y1Edit)
		h2boxLayout.addWidget(x2)
		h2boxLayout.addWidget(self.x2Edit)
		h2boxLayout.addWidget(y2)
		h2boxLayout.addWidget(self.y2Edit)
		h2boxLayout.addStretch()

		h4boxLayout = QHBoxLayout()
		h4boxLayout.addStretch()
		h4boxLayout.addWidget(OkBtn)
		h4boxLayout.addWidget(CancelBtn)
		h4boxLayout.addStretch()

		mainLayout = QVBoxLayout()
		mainLayout.addLayout(h1boxLayout)
		mainLayout.addLayout(h2boxLayout)
		mainLayout.addLayout(h4boxLayout)
		
		self.setLayout(mainLayout)
		self.exec()

	def clickOK(self):
		self.params['id'] = int(self.idEdit.text())
		self.params['x1'] = int(self.x1Edit.text())
		self.params['y1'] = int(self.y1Edit.text())
		self.params['x2'] = int(self.x2Edit.text())
		self.params['y2'] = int(self.y2Edit.text())
		self.params['algorithm'] = self.algorithm
		self.close()

	def clickCancel(self):
		self.close()

	def getAlgorithm(self, text):
		self.algorithm = text


