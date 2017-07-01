import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Editor(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.initUI()

	#-----------------------------
	# toolbar inits
	def initToolBar(self):
		self.toolbar = self.addToolBar("Options")
		# adds a break so new toolbar will be added under this one.
		self.addToolBarBreak()
	
	def initFormatBar(self):
		self.formatbar = self.addToolBar("Format")

	def initMenuBar(self):
		menubar = self.menuBar()

		file = menubar.addMenu("File")
		edit = menubar.addMenu("Edit")
		view = menubar.addMenu("View")
	
	def initStatusBar(self):
		statusbar = self.statusBar()

	#-----------------------------
	# the initial UI
	def initUI(self):
		
		# main text frame
		self.text = QtGui.QTextEdit(self)
		self.setCentralWidget(self.text)
				
		# toolbars
		self.initToolBar()
		self.initFormatBar()
		self.initMenuBar()
		self.initStatusBar()
		
		# window position and name
		self.setGeometry(50, 50, 1266, 668)
		self.setWindowTitle("pyQtEditor")


