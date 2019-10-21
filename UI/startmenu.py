# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startmenu.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(240, 100, 481, 411))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.startButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.rulesButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.rulesButton.setFont(font)
        self.rulesButton.setObjectName("rulesButton")
        self.verticalLayout.addWidget(self.rulesButton)
        self.settingsButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.settingsButton.setFont(font)
        self.settingsButton.setObjectName("settingsButton")
        self.verticalLayout.addWidget(self.settingsButton)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.videoStartMenu = QVideoWidget(self.centralwidget)
        self.videoStartMenu.setGeometry(QtCore.QRect(100, 0, 761, 100))
        self.videoStartMenu.setObjectName("videoStartMenu")
        self.image1 = QtWidgets.QLabel(self.centralwidget)
        self.image1.setGeometry(QtCore.QRect(0, 200, 240, 161))
        self.image1.setText("")
        self.image1.setObjectName("image1")
        self.image2 = QtWidgets.QLabel(self.centralwidget)
        self.image2.setGeometry(QtCore.QRect(720, 200, 240, 161))
        self.image2.setText("")
        self.image2.setObjectName("image2")
        self.logoImage1 = QtWidgets.QLabel(self.centralwidget)
        self.logoImage1.setGeometry(QtCore.QRect(0, 0, 100, 100))
        self.logoImage1.setText("")
        self.logoImage1.setObjectName("logoImage1")
        self.logoImage2 = QtWidgets.QLabel(self.centralwidget)
        self.logoImage2.setGeometry(QtCore.QRect(860, 0, 100, 100))
        self.logoImage2.setText("")
        self.logoImage2.setObjectName("logoImage2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "StartMenu"))
        self.startButton.setText(_translate("MainWindow", "START"))
        self.rulesButton.setText(_translate("MainWindow", "RULES"))
        self.settingsButton.setText(_translate("MainWindow", "SETTINGS"))
        self.pushButton.setText(_translate("MainWindow", "EXIT"))


from PyQt5.QtMultimediaWidgets import QVideoWidget
