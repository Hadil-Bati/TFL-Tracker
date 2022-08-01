from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from otherwindow import Ui_otherWindow
PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

class Ui_MainWindow(object):

#function i added so that the MainWindow connects to the other window
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_otherWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        MainWindow.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(823, 618)
        MainWindow.setStyleSheet("")

        #adding a one line image path for the label to show the background image
        self.imagePath = "london2.jpg"
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 900, 650))
        self.label.setStyleSheet("background-image: url(:/newPrefix/london2.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 0, 481, 71))
        self.label_2.setStyleSheet("color: rgb(195,176,145);\n"
"font: 81 35pt \"Rockwell Extra Bold\";")
        self.label_2.setObjectName("label_2")

        self.btn_open = QtWidgets.QPushButton(self.centralwidget)
        self.btn_open.setGeometry(QtCore.QRect(270, 270, 261, 61))
        self.btn_open.setStyleSheet("font: 75 italic 18pt \"Century Gothic\";\n"
"background-color: rgb(225 ,198 ,153);\n"
"border-radius: 20px;")
        self.btn_open.setCheckable(False)
        self.btn_open.setAutoDefault(False)
        self.btn_open.setObjectName("btn_open")


#This is a change i added which is click button and it connects to other Window
        self.btn_open.clicked.connect(self.openWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #the code i added to make sure the image shows in the background
        self.image = QtGui.QImage(self.imagePath)
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)
        self.label.setPixmap(self.pixmapImage)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TFL Tracker"))
        self.label_2.setText(_translate("MainWindow", "TFL TRACKER"))
        self.btn_open.setText(_translate("MainWindow", "Plan your journey"))

import mainbackground


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

