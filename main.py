#coding = 'utf-8'

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import Ui_form

 
#demo
def buttonClicked(girl):
    ui.pushButton.setText('changed')
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_form.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(lambda:buttonClicked(ui))
    MainWindow.show()
    sys.exit(app.exec_())