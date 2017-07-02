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

		#new
		self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"),"New",self)
		self.newAction.setShortcut("Ctrl+N")
		self.newAction.setStatusTip("Create a new document from scratch.")
		self.newAction.triggered.connect(self.new)

		#open
		self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"),"Open file",self)
		self.openAction.setStatusTip("Open existing document")
		self.openAction.setShortcut("Ctrl+O")
		self.openAction.triggered.connect(self.open)

		#save
		self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),"Save",self)
		self.saveAction.setStatusTip("Save document")
		self.saveAction.setShortcut("Ctrl+S")
		self.saveAction.triggered.connect(self.save)

		self.toolbar = self.addToolBar("Options")

		self.toolbar.addAction(self.newAction)
		self.toolbar.addAction(self.openAction)
		self.toolbar.addAction(self.saveAction)

		self.toolbar.addSeparator()

		# Makes the next toolbar appear underneath this one
		self.addToolBarBreak()

	# --------------------------------------
	# actions
	def new():
		spawn = Main(self)
		spawn.show()

	def open(self):

		self.filename = QtGui.QFileDialog.getOpenFileName(self, 'Open File', ".", "(*.pqe)")

		if self.filename:
			with open(self.filename, "rt") as file:
				self.text.setText(file.read())

	def save(self):
		
		# if the file does not have a name yet
		if not self.filename:
			self.filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File')

		# append extention if its not there
		if not self.filename.endswith(".pqe"):
			self.filename += ".pqe"

		# save the contents as an html
		with open(self.filename, "wt") as file:
			file.write(self.text.toHtml())

	# --------------------------------------------
	def initFormatBar(self):
		self.formatbar = self.addToolBar("Format")

	def initMenuBar(self):

		menubar = self.menuBar()

		file = menubar.addMenu("File")
		edit = menubar.addMenu("Edit")
		view = menubar.addMenu("View")

		file.addAction(self.newAction)
		file.addAction(self.openAction)
		file.addAction(self.saveAction)
		
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


