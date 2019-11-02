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
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.videoStartMenu_1 = QVideoWidget(self.centralwidget)
        self.videoStartMenu_1.setObjectName("videoStartMenu_1")
        self.gridLayout.addWidget(self.videoStartMenu_1, 1, 0, 1, 3)
        self.videoStartMenu_2 = QVideoWidget(self.centralwidget)
        self.videoStartMenu_2.setObjectName("videoStartMenu_2")
        self.gridLayout.addWidget(self.videoStartMenu_2, 1, 4, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)
        self.rulesButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.rulesButton.setFont(font)
        self.rulesButton.setObjectName("rulesButton")
        self.verticalLayout.addWidget(self.rulesButton)
        self.settingsButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.settingsButton.setFont(font)
        self.settingsButton.setObjectName("settingsButton")
        self.verticalLayout.addWidget(self.settingsButton)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.exitButton.setFont(font)
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        self.gridLayout.addLayout(self.verticalLayout, 1, 3, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 1)
        self.logoImage2 = QtWidgets.QLabel(self.centralwidget)
        self.logoImage2.setText("")
        self.logoImage2.setObjectName("logoImage2")
        self.gridLayout.addWidget(self.logoImage2, 0, 6, 1, 1)
        self.logoImage1 = QtWidgets.QLabel(self.centralwidget)
        self.logoImage1.setText("")
        self.logoImage1.setObjectName("logoImage1")
        self.gridLayout.addWidget(self.logoImage1, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 1, 1, 1)
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
        self.exitButton.setText(_translate("MainWindow", "EXIT"))
from PyQt5.QtMultimediaWidgets import QVideoWidget
