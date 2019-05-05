from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *

# PUW refer to pop-up-window
class PUWGetCanvasSize(QDialog):
	def __init__(self, tmpDict, parent=None):
		super(PUWGetCanvasSize, self).__init__(parent)
		self.tmpDict = tmpDict
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
		self.tmpDict['w'], self.tmpDict['h'] = int(self.widthEdit.text()), int(self.heightEdit.text())
		self.close()
		
	def clickCancel(self):
		self.close()


class PUWGetLineSettings(QDialog):
	def __init__(self, pArr, parent=None):
		super(PUWGetLineSettings, self).__init__(parent)
		self.pArr = pArr
		self.initUI()

	def initUI(self):
		self.setFixedSize(300, 200)
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
		self.x1Edit.setText('10')
		self.y1Edit.setText('10')
		self.x2Edit.setText('20')
		self.y2Edit.setText('20')
		OkBtn = QPushButton("OK")
		OkBtn.clicked.connect(self.clickOK)
		OkBtn.setShortcut("Enter")
		OkBtn.setAutoDefault(True)
		CancelBtn = QPushButton("Cancel")
		CancelBtn.clicked.connect(self.clickCancel)
		CancelBtn.setAutoDefault(False)
		
		grid = QGridLayout()
		grid.addWidget(x1, 1, 0)
		grid.addWidget(self.x1Edit, 1, 1)
		grid.addWidget(y1, 1, 2)
		grid.addWidget(self.y1Edit, 1, 3)
		grid.addWidget(x2, 2, 0)
		grid.addWidget(self.x2Edit, 2, 1)
		grid.addWidget(y2, 2, 2)
		grid.addWidget(self.y2Edit, 2, 3)
		grid.addWidget(QLabel(""), 3, 0)
		grid.addWidget(CancelBtn, 3, 1)
		grid.addWidget(OkBtn, 3, 2)
		grid.addWidget(QLabel(""), 3, 3)
		
		self.setLayout(grid)
		self.exec()

	def clickOK(self):
		self.pArr.append(QPoint(int(self.x1Edit.text()), int(self.y1Edit.text())))
		self.pArr.append(QPoint(int(self.x2Edit.text()), int(self.y2Edit.text())))
		self.close()
		
	def clickCancel(self):
		self.close()


class PUWGetEllipseSettings(QDialog):
	def __init__(self, rCenter, rArr, parent=None):
		super(PUWGetEllipseSettings, self).__init__(parent)
		self.rCenter = rCenter
		self.rArr = rArr
		self.initUI()

	def initUI(self):
		self.setFixedSize(300, 200)
		self.setWindowTitle("Line settings")
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
		self.xEdit.setText('200')
		self.yEdit.setText('200')
		self.rxEdit.setText('60')
		self.ryEdit.setText('60')
		OkBtn = QPushButton("OK")
		OkBtn.clicked.connect(self.clickOK)
		OkBtn.setShortcut("Enter")
		OkBtn.setAutoDefault(True)
		CancelBtn = QPushButton("Cancel")
		CancelBtn.clicked.connect(self.clickCancel)
		CancelBtn.setAutoDefault(False)
		
		grid = QGridLayout()
		grid.addWidget(x, 1, 0)
		grid.addWidget(self.xEdit, 1, 1)
		grid.addWidget(y, 1, 2)
		grid.addWidget(self.yEdit, 1, 3)
		grid.addWidget(rx, 2, 0)
		grid.addWidget(self.rxEdit, 2, 1)
		grid.addWidget(ry, 2, 2)
		grid.addWidget(self.ryEdit, 2, 3)
		grid.addWidget(QLabel(""), 3, 0)
		grid.addWidget(CancelBtn, 3, 1)
		grid.addWidget(OkBtn, 3, 2)
		grid.addWidget(QLabel(""), 3, 3)
		
		self.setLayout(grid)
		self.exec()

	def clickOK(self):
		self.rCenter.append(QPoint(int(self.xEdit.text()), int(self.yEdit.text())))
		self.rArr.append(int(self.rxEdit.text()))
		self.rArr.append(int(self.ryEdit.text()))
		self.close()
		
	def clickCancel(self):
		self.close()





