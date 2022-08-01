from PyQt5 import QtCore, QtGui, QtWidgets
from outputwindow import Ui_outputWindow
import PyQt5
PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)

class Ui_otherWindow(object):
    #Function that connects the 'ENTER' push button to the third output display window
    def enterWindow(self):
        try:
            self.window = QtWidgets.QMainWindow()
            self.message = [self.start_station.toPlainText().title(), self.end_station.toPlainText().title(), self.timeEdit.text()]
            self.ui = Ui_outputWindow(self.message)
            self.ui.setupUi(self.window)
            self.window.show()
        except Exception as f:
            print(f)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(799, 590)

        #one line of setting image path to the background image
        self.imagePath = "london3.jpg"
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 801, 591))
        self.label.setStyleSheet("background-image: url(:/newPrefix/london3.jpg);")
        self.label.setText("")
        self.label.setScaledContents(False)
        self.label.setObjectName("label")

        #bubble middle frame
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(210, 100, 391, 441))
        self.frame.setStyleSheet("background-color: rgb(225 ,198 ,153);\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        # the code i added to make sure the image shows in the background
        self.image = QtGui.QImage(self.imagePath)
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)

        self.label.setPixmap(self.pixmapImage)

        self.stations = QtWidgets.QLabel(self.frame)
        self.stations.setGeometry(QtCore.QRect(30, 20, 331, 301))
        self.stations.setText("")
        self.stations.setStyleSheet("font: 14pt \"Century Gothic\";")
        self.stations.setObjectName("stations")

#this is label that says ' from station:'
        self.from_text = QtWidgets.QLabel(self.frame)
        self.from_text.setGeometry(QtCore.QRect(10, 50, 200, 40))
        self.from_text.setText("Enter Starting Station:")
        self.from_text.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.from_text.setObjectName("from_text")

        # this is label that says 'NOTICE!'
        self.notice = QtWidgets.QLabel(self.frame)
        self.notice.setGeometry(QtCore.QRect(160, 250, 200, 40))
        self.notice.setText("NOTICE!")
        self.notice.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.notice.setObjectName("notice label")

        # this is label that entails the train operating times notice
        self.notice = QtWidgets.QLabel(self.frame)
        self.notice.setGeometry(QtCore.QRect(110, 280, 400, 40))
        self.notice.setText("Trains operate from ")
        self.notice.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.notice.setObjectName("notice second label")

        # this is label that continues the train operating time notice
        self.notice = QtWidgets.QLabel(self.frame)
        self.notice.setGeometry(QtCore.QRect(70, 310, 400, 20))
        self.notice.setText("05:00 until midnight each day.")
        self.notice.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.notice.setObjectName("notice third label")

#this is the start station textEdit where you write your starting station
        self.start_station = QtWidgets.QPlainTextEdit(self.frame)
        self.start_station.setGeometry(QtCore.QRect(20, 90, 150, 40))
        self.start_station.setStyleSheet("background-color: rgb(156, 154, 127);\n"
"font: 10pt \"Century Gothic\";")
        self.start_station.setObjectName("start_station")

#this is the second label that says "end destination station:"
        self.end_text = QtWidgets.QLabel(self.frame)
        self.end_text.setGeometry(QtCore.QRect(10, 130, 200, 40))
        self.end_text.setText("Enter Destination Station:")
        self.end_text.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.end_text.setObjectName("end_text")

#a second textEdit that you write in your end station
        self.end_station = QtWidgets.QPlainTextEdit(self.frame)
        self.end_station.setGeometry(QtCore.QRect(20, 170, 150, 40))
        self.end_station.setStyleSheet("background-color: rgb(156, 154, 127);\n"
                                         "font: 10pt \"Century Gothic\";")
        self.end_station.setObjectName("plainTextEdit")


#A push button that says enter to take the input into output.
        self.push_btn = QtWidgets.QPushButton(self.centralwidget)
        self.push_btn.setGeometry(QtCore.QRect(445, 270, 100, 40))
        self.push_btn.setStyleSheet("font: 40 italic 14pt \"Century Gothic\";\n"
                                    "background-color: rgb(156, 154, 127);\n"
                                    "border-radius: 20px;")
        self.push_btn.setCheckable(False)
        self.push_btn.setAutoDefault(False)
        self.push_btn.setObjectName("push_btn")

        #The connection of the 'ENTER' push button to the function which displays third window.
        self.push_btn.clicked.connect(self.enterWindow)


        #Set up for a Time Edit which allows you to write in when you are leaving
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(457, 195, 85, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(18)
        self.timeEdit.setFont(font)
        self.timeEdit.setStyleSheet("border-radius: 40px;\n"
                                    "background-color: rgb(156, 154, 127);\n"
                                    "")
        self.timeEdit.setObjectName("timeEdit")

        #Label which says 'Leaving Time:'
        self.date_label = QtWidgets.QLabel(self.frame)
        self.date_label.setGeometry(QtCore.QRect(240, 50, 150, 45))
        self.date_label.setText("Leaving Time:")
        self.date_label.setStyleSheet("font: 12pt \"Century Gothic\";")
        self.date_label.setObjectName("end_text")

        #plan your journey label
        self.PlanYourJourney = QtWidgets.QLabel(self.centralwidget)
        self.PlanYourJourney.setGeometry(QtCore.QRect(120, 20, 621, 71))
        self.PlanYourJourney.setStyleSheet("color: rgb(195,176,145);\n"
"font: 81 36pt \"Rockwell Extra Bold\";")
        self.PlanYourJourney.setObjectName("PlanYourJourney")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TFL Tracker"))
        self.PlanYourJourney.setText(_translate("MainWindow", "PLAN YOUR JOURNEY"))
        self.push_btn.setText(_translate("MainWindow", "ENTER"))
#import secondary_background_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_otherWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
