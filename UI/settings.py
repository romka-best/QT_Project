# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
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
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        self.backButton.setGeometry(QtCore.QRect(0, 0, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(270, 60, 691, 451))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.radiopve = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.radiopve.setFont(font)
        self.radiopve.setChecked(False)
        self.radiopve.setObjectName("radiopve")
        self.gridLayout.addWidget(self.radiopve, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 3, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 4, 0, 1, 1)
        self.radiopvp = QtWidgets.QRadioButton(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.radiopvp.setFont(font)
        self.radiopvp.setChecked(True)
        self.radiopvp.setObjectName("radiopvp")
        self.gridLayout.addWidget(self.radiopvp, 0, 0, 1, 1)
        self.videoSettings = QVideoWidget(self.centralwidget)
        self.videoSettings.setGeometry(QtCore.QRect(0, 60, 271, 451))
        self.videoSettings.setObjectName("videoSettings")
        self.logoImage = QtWidgets.QLabel(self.centralwidget)
        self.logoImage.setGeometry(QtCore.QRect(270, 0, 691, 61))
        self.logoImage.setText("")
        self.logoImage.setObjectName("logoImage")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 960, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings"))
        self.backButton.setText(_translate("MainWindow", "<----- Back"))
        self.radiopve.setText(_translate("MainWindow", "PVE"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ENGLISH"))
        self.comboBox.setItemText(1, _translate("MainWindow", "RUSSIAN"))
        self.saveButton.setText(_translate("MainWindow", "SAVE"))
        self.radiopvp.setText(_translate("MainWindow", "PVP"))


from PyQt5.QtMultimediaWidgets import QVideoWidget
