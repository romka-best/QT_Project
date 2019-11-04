# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_settings(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 0, 1, 1)
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.saveButton.setFont(font)
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 3, 0, 1, 1)
        self.radiopvp = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.radiopvp.setFont(font)
        self.radiopvp.setChecked(True)
        self.radiopvp.setObjectName("radiopvp")
        self.gridLayout.addWidget(self.radiopvp, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 1, 2, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 3, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 2, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 5, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout.addWidget(self.backButton, 0, QtCore.Qt.AlignLeft)
        self.logoImage = QtWidgets.QLabel(self.centralwidget)
        self.logoImage.setText("")
        self.logoImage.setObjectName("logoImage")
        self.horizontalLayout.addWidget(self.logoImage)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Settings"))
        self.comboBox.setItemText(0, _translate("MainWindow", "ENGLISH"))
        self.saveButton.setText(_translate("MainWindow", "SAVE"))
        self.radiopvp.setText(_translate("MainWindow", "PVP"))
        self.backButton.setText(_translate("MainWindow", "<----- Back"))
