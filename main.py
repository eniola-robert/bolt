from PyQt5.QtGui import QKeySequence 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QMessageBox)

class MainWindow(QMainWindow):
	WindowList = []
	def __init__(self):
		super(MainWindow, self).__init__()
		self.createActions()
		self.createMenus()
		self.setWindowTitle('___')
		self.resize(400, 300)
		self.statusBar()



	def window(self):
		other = MainWindow()
		other.WindowList.append(other)
		other.show()

	def documentation(self):
		print('Please replace me')



	def about(self):
		QMessageBox.about(self, 'About the developers',
			'Wix is an online website builder with a simple drag & drop interface, meaning you do the work online and instantly publish to the web.')

	

	def createActions(self):
		self.window = QAction('&Open New Window', self, shortcut = QKeySequence.New,
			statusTip = 'Open new window', triggered = self.window)


		self._open = QAction('&Open', self, shortcut = QKeySequence.Open,
			statusTip = 'open existing file')


		self.connect = QAction('&Connect live...', self, shortcut = 'Ctrl+L',
			statusTip = 'connect to a live camera')

		self.exit = QAction('&Exit', self, shortcut = 'Ctrl+X',
			statusTip = 'close the program')


		#################### Tools bar ######################

		self.plot = QAction('&Plot graph', self, shortcut = 'Ctrl+P',
			statusTip = 'plot graph')

		self.map = QAction('&Show map', self, shortcut = 'Ctrl+M',
			statusTip = 'show map')

		########################### This is for help #####################
		self.howto = QAction('&Documentation', self, shortcut = 'Ctrl+f11', 
			statusTip = 'check how to use it', triggered = self.documentation)
		self.about = QAction('&About', self, shortcut = 'Ctrl+f12', 
				statusTip = 'Know about the developers', triggered = self.about)


	def createMenus(self):
		self.fileMenu = self.menuBar().addMenu('&File')
		self.fileMenu.addAction(self.window)
		self.fileMenu.addAction(self._open)
		self.fileMenu.addAction(self.connect)
		self.fileMenu.addAction(self.exit)


		self.surveyMenu = self.menuBar().addMenu('&Survey')
#		self.surveyMenu.addAction(self.map)
#		self.surveyMenu.addAction(self.rate)


		self.toolsMenu = self.menuBar().addMenu('&Tools')
		self.toolsMenu.addAction(self.plot)
		self.toolsMenu.addAction(self.map)

		self.helpMenu = self.menuBar().addMenu('&Help')
		self.helpMenu.addAction(self.howto)
		self.helpMenu.addAction(self.about)



if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	mainWin = MainWindow()
	mainWin.show()
	sys.exit(app.exec_())