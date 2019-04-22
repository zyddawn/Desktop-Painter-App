# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import * 
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
from Canvas import Canvas

iconPath = './Icons'
imageTypes = ['.bmp', '.png', '.jpeg']

class MainWindow(QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.initUI()
		self.canvas = None

	def initUI(self):
		self.setUpWindow(0.8)
		self.setUpMenu()
		self.setStatusBar()
		self.setCanvas()
		self.show()

	def setUpWindow(self, ratio=0.8):
		ScreenRect = QDesktopWidget().availableGeometry()
		[x, y, w, h] = [ScreenRect.x(), ScreenRect.y(), ScreenRect.width(), ScreenRect.height()]
		self.setGeometry((1-ratio)*w/2+x, (1-ratio)*h/2+y, ratio*w, ratio*h)
		self.setWindowTitle("Yudong Zhang's Mini CG System")

	def setCanvas(self):
		self.canvas = Canvas()
		self.canvas.setPixmap(QPixmap(os.path.join('.', 'test.bmp')))
		vbox = QVBoxLayout()
		vbox.addWidget(self.canvas)
		canvasContainer = QWidget(self)
		canvasContainer.setLayout(vbox)
		self.setCentralWidget(canvasContainer)

	def refreshCanvas(self):
		pass



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
		# saveAct.triggered.connect(self.saveFile)
		# Save as file
		saveAsAct = QAction(QIcon(os.path.join(iconPath, 'icons8-save-as-64.png')), 'Save as...', self)
		saveAsAct.setShortcut('Shift+Ctrl+S')
		saveAsAct.setStatusTip('Save file as...')
		# saveAsAct.triggered.connect(self.saveFileAs)
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
		toolbar = self.addToolBar("Operations")
		# choose color 
		colorAct = QAction(QIcon(os.path.join(iconPath, 'icons8-color-palette-64')), 'Select color', self)
		colorAct.setStatusTip('Select color')
		colorAct.triggered.connect(self.selectColor)

		# choose line width
		## TODO

		toolbar.addAction(newAct)
		toolbar.addAction(openAct)
		toolbar.addAction(saveAct)
		toolbar.addAction(saveAsAct)
		toolbar.addSeparator()
		toolbar.addAction(colorAct)



	def setStatusBar(self):
		self.statusbar = self.statusBar()
		self.statusbar.showMessage('Ready')


	def newCanvas(self):
		# Ask if need to save old canvas
		print("Function newCanvas has not been implemented yet.")
		pass


	def openFile(self):
		fname = QFileDialog.getOpenFileName(self, 'Open file', '.')
		if fname[0]:
			if fname[0][-4:] not in imageTypes:
				# pop up msg: can only open .bmp file
				msg = QMessageBox()
				pixmap = QPixmap(os.path.join(iconPath, 'icons8-cartoon-face-64.png'))
										# .scaledToHeight(32, QtCore.Qt.SmoothTransformation)
				msg.setIconPixmap(pixmap)
				msg.setText("Can only open image-typed files.")
				msg.exec_()
			else:
				# TODO: show the file 
				print("Open file functionality has not been implemented yet.")


	def saveFile(self):
		print("Function saveFile has not been implemented yet.")
		pass


	def saveFileAs(self):
		print("Function saveFileAs has not been implemented yet.")
		pass


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
			## set color for certain objects
			print("Function selectColor has not been implemented yet.")
			pass


if __name__ == '__main__':
	print("sys.argv: {}".format(sys.argv))
	app = QApplication(sys.argv)
	ex = MainWindow()
	sys.exit(app.exec_())

