import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Editor(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		filename = ""
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

		#print
		self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"),"Print document",self)
		self.printAction.setStatusTip("Print document")
		self.printAction.setShortcut("Ctrl+P")
		self.printAction.triggered.connect(self.printHandler)

		#preview
		self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"),"Page view",self)
		self.previewAction.setStatusTip("Preview page before printing")
		self.previewAction.setShortcut("Ctrl+Shift+P")
		self.previewAction.triggered.connect(self.preview)

		# #cut
		# self.cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"),"Cut to clipboard",self)
		# self.cutAction.setStatusTip("Delete and copy text to clipboard")
		# self.cutAction.setShortcut("Ctrl+X")
		# self.cutAction.triggered.connect(self.text.cut)

		# #copy
		# self.copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"),"Copy to clipboard",self)
		# self.copyAction.setStatusTip("Copy text to clipboard")
		# self.copyAction.setShortcut("Ctrl+C")
		# self.copyAction.triggered.connect(self.text.copy)

		# #paste
		# self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"),"Paste from clipboard",self)
		# self.pasteAction.setStatusTip("Paste text from clipboard")
		# self.pasteAction.setShortcut("Ctrl+V")
		# self.pasteAction.triggered.connect(self.text.paste)

		# #undo
		# self.undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"),"Undo last action",self)
		# self.undoAction.setStatusTip("Undo last action")
		# self.undoAction.setShortcut("Ctrl+Z")
		# self.undoAction.triggered.connect(self.text.undo)

		# #redo
		# self.redoAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"),"Redo last undone thing",self)
		# self.redoAction.setStatusTip("Redo last undone thing")
		# self.redoAction.setShortcut("Ctrl+Y")
		# self.redoAction.triggered.connect(self.text.redo)

		# #bulletList
		# bulletAction = QtGui.QAction(QtGui.QIcon("icons/bullet.png"),"Insert bullet List",self)
		# bulletAction.setStatusTip("Insert bullet list")
		# bulletAction.setShortcut("Ctrl+Shift+B")
		# bulletAction.triggered.connect(self.bulletList)

		# #numberedList
		# numberedAction = QtGui.QAction(QtGui.QIcon("icons/number.png"),"Insert numbered List",self)
		# numberedAction.setStatusTip("Insert numbered list")
		# numberedAction.setShortcut("Ctrl+Shift+L")
		# numberedAction.triggered.connect(self.numberList)

		self.toolbar = self.addToolBar("Options")

		self.toolbar.addAction(self.newAction)
		self.toolbar.addAction(self.openAction)
		self.toolbar.addAction(self.saveAction)

		self.toolbar.addSeparator()
		
		self.toolbar.addAction(self.printAction)
		self.toolbar.addAction(self.previewAction)
		
		self.toolbar.addSeparator()

		# Makes the next toolbar appear underneath this one
		self.addToolBarBreak()

	def initFormatBar(self):
		self.formatbar = self.addToolBar("Format")

	def initMenuBar(self):

		menubar = self.menuBar()

		file = menubar.addMenu("File")
		edit = menubar.addMenu("Edit")
		view = menubar.addMenu("View")

		# file actions
		file.addAction(self.newAction)
		file.addAction(self.openAction)
		file.addAction(self.saveAction)
		file.addAction(self.printAction)
		file.addAction(self.previewAction)

		# edit.addAction(self.undoAction)
		# edit.addAction(self.redoAction)
		# edit.addAction(self.cutAction)
		# edit.addAction(self.copyAction)
		# edit.addAction(self.pasteAction)

	
	def initStatusBar(self):
		statusbar = self.statusBar()


	# --------------------------------------
	# actions
	def new(self):
		spawn = Editor(self)
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

	def preview(self):
		# open Qts preview dialog
		preview = QtGui.QPrintPreviewDialog()

		#if print is requested, open print page
		preview.paintRequested.connect(lambda doc: self.text.print_(doc))

		preview.exec_()

	def printHandler(self):

		dialog = QtGui.QPrintDialog()

		if dialog.exec_() == QtGui.QDialog.Accepted:
			self.text.document().print_(dialog.printer())

	#-------------------------------------
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


