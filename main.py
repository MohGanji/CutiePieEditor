import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from Editor import Editor

def main():
	
	app = QtGui.QApplication(sys.argv)
	main = Editor()
	main.show()

	sys.exit(app.exec_())

if __name__ == "__main__":
	main()

