import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt

class Editor(QtGui.QMainWindow):

	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.initUI()

	def initUI(self):
		self.setGeometry(50, 50, 1266, 668)
		self.setWindowTitle("pyQtEditor")

