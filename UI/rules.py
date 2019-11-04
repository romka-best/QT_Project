# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rules.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_rules(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 540)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.backButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.backButton.setFont(font)
        self.backButton.setObjectName("backButton")
        self.horizontalLayout_2.addWidget(self.backButton, 0, QtCore.Qt.AlignLeft)
        self.logoImage = QtWidgets.QLabel(self.centralwidget)
        self.logoImage.setText("")
        self.logoImage.setObjectName("logoImage")
        self.horizontalLayout_2.addWidget(self.logoImage)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rules"))
        self.backButton.setText(_translate("MainWindow", "<----- Back"))
