from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5
from TFL import *
import pandas as pd
import math
from prettytable import PrettyTable

PyQt5.QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
class Ui_outputWindow(object):
    ### new added message conenction to the other window
    def __init__(self, message = None):
        if message:
            self.createString(message)
        else:
            self.string = 'Error. Make sure you input the name of the stations correctly.'

    def createString(self, message):
        dijkstra = (main(message[0], message[1], message[2]))
        if type(dijkstra) == str:
            self.string = dijkstra
        else:
            list_of_stations, list_of_lines = [], []
            [list_of_stations.append(i.data) for i in dijkstra[0]]
            [list_of_lines.append(i.line) for i in dijkstra[0]]
            changes, times = dijkstra[1], dijkstra[2]
            times.append(0)
            self.string = ''
            string = ''
            total_time = dijkstra[4]
            table = PrettyTable()
            table.field_names = ("Current Station", "Line", "Time to next station", "Total Time")
            if dijkstra[4] == 0:
                self.string += 'The train is at the platform. It will depart soon!<br>' \
                               'Please mind the gap between the train and the platform.<br><br>'
            else:
                self.string += "The next train will be here in: {} minute(s)<br>" \
                               "Please mind the gap between the train and " \
                               "the platform.<br><br>".format(dijkstra[4])
            for i in range(len(list_of_lines)):
                table.add_row([list_of_stations[i], list_of_lines[i], times[i], total_time])
                total_time += times[i]

            summary = '<br><br><br>Journey Summary<br>Route: {} to {} <br>Number of changes: {}<br>Total time: {} minutes.<br>' \
                      'Estimated time of arrival: {}'.format(message[0], message[1], changes, (total_time),
                                                             dijkstra[3].strftime('%H:%M'))
            table.align = 'c'
            table.format = True
            self.string += table.get_html_string()
            self.string += summary
#We used a HTML table because other types of formatting would get printed in a distorted way.



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")


        #picture for the background
        self.imagePath = "london_pic.jpg"
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 801, 800))
        self.background.setStyleSheet("background-image: url(:/newPrefix/london_pic.jpg);")
        self.background.setText("")
        self.background.setScaledContents(False)
        self.background.setObjectName("background pic")


        # The frame used for the background bubble
        self.bubble_frame = QtWidgets.QFrame(self.centralwidget)
        self.bubble_frame.setGeometry(QtCore.QRect(50, 100, 700, 600))
        self.bubble_frame.setStyleSheet("background-color: rgb(225 ,198 ,153);\n"
                                        "border-radius: 20px;")
        self.bubble_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.bubble_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.bubble_frame.setObjectName("frame")

        # the code i added to make sure the image shows in the background
        self.image = QtGui.QImage(self.imagePath)
        self.pixmapImage = QtGui.QPixmap.fromImage(self.image)

        self.background.setPixmap(self.pixmapImage)

        # Making a scrollArea that allows scroll down.
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(65, 130, 680, 560))
        self.scrollArea.setStyleSheet("background-color: rgb(225 ,198 ,153);\n"
                                        "border-radius: 20px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 499, 389))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("verticalLayout")


        #The output label that should be connected to print the output
        self.output = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.output.setGeometry(QtCore.QRect(90, 80, 560, 600))
        self.output.setText(self.string)
        self.output.setStyleSheet("font: 11pt \"Century Gothic\";")
        self.output.setObjectName("output Text")
        self.horizontalLayout.addWidget(self.output)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #A 'back' button which closes the output window
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(300, 710, 200, 61))
        self.btn_close.setStyleSheet("font: 75 italic 18pt \"Century Gothic\";\n"
                                     "background-color: rgb(156, 154, 127);\n"
                                     "border-radius: 20px;")
        self.btn_close.setCheckable(False)
        self.btn_close.setAutoDefault(False)
        self.btn_close.setObjectName("btn_close")

        #Clicking the 'back' button will close the window
        self.btn_close.clicked.connect(MainWindow.close)



        #Label made for the 'Your Journey' title
        self.YourJourney = QtWidgets.QLabel(self.centralwidget)
        self.YourJourney.setGeometry(QtCore.QRect(170, 10, 621, 71))
        self.YourJourney.setStyleSheet("color: rgb(156, 154, 127);\n"
                                           "font: 81 40pt \"Rockwell Extra Bold\";")
        self.YourJourney.setObjectName("YourJourney")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TFL Tracker"))
        self.YourJourney.setText(_translate("MainWindow", "YOUR JOURNEY:"))
        self.btn_close.setText(_translate("MainWindow", "BACK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_outputWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())