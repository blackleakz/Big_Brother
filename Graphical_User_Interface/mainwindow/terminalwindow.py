# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1368, 652)
        MainWindow.setStyleSheet("background-color:    rgb(147, 147, 147);\n"
"color: rgb(0, 255, 17);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 1331, 621))
        self.groupBox.setStyleSheet("background-color:    rgb(113, 113, 113);\n"
"color: rgb(0, 255, 17);")
        self.groupBox.setTitle("")
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setObjectName("groupBox")
        self.progressBar = QtWidgets.QProgressBar(self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(10, 590, 1311, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.send_consoleLogbtn = QtWidgets.QPushButton(self.groupBox)
        self.send_consoleLogbtn.setGeometry(QtCore.QRect(640, 550, 101, 31))
        self.send_consoleLogbtn.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"color: rgb(0, 0, 0);")
        self.send_consoleLogbtn.setObjectName("send_consoleLogbtn")
        self.consoleLog = QtWidgets.QTextBrowser(self.groupBox)
        self.consoleLog.setGeometry(QtCore.QRect(20, 40, 721, 501))
        self.consoleLog.setStyleSheet("background-color:  rgb(70, 70, 70);\n"
"color: rgb(60, 255, 0);")
        self.consoleLog.setObjectName("consoleLog")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 18))
        self.label.setObjectName("label")
        self.terminal = QtWidgets.QTextBrowser(self.groupBox)
        self.terminal.setGeometry(QtCore.QRect(760, 40, 561, 501))
        self.terminal.setStyleSheet("background-color:  rgb(70, 70, 70);\n"
"color: rgb(60, 255, 0);")
        self.terminal.setObjectName("terminal")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(760, 20, 91, 18))
        self.label_2.setObjectName("label_2")
        self.send_terminalbtn = QtWidgets.QPushButton(self.groupBox)
        self.send_terminalbtn.setGeometry(QtCore.QRect(1210, 550, 101, 31))
        self.send_terminalbtn.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"color: rgb(0, 0, 0);")
        self.send_terminalbtn.setObjectName("send_terminalbtn")
        self.consoleLog_inp = QtWidgets.QLineEdit(self.groupBox)
        self.consoleLog_inp.setGeometry(QtCore.QRect(20, 550, 601, 31))
        self.consoleLog_inp.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"color: rgb(0, 0, 0);")
        self.consoleLog_inp.setObjectName("consoleLog_inp")
        self.terminal_inp = QtWidgets.QLineEdit(self.groupBox)
        self.terminal_inp.setGeometry(QtCore.QRect(760, 551, 441, 31))
        self.terminal_inp.setStyleSheet("background-color: rgb(236, 236, 236);\n"
"color: rgb(0, 0, 0);")
        self.terminal_inp.setObjectName("terminal_inp")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BigBrother v.1.0 || (c)by BlackLeakz"))
        self.send_consoleLogbtn.setText(_translate("MainWindow", "Send"))
        self.label.setText(_translate("MainWindow", "ConsoleLog"))
        self.label_2.setText(_translate("MainWindow", "Terminal"))
        self.send_terminalbtn.setText(_translate("MainWindow", "Send"))
